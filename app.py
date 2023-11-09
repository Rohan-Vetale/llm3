import json
from llamaapi import LlamaAPI
from fastapi import FastAPI



app = FastAPI()
@app.get('/fetLama')


async def fetLama(prompt1: str):
    # Initialize the llamaapi with your api_token
    llama = LlamaAPI("LL-2FxqtbBbbOS82FwtvY0awiWv7jTnr1BXkFjDkfZTZEluJRJUZgZSCfK6gtCebXig")

    # Define your API request
    api_request_json = {
        "messages": [
            {"role": "user", "content": prompt1},
        ],
        
        "stream": False,
        
    }

    # Make your request and handle the response
    response = llama.run(api_request_json)
    print(json.dumps(response.json(), indent=2))
    repli = json.dumps(response.json(), indent=2)
    content1 = json.loads(repli[0])[0]['choices'][0]['message']['content']
    return {
        content1
    
    
    }


