from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

with open("logs/pipeline.log", "r") as f:
    logs = f.read()

prompt = f"""
Analyze the following ETL pipeline logs.
Identify warnings, failures, and suggest improvements.

Logs:
{logs}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)