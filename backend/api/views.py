from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data) ### in this method we get all the data
        data = model_to_dict(model_data, fields=['id','title', 'price'])

    return JsonResponse(data)
        # print(data)
        # data = dict(data)
        # json_data_str = json.dumps(data)
   # return  HttpResponse(json_data_str, headers={"content_type":"application/json"})


