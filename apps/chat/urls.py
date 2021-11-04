from django.urls import path
from . import views


urlpatterns = [
    path('guild/', views.GuildView.as_view({'get': 'list', 'post': 'create'})),
    path('guild/<int:pk>/', views.GuildView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
