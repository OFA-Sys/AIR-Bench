# AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension
[Arxiv link](https://arxiv.org/pdf/2402.07729.pdf) https://arxiv.org/pdf/2402.07729.pdf   
[**ACL 2024 Main conference**] https://aclanthology.org/2024.acl-long.109.pdf

<figure>
    <img src="Images/main_figure.png" width="60%">  
</figure>


AIR-Bench (Audio InstRuction Benchmark) is the ***First*** benchmark designed to evaluate the ability of LALMs to understand various types of audio signals (including human speech, natural sounds and music), and furthermore, to interact with humans in textual format. 

AIR-Bench encompasses two dimensions: ***foundation*** and ***chat*** benchmarks. The former consists of 19 tasks with approximately ***19k*** single-choice questions. The latter one contains ***2k*** instances of open-ended question-and-answer data.

# Overview of LALM Response  
<img src="Images/Foundation_Example.png" width="60%">

<img src="Images/Chat_Example.png" width="60%">

# LeaderBoard
- Welcome to submit **your LALM** results to issue or directly email qyang1021@zju.edu.cn. We will update the ranking list
- At present, the scoring model of our automated evaluation framework is: gpt-4-0125-preview

## Chat LeaderBoard
| Rank | Categories       | Speech | Sound | Music  | Mixed Audio | Average |
|------|------------------|--------|-------|--------|-------------|---------|
| 🏅   | Qwen2-Audio | **7.18**   | **6.99**  | **6.79** | **6.77**   | **6.93** |
| 🥈   | Qwen-Audio-Turbo | 7.04   | 6.59  | 5.98 | 5.77        | 6.34 |
|  🥉  | SALMONN          | 6.16   | 6.28  | 5.95   | 6.08        | 6.11    |
| 4  | Qwen-Audio       | 6.47   | 6.95 | 5.52   | 5.38        | 6.08    |
| 5  | Gemini-1.5-pro | 6.97   | 5.49  | 5.06 | 5.27        | 5.70 |
| 6  | BLSP             | 6.17   | 5.55  | 5.08   | 4.52        | 5.33    |
| 7    | Pandagpt         | 3.58   | 5.46  | 5.06   | 2.93        | 4.25    |
| 8    | Next-gpt         | 3.86   | 4.76  | 4.18   | 2.92        | 4.13    |
| 9    | SpeechGPT        | 1.57   | 0.95  | 0.95   | 1.14        | 1.15    |
| 10    | Macaw-LLM        | 0.97   | 1.01  | 0.91   | 1.00        | 1.01    |
|      | Whisper+GPT 4    | **7.54** | /    | /      | /           | /       |
## Foundation Leaderboard
|            Categories            | Qwen-Audio-Turbo | Qwen-Audio | Pandagpt | SALMONN | Next-gpt |  BLSP | SpeechGPT | Whisper+GPT 4 |
|:--------------------------------:|:----------------:|:----------:|:--------:|:-------:|:--------:|:-----:|:---------:|:-------------:|
|               Rank               |         🏅        |      🥈     |     🥉    |    4    |     5    |   6   |     7     |       /       |
|         Speech grounding         |       45.4%      |    56.1%   |   23.0%  |  25.3%  |   25.4%  | 25.0% |   28.8%   |     35.0%     |
|  Spoken language identification  |       95.9%      |    92.8%   |   34.6%  |  28.1%  |   23.7%  | 30.8% |   39.6%   |     96.8%     |
|    Speaker gender recognition    |       82.5%      |    67.2%   |   66.5%  |  35.5%  |   57.0%  | 33.2% |   29.2%   |     21.9%     |
|        Emotion recognition       |       60.0%      |    43.2%   |   26.0%  |  29.9%  |   25.7%  | 27.4% |   37.6%   |     59.5%     |
|      Speaker age prediction      |       58.8%      |    36.0%   |   42.5%  |  48.7%  |   62.4%  | 51.2% |   20.4%   |     41.1%     |
|     Speech entity recognition    |       48.1%      |    71.2%   |   34.0%  |  51.7%  |   26.1%  | 37.2% |   35.9%   |     69.8%     |
|       Intent classification      |       56.4%      |    77.8%   |   28.5%  |  36.7%  |   25.6%  | 46.6% |   45.8%   |     87.7%     |
|   Speaker number  verification   |       54.3%      |    35.3%   |   43.2%  |  34.3%  |   25.4%  | 28.1% |   32.6%   |     30.0%     |
|    Synthesized voice detection   |       69.3%      |    48.3%   |   53.1%  |  50.0%  |   30.8%  | 50.0% |   39.2%   |     40.5%     |
|          Audio grounding         |       41.6%      |    23.9%   |   38.3%  |  24.0%  |   62.2%  | 34.6% |   26.1%   |       /       |
|    Vocal sound classification    |       78.1%      |    84.9%   |   31.6%  |  45.3%  |   23.5%  | 29.8% |   26.2%   |       /       |
|   Acoustic scene classification  |       61.3%      |    67.5%   |   55.7%  |  34.1%  |   24.1%  | 25.2% |   23.7%   |       /       |
|     Sound question answering     |       62.8%      |    64.6%   |   48.7%  |  28.4%  |   18.8%  | 36.1% |   33.9%   |       /       |
| Music instruments classification |       59.6%      |    59.1%   |   47.7%  |  41.3%  |   24.3%  | 22.8% |   29.1%   |       /       |
|    Music genre  classfication    |       77.1%      |    71.2%   |   39.8%  |  45.3%  |   28.1%  | 26.1% |   29.3%   |       /       |
|    Music note  analysis-pitch    |       30.1%      |    28.6%   |   26.4%  |  26.4%  |   25.1%  | 23.5% |   24.1%   |       /       |
|   Music note analysis-velocity   |       25.1%      |    25.4%   |   27.2%  |  22.8%  |   23.1%  | 24.9% |   25.2%   |       /       |
|     Music question  answering    |       62.5%      |    48.2%   |   50.7%  |  54.6%  |   47.1%  | 31.0% |   31.3%   |       /       |
|      Music emotion detection     |       39.0%      |    36.1%   |   36.7%  |  32.2%  |   25.4%  | 28.3% |   29.7%   |       /       |
|              Average             |       57.8%      |    54.5%   |   40.2%  |  36.0%  |   31.5%  | 31.4% |   30.0%   |       /       |

# Download AIR-Bench
Please refer to the issue.

# Easy Evaluation
## Step1: Evaluate on Foundation Benchmark
### Inference your model on Foundation Benchmark
`python Inference_Foundation.py`
### [Optional] Alignment on Foundation Benmark
This is an optional step. This situation applies when your model cannot accurately answer ABCD and needs to be aligned with GPT.
We provide a script that can batch call GPT, you only need to do one thing: replace your own GPT call keys (MIT_SPIDER_TOKEN and MIT_SPIDER_URL).

`python align_in_foundation.py`

### Calculate score on Foundation Benchmark
`python score_foundation.py`

## Step2: Evaluate on Chat Benchmark
### Inference your model on Chat Benchmark
`python Inference_Chat.py`
### Calculate gpt score on Chat Benchmark
`python score_chat.py`
### Note
The final score is the average of the model prediction scores (remember to swap the positions of answer_gt and model prediction and then calculate the final score).
### Merge score 
Summarize the scores on the chat dataset as the final score. See cal_score.py for the simple code provided. Note that in the `cal_score` script, the average of `'speech_and_sound'` and `'speech_and_music'` is the final result of `mixed-audio`.

# License
AIR-Bench is released under Apache License Version 2.0.

# Citing
If you find this repository helpful, please consider citing it:  

> @article{yang2024air,
  title={AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension},
  author={Yang, Qian and Xu, Jin and Liu, Wenrui and Chu, Yunfei and Jiang, Ziyue and Zhou, Xiaohuan and Leng, Yichong and Lv, Yuanjun and Zhao, Zhou and Zhou, Chang and others},
  journal={arXiv preprint arXiv:2402.07729},
  year={2024}
}

