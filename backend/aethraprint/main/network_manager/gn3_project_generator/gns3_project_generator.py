from requests.models import Response


import requests
import json
from pydantic import BaseModel, Field


def createProejct(project_name,file_path,GNS3_IP,GNS3_PORT):
    
    payload = {
        "name" : project_name
    }

    url = f"http://{GNS3_IP}:{GNS3_PORT}/v2/projects"


    response: Response = requests.post(url, data=json.dumps(payload))

    if response.status_code == 201:
        project_info = response.json()
        print(f" Project Created")
        print(f":Project_ID:{project_info['project_id']}")
        print(f"Path: {project_info['path']}")
        # 이후 class로 저장 
    else:
        url = f"https://{GNS3_IP}:{GNS3_PORT}/v2/projects"
        response: Response = requests.post(url, data=json.dumps(payload))
        if response.status_code == 201:
            project_info = response.json()
            print(f" Project Created")
            print(f":Project_ID:{project_info['project_id']}")
            print(f"Path: {project_info['path']}")