from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # model instance (model data)
        # turn a python dictionary
        # return JSON to my Client
    return JsonResponse(data)
