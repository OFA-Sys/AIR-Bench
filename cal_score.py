import json

#Cir the score
input_file = 'chat_score_cir.json'
#input_file = 'chat_score.json'


with open(input_file, 'r') as fp:
   data = json.load(fp)

task_name_list = ['speech','sound','music','speech_and_sound','speech_and_music']
total_num_dict = {'speech':0, 'sound':0, 'music':0, 'speech_and_sound':0, 'speech_and_music':0}
win_num_dict = {'speech':0, 'sound':0, 'music':0, 'speech_and_sound':0, 'speech_and_music':0}
gpt4_score_sum_dict = {'speech':0, 'sound':0, 'music':0, 'speech_and_sound':0, 'speech_and_music':0}
llm_score_sum_dict = {'speech':0, 'sound':0, 'music':0, 'speech_and_sound':0, 'speech_and_music':0}
fail_num = 0
total_sum = 0
for line in data:
    task_name = line['task_name']
    if task_name == 'speech_QA' or task_name == 'speech_dialogue_QA':
        task_id = 'speech'
    elif task_name == 'music_QA' or task_name == 'music_generation_analysis_QA':
        task_id = 'music'
    elif task_name == 'sound_QA' or task_name == 'sound_generation_QA':
        task_id = 'sound'
    elif task_name == 'speech_and_sound_QA':
        task_id = 'speech_and_sound'
    elif task_name == 'speech_and_music_QA':
        task_id = 'speech_and_music'
    total_num = total_num_dict.get(task_id, 0)
    win_num = win_num_dict.get(task_id, 0)
    gpt4_socre_sum = gpt4_score_sum_dict.get(task_id, 0)
    llm_socre_sum = llm_score_sum_dict.get(task_id, 0)
    gpt_score = line['gpt-score'].strip().replace('\n','')
    scores = gpt_score.split(' ')

    if len(scores) == 2:
        try: 
        #if True:
            total_num += 1
            total_sum += 1
            gpt_score = int(scores[0])
            llm_score = int(scores[1])
            if gpt_score > 10:
                exit(1)
            if llm_score > 10:
                exit(1)
            gpt4_socre_sum += gpt_score
            llm_socre_sum += llm_score
            if 'cir' in input_file:
                if gpt_score > llm_score:
                    win_num += 1
            else:
                if llm_score > gpt_score:
                    win_num += 1

        except:
            print("gpt-4-turbo predict is: ", end='')
            print(line['gpt-score'])
            fail_num += 1
            continue
    else:
        print("gpt-4-turbo predict is: ", end='')
        print(line['gpt-score'])
        fail_num += 1
        continue

       
    total_num_dict[task_id] = total_num
    win_num_dict[task_id] = win_num
    gpt4_score_sum_dict[task_id] = gpt4_socre_sum
    llm_score_sum_dict[task_id] = llm_socre_sum

for task_id in task_name_list:
    total_num = total_num_dict[task_id]
    win_num = win_num_dict[task_id]
    gpt4_avg_score = gpt4_score_sum_dict[task_id] / total_num
    llm_avg_score = llm_score_sum_dict[task_id] / total_num
    win_ratio = win_num / total_num
    print(f'{task_id}: Sum={total_num}, Win_Rate={win_ratio}, gpt4_avg_score={gpt4_avg_score}, llm_avg_score={llm_avg_score}')

per = total_sum / (total_sum + fail_num)
print(f'fail_num: {fail_num}, success_num: {total_sum}, percentage: {per}')
