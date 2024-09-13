# Chain of Thoughts

## Overview

Welcome to the Chain of Thoughts section! This is dedicated to exploring a series of questions through a structured approach, providing insightful answers to each query. To maintain organization and clarity, the questions are stored in the `devrev_qa.json` file in JSON format, featuring a unique identifier (`qid`) for each question along with the corresponding question text.

## Structure

### 1. Questions

All questions can be found in the `devrev_qa.json` file, where each entry consists of:

- **qid**: A unique identifier for easy reference.
- **question**: The actual question presented as a string.

### 2. Prompt Template

To tackle each question systematically, utilize the `prompts.py` file, which contains the Chain of Thought prompt template. This template outlines the available tools and the methodology to approach and solve each question. Familiarize yourself with the template before diving into the questions.

## Usage

Follow these steps to obtain answers for the questions:

1. Ensure you have Python installed on your system. 
2. OPEN_API_KEY must be made available in .env file
3. Run the `cot.py` script:

    ```bash
    python cot.py
    ```

4. After running the script, an answer file will be generated for each question in the format `q{qid}.json`.

## Dependencies

- Python  3.10.10
- openai   0.27.0

## Files

- `devrev_qa.json`: JSON file containing the list of questions.
- `prompts.py`: Template for the Chain of Thought prompts, detailing available tools and methodology.
- `cot.py`: Script to run and generate answers for the questions.

## How to add new question
- To add a new question , add it in `devrev_qa.json` with a `qid` and `question`.
## How to add new tool

- To add a new tool, you just have to add the tool name , its description in the string `TOOL_DESCRIPTION` in `prompts.py`
- For each type of argument a tool requires, write the toolname and the argument inside it with its description and example. Refer to the example tools added in it.


