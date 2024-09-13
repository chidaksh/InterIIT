<!---
Acknoledgements: https://github.com/night-chen/ToolQA
-->

<div align= "center">
    <h1> 🛠️ToolQA</h1>
</div>
# ReAct

## Overview

Thought, Action and Observation prompting technique to aid solving problems involving critical thinking and logic involved.

## Usage

Follow these steps to obtain answers for the questions:

1. Ensure you have Python installed on your system. 
2. If you are using bash, add your `OPEN_AI_KEY using` following command ```export OPEN_AI_KEY='KEY'```.
3. Else, in line 27 of `tests.py`, add your `OPEN_AI_KEY` as default parameter in the `--api_key` argument.
3. Run the `tests.py` in the location `benchmark/ReAct/code/`:

    ```bash
    python tests.py
    ```
4. The questions are available in `data/qapairs.jsonl`. 


## How to add new tools ?

- In the file `prompts.py` inside `benchmark/ReAct/code` , add the information about the new tool, its description and information about the arguments in the variable `REACT_INSTRUCTION `. 

## How to add new question ?

- In the file `qapairs.jsonl` inside `data` folder , add the new question in the json format by providing an id to the question `qid` and the question in `question` field.