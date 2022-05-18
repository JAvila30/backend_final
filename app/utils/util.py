from typing import Dict, List, Tuple
from django.http.response import JsonResponse
def build_response( status_code: str, status_description: str, http_status: int, body: dict):
    print("Inicio de build_response")
    return JsonResponse({
        "httpStatus": http_status,
        "headers": 
            {
                "Content-Type":"application/json"
             },
        "executionDetails":
            {  
             "code": status_code,
            "description":status_description
        },
        "body":body,
    })
    