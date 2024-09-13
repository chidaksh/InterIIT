'''
Close-domain QA Pipeline
'''
import sys
import os
# Change the path here.
sys.path.append(os.getcwd())
import argparse
from toolbench.inference.Downstream_tasks.rapidapi import pipeline_runner

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--backbone_model', type=str, default="chatgpt_function", required=False, help='chatgpt_function or davinci or toolllama')
    parser.add_argument('--openai_key', type=str, default="", required=False, help='openai key for chatgpt_function or davinci model')
    parser.add_argument('--model_path', type=str, default="your_model_path/", required=False, help='')
    parser.add_argument('--tool_root_dir', type=str, default="your_tools_path/", required=True, help='')
    parser.add_argument("--lora", action="store_true", help="Load lora model or not.")
    parser.add_argument('--lora_path', type=str, default="your_lora_path if lora", required=False, help='')
    parser.add_argument('--max_observation_length', type=int, default=1024, required=False, help='maximum observation length')
    parser.add_argument('--max_source_sequence_length', type=int, default=4096, required=False, help='original maximum model sequence length')
    parser.add_argument('--max_sequence_length', type=int, default=8192, required=False, help='maximum model sequence length')
    parser.add_argument('--observ_compress_method', type=str, default="truncate", choices=["truncate", "filter", "random"], required=False, help='observation compress method')
    parser.add_argument('--method', type=str, default="DFS_woFilter_w2", required=False, help='method for answer generation: CoT@n,Reflexion@n,BFS,DFS,UCT_vote')
    parser.add_argument('--input_query_file', type=str, default="", required=False, help='input path')
    parser.add_argument('--output_answer_file', type=str, default="",required=False, help='output path')
    parser.add_argument('--toolbench_key', type=str, default="",required=False, help='your toolbench key to request rapidapi service')
    parser.add_argument('--rapidapi_key', type=str, default="",required=False, help='your rapidapi key to request rapidapi service')
    parser.add_argument('--use_rapidapi_key', action="store_true", help="To use customized rapidapi service or not.")
    parser.add_argument('--api_customization', action="store_true", help="To use customized api or not.")
    parser.add_argument('--corpus_tsv_path', type=str, default="corpus.xlsx",required=False, help='your corpus tsv path')
    parser.add_argument('--retrieval_model_path', type=str, default="ToolBench/ToolBench_IR_bert_based_uncased", required=False)
    parser.add_argument('--retrieved_api_nums', type=int, default=5,required=False) 
    args = parser.parse_args()
    pipeline_runner = pipeline_runner(args, add_retrieval= True)
    pipeline_runner.run()

