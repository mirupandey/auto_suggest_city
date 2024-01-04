from fastapi import FastAPI
import uvicorn
import requests
import pandas as pd
# from pydantic import BaseModel

app = FastAPI()

@app.get('/suggestions/{city}')
async def get_city_suggestion(city: str):
    url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city)
    headers = {'X-Api-Key': 'FMfzPO6dz0yccpQ/LjPNwg==buskdZFKS6eoqVl5'}
    response = requests.get(url, headers=headers)
    # , params="name,latitude,longitude")
    print("response: {}".format(response))
    final_return = {
            'suggestions': []
        }
    
    if response.status_code == requests.codes.ok:
        json_val = response.json()
        for val in json_val:
            final_return['suggestions'].append({'name': val['name'], 'latitude': val['latitude'], 'longitude': val['longitude']})
        
    return final_return


if __name__ == "__main__":
   uvicorn.run("auto_suggest_city:app", host="127.0.0.1", port=8001, reload=True)