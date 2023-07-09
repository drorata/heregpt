import openai
import os


def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
