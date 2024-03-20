'''
Easy Inference
All you need to do is fill this file with the inference module of your model.
If you want to make batch infer, please convert according to the logic of your model.
'''

import os
import argparse
import json
from tqdm import tqdm
import shutil

data_path_root = 'Foundation'  #where you download our Foundation benchmark
input_file = f'{data_path_root}/Foundation_meta.json'
output_file = 'Foundation_result_modelx.jsonl'

def main():
    #Step1: Bulid your model; Implement according to your own model
    #model = model.cuda()
    #model.eval()

    #Step2: Single step inference
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        fin = json.load(fin)
        for item in tqdm(fin):
            wav = item['path']
            task_name = item['task_name']
            dataset_name = item['dataset_name']
            if task_name =='Audio_Grounding':
                wav = item['path']
                data_path = wav_fn = f'{data_path_root}/{task_name}_{dataset_name}/{wav}'[:-3] + 'flac'
            else:
                wav = item['path']
                data_path = wav_fn = f'{data_path_root}/{task_name}_{dataset_name}/{wav}'
            if os.path.exists(wav_fn) == False:
                print(f"lack wav {wav_fn}")
                continue
            
            
            #Construct prompt
            question = item['question']
            question_prompts = 'Choose the most suitable answer from options A, B, C, and D to respond the question in next line, you may only choose A or B or C or D.'
            choice_a = item['choice_a']
            choice_b = item['choice_b']
            choice_c = item.get('choice_c', None)
            choice_d = item.get('choice_d', None)
            choices = f'A. {choice_a}\nB. {choice_b}\nC. {choice_c}\nD. {choice_d}'
            instruction = question_prompts + '\n' + question + '\n' + choices
            

            #Step 3: Run model inference
            #output = model.infer(
            #    Prompts=instruction,
            #    Audio_path=data_path,
            #    ...
            #)
            
            #target_pth = f'{data_path_root}/{task_name}_{dataset_name}'
            #file_name = data_path.split('/')[-1]
            #os.makedirs(target_pth, exist_ok=True)
            #shutil.copy(data_path, f'{target_pth}/{file_name}')


            
            output = 'A.'
            #Step 4: save result
            json_string = json.dumps(
                {
                    "path": item["path"],
                    "question": question,
                    "choice_a": choice_a,
                    "choice_b": choice_b,
                    "choice_c": choice_c,
                    "choice_d": choice_d,
                    "answer_gt": item["answer_gt"],
                    "task_name": task_name,
                    "dataset_name": dataset_name,
                    "response": output,
                    "uniq_id": item["uniq_id"],
                },
                #indent=4, 
                ensure_ascii=False
            )
            fout.write(json_string + "\n")
            

if __name__ == "__main__":
    main()