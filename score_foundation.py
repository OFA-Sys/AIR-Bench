import json

input_file = 'Foundation_result_modelx.jsonl'
fail_num = 0
task_id_list = []
total_num_dict = {}
correct_num_dict = {}

with open(input_file, 'r') as fp:
    for data in fp:
        line = json.loads(data)
        task_name = line['task_name']
        dataset_name = line['dataset_name']
        if task_name == None:
            print("1.task_name is None")
            continue
        task_id = task_name + '_' + dataset_name
        if task_id not in task_id_list:
            task_id_list.append(task_id)
        total_num = total_num_dict.get(task_id, 0)
        correct_num = correct_num_dict.get(task_id, 0)
        predict = line['response'].strip().replace('\n', '')
        if predict != 'None' and predict:
            if predict[0] == 'A' or predict[0] == 'B' or predict[0] == 'C' or predict[0] == 'D':
                gpt_predict = predict[0]
                if line['answer_gt'] == line['choice_a']:
                    gt = 'A'
                elif line['answer_gt'] == line['choice_b']:
                    gt = 'B'
                elif line['answer_gt'] == line.get('choice_c', None):
                    gt = 'C'
                elif line['answer_gt'] == line.get('choice_d', None):
                    gt = 'D'
                else:
                    print('???? gt_answer is: ', end='')
                    print(line['answer_gt'])
                    exit(1)
            #This situation may occur when the answer given by gpt is "The answer is A."
            elif len(predict) > 1:
                if predict[-2] == 'A' or predict[-2] == 'B' or predict[-2] == 'C' or predict[-2] == 'D':
                    gpt_predict = predict[-2]
                    if line['answer_gt'] == line['choice_a']:
                        gt = 'A'
                    elif line['answer_gt'] == line['choice_b']:
                        gt = 'B'
                    elif line['answer_gt'] == line.get('choice_c', None):
                        gt = 'C'
                    elif line['answer_gt'] == line.get('choice_d', None):
                        gt = 'D'
                    else:
                        print('???? gt_answer is: ', end='')
                        print(line['answer_gt'])
                        exit(1)
                else:
                    print(f'response is {predict}')
                    fail_num += 1
                    continue
            else:
                print(f'response is {predict}')
                fail_num += 1
                continue

            if gt == gpt_predict:
                total_num += 1
                correct_num += 1
            else:
                total_num += 1

            total_num_dict[task_id] = total_num
            correct_num_dict[task_id] = correct_num
            
        else:
            print('2.Response is None.')
            fail_num += 1


total_sum = 0
for task_id in task_id_list:
    total_num = total_num_dict[task_id]
    correct_num = correct_num_dict[task_id]
    acc = correct_num / total_num
    total_sum += total_num
    print(f'{task_id}: Sum={total_num}, correct={correct_num}, acc={acc}')

print(f'total_sum: {total_sum}')
print(f'fail_num: {fail_num}')


            