# AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension
[Arxiv link](https://arxiv.org/pdf/2402.07729.pdf) https://arxiv.org/pdf/2402.07729.pdf   
[ACL 2024 Main conference] Awaiting the release of the camera-ready version of PDF.

<figure>
    <img src="Images/main_figure.png" width="60%">  
</figure>


AIR-Bench (Audio InstRuction Benchmark) is the ***First*** benchmark designed to evaluate the ability of LALMs to understand various types of audio signals (including human speech, natural sounds and music), and furthermore, to interact with humans in textual format. 

AIR-Bench encompasses two dimensions: ***foundation*** and ***chat*** benchmarks. The former consists of 19 tasks with approximately ***19k*** single-choice questions. The latter one contains ***2k*** instances of open-ended question-and-answer data.

# Overview of LALM Response  
<img src="Images/Foundation_Example.png" width="60%">

<img src="Images/Chat_Example.png" width="60%">


# Download AIR-Bench
Refer to the issue.

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

# Citing
If you find this repository helpful, please consider citing it:  

> @article{yang2024air,
  title={AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension},
  author={Yang, Qian and Xu, Jin and Liu, Wenrui and Chu, Yunfei and Jiang, Ziyue and Zhou, Xiaohuan and Leng, Yichong and Lv, Yuanjun and Zhao, Zhou and Zhou, Chang and others},
  journal={arXiv preprint arXiv:2402.07729},
  year={2024}
}

