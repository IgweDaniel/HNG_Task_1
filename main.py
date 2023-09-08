from typing import Union
from fastapi import FastAPI
from datetime import datetime, timezone
app = FastAPI()


@app.get("/api")
def read_root(slack_name: str, track:str):
    dt = datetime.now(timezone.utc)
    return {
        "slack_name":slack_name,
        "current_day":dt.strftime('%A'),
        "utc_time":dt.timestamp() ,
        "track":track,
        "github_file_url":"https://github.com/IgweDaniel/HNG_Task_1/blob/main/main.py",
        "github_repo_url":"https://github.com/IgweDaniel/HNG_Task_1",
        "status_code":200
    }



