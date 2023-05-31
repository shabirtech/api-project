from django.urls import path

from . import views

urlpatterns = [
    ### url using class base view

    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view),


    ### url of function base view 
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
]
