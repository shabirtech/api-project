from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF api view
    """
    serializer =  ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() 
        print(serializer.data)
        
        return Response(serializer.data)
  
    return Response({"Invalid": "Not good data"}, status=400)


