# Drone LLM Experiments

This project was done for my class CSE 233: Advanced Computer Security. 

In this project, we investigate the performance of LLMs under these adversarial conditions, examining their ability to detect and respond to perception and GPS spoofing attacks. Specifically, we analyze whether LLMs can identify inconsistencies in textual scene descriptions caused by these attacks and evaluate their effectiveness as an additional layer of security. Furthermore, we explore tailored prompting techniques to enhance the LLMs’ ability to recognize anomalies and improve their robustness against adversarial manipulation. Through these experiments, we aim to assess the viability of LLMs as a defense mechanism in autonomous drone operations and contribute insights into their potential role in enhancing cybersecurity for AI-powered systems.

These files will run different types of tests

## CHATGPT API KEY

Make sure you have your own OPENAI API key. This is required to run the code.

If you do not have one setup in the environment, run the following command in your terminal (Windows):

```bash
setx OPEn_API_KEY "{API key}"
```

## Usage

To run the tests and generate the output, use the following command in your terminal:

```bash
python tests.py 'type of test (a, h, b, t)'
```

Here are what each of the command arguments do:
- a: runs a test comparing a drone LLM without prompting and a drone LLM with prompting and history frames on scenes with inconsistencies. The results will be shown in a graph which is saved as 'drone_graph_comparison.png' and will be appended to output.json.
- h: runs a test comparing a drone LLM with prompting but with different numbers of history in decreasing order from 4 to 1. The results will be shown in a graph which is saved as 'drone_graph_history_frames.png' and will be appended to output.
- b: (Unfinished) runs a test comparing a drone LLM without prompting and a drone LLM with prompting and history frames on benign scenes.
- t: runs one test on a drone LLM with prompting and history frames on the temporal inconsistency scene and prints the output.
