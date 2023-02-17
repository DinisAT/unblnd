import openai
import os
from dotenv import load_dotenv

load_dotenv()

def gen_first_question():
    openai.api_key = os.getenv('OPENAI_API_KEY')


    string = input('Generate a random topic, and question me is I like it with no more then 8 words')

    response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=string,
                max_tokens=10,
                temperature=0.8,
                top_p=0.2
                )
    if response.get('choices')[0].get('text'):
        return response.get('choices')[0].get('text'):
