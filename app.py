import json
from llamaapi import LlamaAPI
from fastapi import FastAPI, Request



app = FastAPI()
@app.get('/fetLama')


async def fetLama(chara: str, prompt1: str):
    # Initialize the llamaapi with your api_token
    llama = LlamaAPI("LL-2FxqtbBbbOS82FwtvY0awiWv7jTnr1BXkFjDkfZTZEluJRJUZgZSCfK6gtCebXig")

    # Define your API request
    api_request_json = {
        "messages": [
            {"role": "user", "content": "act as "+ chara + " and answer the following question in english under 50 words. " + prompt1},
        ],
        
        "stream": False,
        
    }
 
    # Make your request and handle the response
    response = llama.run(api_request_json)
   # peso = response.json()
   # peso = jeso['choices'][0]['message']
    json_response1 = json.dumps(response.json())
    
    
    
    return {
        json_response1
    
    
    }

