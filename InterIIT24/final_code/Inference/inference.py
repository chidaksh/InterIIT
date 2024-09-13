# Change the number of iterations as required
NUM_ITERATIONS=20


import openai
import os
from dotenv import load_dotenv
import json 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
import argparse



def tokenSummary(data):
    print(data['usage'])
def generate_prompt(question):

    # Make a call to the OpenAI API using v1/chat/completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat-based model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )

    generated_answer = response['choices'][0]['message']['content'].strip()

    return generated_answer,response


parser = argparse.ArgumentParser(description='Process input and save to output file')

# Add input and output file arguments
parser.add_argument('input_filename', type=str, help='Input filename')
parser.add_argument('output_filename', type=str, help='Output filename')

# Parse command-line arguments
args = parser.parse_args()

# Access the values of input and output filenames
input_filename = args.input_filename
output_filename = args.output_filename

with open(input_filename, 'r') as file:
    questions_data = json.load(file)

truth = []

with open("output_responses.csv", "w") as output_file:
    for i in range(NUM_ITERATIONS):
        for question_data in questions_data:
            question = question_data['question']
            gnd = question_data['gnd']
            mod = question_data['mod']
            qid = question_data["qid"]
            win = question_data["win"]
            truth.append(win)
            PROMPT_TEMPLATE = f"""Choose [1] or [2] for your preference.If both same then output [1] for the question :: {question}\nPlease don't provide reasons. 
            You must follow the following criteria
            - Informative: whether it contains all necessary information to reply to the query.
            - Factuality: whether it accurately describes what has been done, and what failed in the end.
            - Reasoning: If answer does not solve the query, whether gives a detailed and accurate reason for failure.
            
            \n\n1) {mod}\n2) {gnd}\n \n\nPlease Print Only [1] or [2] and nothing else in your output"""

            answer, _ = generate_prompt(PROMPT_TEMPLATE)
            print(f"RESPONSE {answer}")
            output_file.write(f"{qid},{answer}\n")


# 1 is Model output
# 2 is Ground truth

import pandas as pd

# Read the CSV file without specifying column names
df = pd.read_csv("output_responses.csv", header=None)

# Assign column names to make the code more readable
df.columns = ['qid', 'choosenPath']

# Initialize counters for preference comparison
ground_truth_count = 0
model_output_count = 0

# Initialize counters for overall preference count
overall_ground_truth_count = 0
overall_model_output_count = 0

# Initialize dictionaries to store counts per question for each path
ground_truth_counts_per_question = {}
model_output_counts_per_question = {}

# Group data by question ID (qid) and calculate statistics
grouped_data = df.groupby('qid')['choosenPath'].value_counts().unstack(fill_value=0)

# Open a file for writing
print(grouped_data)
with open(output_filename+".txt", "w") as output_file:
    # Print statistics for each question
    for qid, row in grouped_data.iterrows():
        output_file.write(f"\nQuestion {qid}:\n")
        total_responses = row.sum()
        model_output_counts_per_question[qid]=0
        ground_truth_counts_per_question[qid]=0
        # Determine preferred path for each question
        preferred_path = row.idxmax()
        output_file.write(f"  Preferred Path: {preferred_path}\n")

        # Update counts for the preferred path per question
        if preferred_path == 2:
            ground_truth_count += 1
            ground_truth_counts_per_question[qid] = ground_truth_counts_per_question.get(qid, 0) + 1
        elif preferred_path == 1:
            model_output_count += 1
            model_output_counts_per_question[qid] = model_output_counts_per_question.get(qid, 0) + 1

        # Display counts and percentages for each path
        for path, count in row.items():
            percentage = (count / total_responses) * 100
            output_file.write(f"  Path {path}: {count} times ({percentage:.2f}% of total responses)\n")

    # Display overall preference counts and percentages
    output_file.write(f"\nPath 1 is preferred for {sum(model_output_counts_per_question.values())} questions")
    output_file.write(f"\nPath 2 is preferred for {sum(ground_truth_counts_per_question.values())} questions")



    # Display overall counts for each path
    overall_counts = df['choosenPath'].value_counts()
    output_file.write("\nOverall Counts:\n")
    for path, count in overall_counts.items():
        output_file.write(f"  Path {path}: {count} times\n")

    print(overall_counts)
    total_choices = len(df)
    percentage_path1 = (overall_counts[1] / total_choices) * 100 if 1 in overall_counts else 0
    percentage_path2 = (overall_counts[2] / total_choices) * 100 if 2 in overall_counts else 0

    # Display the percentages
    output_file.write(f"\nPercentage of times each path is chosen:\n")
    output_file.write(f"  Path1: {percentage_path1:.2f}%\n")
    output_file.write(f"  Path2: {percentage_path2:.2f}%\n")


    model_accuracy = sum(truth)*100.0/len(truth)
    output_file.write(f"\n Model Accuracy with given data: {model_accuracy} %\n")
    # Determine the preferred path
    preferred_path = 'Model path' if percentage_path1 > percentage_path2 else 'Human path'
    output_file.write(f"\n Therefore Preferred Path: {preferred_path}\n")