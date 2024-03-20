# -*- coding: utf-8 -*-
import json
import os
import random
import time
import logging
import shortuuid
from copy import deepcopy
from concurrent.futures.thread import ThreadPoolExecutor
import threading
import argparse
from func_timeout import func_set_timeout
import os
import time
import random
import requests
import jsonlines
import pandas as pd
from tqdm import tqdm

MAX_API_RETRY = 3
LLM_MIT_RETRY_SLEEP = 5

os.environ['MIT_SPIDER_TOKEN'] = ''
os.environ['MIT_SPIDER_URL'] = ''



def load_file2list(path):
    res = []
    with open(path,'r+',encoding='utf8') as f:
        for item in jsonlines.Reader(f):
            res.append(item)
    return res




def mit_openai_api(**kwargs):
    if not os.environ.get('MIT_SPIDER_TOKEN', None):
        print("NO MIT_SPIDER_TOKEN FOUND，please set export MIT_SPIDER_TOKEN=<YOUR TOKEN>")
    if not os.environ.get('MIT_SPIDER_URL', None):
        print("NO MIT_SPIDER_URL FOUND，please set export MIT_SPIDER_URL=<YOUR URL>")
    mit_spider_config = {
        "url": os.environ.get("MIT_SPIDER_URL", None),
        "header": {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('MIT_SPIDER_TOKEN', None)}"
        }
    }
    tenant = None
    response = None
    for i in range(MAX_API_RETRY):
        try:
            if tenant:
                payload = {'tenant': tenant}
            else:
                payload = dict()
            for k, w in kwargs.items():
                payload[f"{k}"] = w
            response = requests.post(mit_spider_config['url'], json=payload, headers=mit_spider_config['header']).json()
        except Exception as e:
            print(response, e)
            time.sleep(LLM_MIT_RETRY_SLEEP)
            continue
        
        if response['code'] == 200:
            return response
        else:
            time.sleep(LLM_MIT_RETRY_SLEEP)
            print(response)
    return None

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S')
logger = logging.getLogger(__name__)
lock = threading.Lock()
finish_count = 0
failed_count = 0


@func_set_timeout(1200)
def get_result_by_request(**kwargs):
    response = mit_openai_api(**kwargs)
    if response['code'] == 200:
        result = response['data']['response']['choices'][0]['message']['content']
        prompt_tokens = response['data']['prompt_tokens']
        completion_tokens = response['data']['completion_tokens']
        finish_reason = response['data']['response']['choices'][0]['finish_reason']
        return result, prompt_tokens, completion_tokens, finish_reason

    else:
        raise Exception(response['messages'])
       


def task(data, writer, args):
    global finish_count
    global failed_count
    openai_args = {
        'model': args.model_name,
        'temperature': args.temperature,
        'max_tokens': args.max_tokens
    }
    openai_args.update(data['openai_args'])
    for i in range(MAX_API_RETRY):
        try:
            result, prompt_tokens, completion_tokens, finish_reason = get_result_by_request(**openai_args)
            item = deepcopy(data)
            item.update({
                "gen": result,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "finish_reason": finish_reason
            })
            lock.acquire()
            finish_count += 1
            writer.write(json.dumps(item, ensure_ascii=False) + "\n")
            writer.flush()
            lock.release()
            return

        except Exception as e:
            print("request error", e)
            pass

    lock.acquire()
    failed_count += 1
    lock.release()


def get_unprocessed_data(args, out_file):
    data_l = list()
    uuid_s = set()
    if os.path.exists(out_file):    
        out_data_l = load_file2list(out_file)
        for data in out_data_l:
            if data['gen'] != 'error':
                uuid_s.add(data[args.uuid])
    for data in load_file2list(args.in_file):
        if data[args.uuid] in uuid_s:
            continue
        data_l.append(data)
    return data_l


def run_chat_gen(args):
    if args.out_file:
        out_file = args.out_file
    else:
        out_file = os.path.splitext(args.in_file)[0] + '_result.jsonl'
    items = get_unprocessed_data(args, out_file)

    pool = ThreadPoolExecutor(max_workers=args.num_workers)
    writer = open(out_file, 'a', encoding='utf8')
    total_count = 0
    global finish_count, failed_count
    for item in items:
        total_count += 1
        pool.submit(task, item, writer, args)
    while finish_count + failed_count < total_count:
        logger.info(f"total:{total_count}  finish:{finish_count}  failed:{failed_count}")
        time.sleep(10)

    time.sleep(10)
    writer.close()


def build_test_file():
    root = '.'
    level_2_output = ''



    with open(os.path.join(root, 'batch_run_input.jsonl'), 'w', encoding='utf-8') as writer, open(level_2_output, 'r') as fin:
            data = json.load(fin)
            for index,row in enumerate(data):
                system_prompt = 'There is a question "QUESTION", and one response is "ANSWER". Among the following choices, which option best matches this response? You may only response with the letter of the option. If the letter of an option has already appeared in the Answer, then simply return that letter. If there are no matching options, then choose one at random. The following lines are the options.'
                path = row['path']
                question = row['question']
                choice_a = row['choice_a']
                choice_b = row['choice_b']
                choice_c = row.get('choice_c', None)
                choice_d = row.get('choice_d', None)
                answer_gt = row['answer_gt']
                task_name = row['task_name']
                dataset_name = row['dataset_name']
                response = row['response']
                

                if response == None:
                    continue
                system_prompt = system_prompt.replace("ANSWER", response).replace("QUESTION", question)
                attention = 'To reiterate, the response you provide to me must be a single letter, either A, B, C, or D.'
                if choice_c == None or choice_d == None:
                    content = system_prompt + '\nA. ' + choice_a + '\nB. ' + choice_b + '\n' + attention
                else:
                    content = system_prompt + '\nA. ' + choice_a + '\nB. ' + choice_b + '\nC. ' + choice_c + '\nD. ' + choice_d + '\n' + attention
                tmp_d = {
                    'uuid': shortuuid.uuid(),
                    'openai_args': {
                        "messages": [{"role": "user", "content": content}]
                    },
                    'path': path,
                    'question': question,
                    'choice_a': choice_a,
                    'choice_b': choice_b,
                    'choice_c': choice_c,
                    'choice_d': choice_d,
                    'answer_gt': answer_gt,
                    'task_name': task_name,
                    'dataset_name': dataset_name,
                    'response': response,
                }
                if random.random() < 0.5:
                    tmp_d['openai_args'].update({"temperature": 2.0})
                writer.write(json.dumps(tmp_d, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="llm gen")
    parser.add_argument("-r", "--root", type=str)
    parser.add_argument("-i", "--in-file", type=str, default='batch_run_input.jsonl')
    parser.add_argument("-o", "--out-file", type=str, default='batch_run_output.jsonl')
    parser.add_argument("-n", "--num-workers", type=int, default=50)     #max=50
    parser.add_argument("-m", "--model-name", type=str, default='gpt-3.5-turbo')
    parser.add_argument("-t", "--temperature", type=float, default=1.0)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--uuid", type=str, default='uuid')

    args = parser.parse_args()
    
    #step 1
    build_test_file()

    #step 2
    run_chat_gen(args)
