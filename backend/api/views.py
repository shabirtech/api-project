from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    #request > HttpRequest > Django
    # print(dir(request))
    # request.body

    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body) #string of json data to python dict
    except:
        pass

    print(data)
    # print(data.keys())
    # print(data.values())
    data['params'] = dict(request.GET) 
    data['headers']=dict(request.headers)
    print(request.headers)
    # json.dumps(dict(request.headers))
    data['content_type'] = request.content_type
    return JsonResponse(data)
