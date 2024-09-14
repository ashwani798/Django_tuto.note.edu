
from django.urls import path
from . import views

#localhost:8000/ashu
#localhost:8000/ashu/order
urlpatterns = [
    path('', views.all_ashu, name='all_ashu'),
    path('<int:ashu_id>/', views.ashu_detail, name='ashu_detail'),
    path('ashu_stores/', views.ashu_store_view, name='ashu_stores'),

]