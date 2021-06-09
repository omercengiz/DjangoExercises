
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd

@csrf_exempt
def maps_func(request):
    if request.method == 'GET':
        return HttpResponse(content=None)
    elif request.method == 'POST':
        response_dict = dict()
        df = pd.read_csv("us_accidents.csv")
        
        received_json_data = json.loads(request.body.decode("utf-8"))
        
        (x1, y1) = received_json_data["x1"], received_json_data["y1"]
        (x2, y2) = received_json_data["x2"], received_json_data["y2"]

        df_json = df[
            (df['Start_Lat'] >= x1) & (df['Start_Lat'] <= x2)
            & (df['Start_Lng'] >= y2) & (df['Start_Lng'] <= y1)
        ]

        df_json.columns = ["lat", "lng", "description"]
        
        
        response = JsonResponse({
            "result": json.loads(df_json.to_json(orient="records"))
            }, safe=False)
        return response
    
"""

{
    "response":[
        {"lat":22,"lng":21,"description":"kazanın sebebi"},
        ]
}

"""