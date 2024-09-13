# Setup
```
pip install -r requirements.txt
```


# Steps to run
```
python ./toolbench/inference/qa_pipeline.py     --tool_root_dir ./data/toolenv/tools/  --openai_key <openai_key> --input_query_file ./devrev_single_query.json --output_answer_file ./output/     --api_customization
```

## Steps to add new APIs
Inside the data/toolenv/tools folder add your tools inside a new folder. 
Use agent007.json as example and add your own tools.

## Add new queries
Write your query in the file following the format given in devrev_single_query.json.

The output for the questions given in the problem statements are in output folder.
*_devrev.json has the output in the required format.