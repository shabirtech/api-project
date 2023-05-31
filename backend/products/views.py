from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def  perform_create(self, serializer):
        ## serializer.save(user= self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
       
        serializer.save(content = content)

        ## send a django signal


product_list_create_view= ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



product_update_view = ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self,instance):
        super().perform_destroy(instance)
    



product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_list_view = ProductListAPIView.as_view()


class ProductMixinView(mixins.ListModelMixin,generics.CreateAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self, request,*args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def  perform_create(self, serializer):
        ## serializer.save(user= self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "This is a single view doing cool stuff"
       
        serializer.save(content = content)

product_mixin_view=ProductMixinView.as_view()


@api_view(["GET", "POST"])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            ## get response -> detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)

        ## list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)




    if method == "POST":
        ## create an item 
        serializer =  ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({'Invalid': "not good data" }, status=400)