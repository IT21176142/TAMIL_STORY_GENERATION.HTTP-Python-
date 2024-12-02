from apiconfig import ModelStory
from prompts import story_generation_tamil_prompt
from fastapi import FastAPI
import uvicorn
from openai import OpenAI
import os
import yaml
import json



with open('./config/config.yml', 'r') as file:
    config_keys = yaml.safe_load(file)


gpt_fine_tune_key = config_keys['OPEN_AI_KEY']
fine_tune_job_id = config_keys['FINE_TUNE_JOB_ID']

client = OpenAI(api_key = gpt_fine_tune_key)


def generate_tamil_story(model_id, test_input):
    """Test the fine-tuned model"""
    try:
        completion = client.chat.completions.create(
            model=model_id,
            messages=story_generation_tamil_prompt(test_input)
        )
        return completion.choices[0].message.content
    except Exception as e:
        return ''

def generate_tamil_story_func(user_id, test_input):
    try: 
        response = generate_tamil_story(fine_tune_job_id, test_input)
        response_json = {
            'user_id': user_id,
            'heading': test_input,
            'story': response
        }
        return response_json, '', 200
    except Exception as e:
        return '', str(e), 400


app = FastAPI(docs_url=None, redoc_url=None)

@app.get('/info')
def index():
    return {'result': {'message': 'Tamil Story Generation Service'}, 'code': 200, 'error': ''}

@app.get('/health')
def health_check():
    return {'result': {'message': 'Tamil Story Generation Service'}, 'code': 200, 'error': ''}

@app.post('/generate/story/tamil')
def predict_voice_speech(data: ModelStory):
    if not data.user or not data.text:
        return {'result': '', 'code': 400, 'error': {'message': 'story generation failed! Please send proper request.'}}
    
    result, error, status = generate_tamil_story_func(data.user, data.text)
    return {'result': result, 'code': status, 'error': error}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


