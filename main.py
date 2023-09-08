from typing import Union
from fastapi import FastAPI
from datetime import datetime, timezone
app = FastAPI()


@app.get("/api")
def read_root(slack_name: str, track:str):
    current_time_utc = datetime.utcnow()

# Format it as a string in the desired format
    formatted_time = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    return {
        "slack_name":slack_name,
        "current_day":current_time_utc.strftime('%A'),
        "utc_time":formatted_time ,
        "track":track,
        "github_file_url":"https://github.com/IgweDaniel/HNG_Task_1/blob/main/main.py",
        "github_repo_url":"https://github.com/IgweDaniel/HNG_Task_1",
        "status_code":200
    }



