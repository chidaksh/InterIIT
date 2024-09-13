import openai
import os
from dotenv import load_dotenv
import json 
from prompts import PROMPT_TEMPLATE
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


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


with open('devrev_qa.json', 'r') as file:
    questions_data = json.load(file)



for question_data in questions_data:
    question = question_data['question']
    qid = question_data["qid"]
    try:
        answer, _ = generate_prompt(PROMPT_TEMPLATE + question)

        response_data = {
            "question": question,
            "answer": json.loads(answer)  # Parse the JSON string to a Python object
        }
        with open(f'q{qid}.json', 'w') as json_file:
            json.dump(response_data, json_file, indent=2)
        print(f"RESPONSE {answer}")

    except:
        print("Error in recieving prompt")
