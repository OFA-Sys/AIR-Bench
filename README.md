# AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension
[Arxiv link](https://arxiv.org/pdf/2402.07729.pdf) https://arxiv.org/pdf/2402.07729.pdf   
[**ACL 2024 Main conference**] Awaiting the release of the camera-ready version of PDF.

<figure>
    <img src="Images/main_figure.png" width="60%">  
</figure>


AIR-Bench (Audio InstRuction Benchmark) is the ***First*** benchmark designed to evaluate the ability of LALMs to understand various types of audio signals (including human speech, natural sounds and music), and furthermore, to interact with humans in textual format. 

AIR-Bench encompasses two dimensions: ***foundation*** and ***chat*** benchmarks. The former consists of 19 tasks with approximately ***19k*** single-choice questions. The latter one contains ***2k*** instances of open-ended question-and-answer data.

# Overview of LALM Response  
<img src="Images/Foundation_Example.png" width="60%">

<img src="Images/Chat_Example.png" width="60%">

# LeaderBoard
- We are eagerly looking forward to evaluating **gpt4o**（after the audio interface is made available).
| Rank |     Benchmark    | Foundation                                  |   |   Chat                                             |
|------|:----------------:|:----------:|:---------:|:---------:|:---------:|---|:--------:|----------|----------|-------------|----------|
|      |    Categories    |   Speech   |   Sound   |   Music   |  Average  |   |  Speech  |   Sound  |   Music  | Mixed Audio |  Average |
| 🏅    | Qwen-Audio-Turbo |  **63.4%** | **61.0%** | **48.9%** | **57.8%** |   |   7.04   |   6.59   | **5.98** |     5.77    | **6.34** |
| 🥈    |      SALMONN     |    37.8%   |   33.0%   |   37.1%   |   36.0%   |   |   6.16   |   6.28   |   5.95   |     6.08    |   6.11   |
| 🥉    |    Qwen-Audio    |    58.7%   |   60.2%   |   44.8%   |   54.5%   |   |   6.47   | **6.95** |   5.52   |     5.38    |   6.08   |
| 4    |       BLSP       |    36.6%   |   31.4%   |   26.1%   |   31.4%   |   |   6.17   |   5.55   |   5.08   |     4.52    |   5.33   |
| 5    |     Pandagpt     |    39.0%   |   43.6%   |   38.1%   |   40.2%   |   |   3.58   |   5.46   |   5.06   |     2.93    |   4.25   |
| 6    |     Next-gpt     |    33.6%   |   32.2%   |   28.9%   |   31.5%   |   |   3.86   |   4.76   |   4.18   |     2.92    |   4.13   |
| 7    |     SpeechGPT    |    34.3%   |   27.5%   |   28.1%   |   30.0%   |   |   1.57   |   0.95   |   0.95   |     1.14    |   1.15   |
| 8    |     Macaw-LLM    |    32.2%   |   30.1%   |   29.7%   |   30.7%   |   |   0.97   |   1.01   |   0.91   |     1.00    |   1.01   |
|      |   Whisper+GPT 4  |    53.6%   |     /     |     /     |     /     |   | **7.54** |     /    |     /    |      /      |     /    |

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
### Calculate score on Chat Benchmark
`python score_chat.py`

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

