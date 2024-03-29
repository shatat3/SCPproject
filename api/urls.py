from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view())   
]

urlpatterns = format_suffix_patterns(urlpatterns)
