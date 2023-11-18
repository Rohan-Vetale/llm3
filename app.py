import json
from llamaapi import LlamaAPI
from fastapi import FastAPI



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
    json_response1 = json.dumps(response.json(), indent=2)
    json_response2 = json.loads(json_response1)

    # Extracting "content"
    content1 = json_response2["choices"][0]["message"]["content"]
    
    return {
        content1
    
    
    }


