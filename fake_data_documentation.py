from dotenv import load_dotenv
load_dotenv(override=True)

import os
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
from openai import OpenAI
openai = OpenAI()
num_para = int(input("Enter the number of parameters:"))
list_of_paras = []
for i in range(num_para):
    para = input(f"Enter parameter{i}:")
    list_of_paras.append(para)

num_of_data_requested = int(input("Enter number of records requested to generate:"))

your_role = '''
You are a Python assistant that must return only valid Python code.
Do NOT include markdown backticks, comments, explanations, or any text at all.
Only return executable code, as plain text. No formatting, no headers, no footers.
'''

generate_job = f"Write python code to generate fake data on parameters in the list {list_of_paras} for {num_of_data_requested} records, convert it to .ods file, use pandas and engine as odf "
messages = [{"role": "system", "content": your_role}, {"role": "user", "content": generate_job}]


response = openai.chat.completions.create(
    model="gpt-4o",
    messages=messages
)

code = response.choices[0].message.content.strip()

if code.startswith("```") and code.endswith("```"):
    code = '\n'.join(code.split('\n')[1:-1])

print(code)

from pathlib import Path 

file_path = Path("Generated_records.py")
file_path.write_text(code, encoding="utf-8")

import subprocess

result = subprocess.run(["python", str(file_path)], capture_output=True, text=True)


if result.stdout:
    print(result.stdout)
if result.stderr:
    print("Errors:\n", result.stderr)
