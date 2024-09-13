# Inference on Tooleval guidelines

## Overview

The preference of model is tested in this code using ideas from Tooleval.


## Usage

Follow these steps to obtain answers for the questions:

1. Ensure you have Python installed on your system. 
2. OPEN_API_KEY must be made available in .env file
3. Run the `inference.py` script:

    ```bash
    python inference.py toolllm.json toollm_inference
    ```
4. The first argument is input json and second is output file. Input can be `react.json` or  `toolllm.json` or `cot.json` 
5. After running the script, output file will have accuracies and preferred paths.

## Files

- `toolllm.json`: JSON file containing the list of questions , model and expected flow of ToolLLM
- `react.json`: JSON file containing the list of questions , model and expected flow of React prompting.
- `cot.json`: JSON file containing the list of questions , model and expected flow of COT prompting.

- `inference.py`: Script to run and generate inferences for the questions of given model.