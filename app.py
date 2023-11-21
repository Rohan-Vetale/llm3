import json
from llamaapi import LlamaAPI
from fastapi import FastAPI, Request



app = FastAPI()
@app.post('/fetLama')


async def fetLama(request: Request):
    # Initialize the llamaapi with your api_token
    llama = LlamaAPI("LL-2FxqtbBbbOS82FwtvY0awiWv7jTnr1BXkFjDkfZTZEluJRJUZgZSCfK6gtCebXig")

    # Define your API request
    api_request_json = request
 
    # Make your request and handle the response
    
    response = llama.run(api_request_json)
    jeso = response.json()
    json_response1 = json.dumps(response.json())
    # Extracting "content"
    content1 = json_response1["choices"][0]["message"]["content"]
    
    return {
        content1
    
    
    }


