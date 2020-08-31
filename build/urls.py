from django.urls import include
from django.urls import path
from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
urlpatterns = [
    path('', views.ListFlowers.as_view()),
    path('<int:pk>/', views.DetailFlowers.as_view()),
]