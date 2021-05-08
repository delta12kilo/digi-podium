from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # path('',views.home,name='home'),
    path('', views.cardView.as_view(),name='post_list'),
    path('<slug:proo>-enroll/',views.registerStuff.as_view(), name='nproo')
]