import json
from llamaapi import LlamaAPI
from fastapi import FastAPI, Request
from fastapi import HTTPException


app = FastAPI()
@app.get('/fetLama')


async def fetLama(chara: str, prompt1: str):
    # Initialize the llamaapi with your api_token
    llama = LlamaAPI("LL-2FxqtbBbbOS82FwtvY0awiWv7jTnr1BXkFjDkfZTZEluJRJUZgZSCfK6gtCebXig")

    # Define your API request
    api_request_json = {
        "messages": [
            {"role": "user", "content": "keep replies short,  do not use any emojis"},
            {"role": "user", "content": "act as "+ chara + " , do not greet if not asked, and reply the following shortly in english accordingly " + prompt1}
        ],
        
        "stream": False,
        
    }
 
    # Make your request and handle the response
    response = llama.run(api_request_json)
    jeso = response.json()
    peso = jeso['choices'][0]['message']['content']
    
    
    
    
    return {
        peso
    
    
    }





@app.post('/fetLama2')
async def fetch_lama(request: Request):
    try:
        # Parse JSON content from the request
        request_json = await request.json()
        
        # Extract values from the JSON payload
        chara = request_json.get("chara")
        prompt1 = request_json.get("prompt1")
        
        if not chara or not prompt1:
            raise HTTPException(status_code=400, detail="Both 'chara' and 'prompt1' are required in the request payload.")
        
        # Initialize the llamaapi with your api_token
        llama = LlamaAPI("LL-2FxqtbBbbOS82FwtvY0awiWv7jTnr1BXkFjDkfZTZEluJRJUZgZSCfK6gtCebXig")

        # Define your API request
        api_request_json = {
            "messages": [
                {"role": "user", "content": "keep replies short under 30 words, do not include any non-utf characters, only use English, do not use any emojis"},
                {"role": "user", "content": f"act as {chara} and answer the following question in English under 30 words."},
                {"role": "user", "content": f"{prompt1}"}
            ],
            "stream": False,
        }

        # Make your request and handle the response
        response2 = llama.run(api_request_json)
        jeso2 = response2.json()
        peso2 = jeso2['choices'][0]['message']['content']

        return {"response": peso2}
    
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
