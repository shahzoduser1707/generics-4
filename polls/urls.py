from django.urls import path
from .views import GetHome,CreateHome,GetCreateHome,DetailUpdateDestroy


urlpatterns = [
    path('getHome/',GetHome.as_view()),
    path('createHome/',CreateHome.as_view()),
    path('getcreateHome/',GetCreateHome.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]