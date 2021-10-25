from django.urls import path
from .endpoint import views, auth_views


urlpatterns = [
    path('me/', views.MeView.as_view({'get': 'retrieve', 'put': 'update'})),

    path('user/', views.UserView.as_view({'get': 'list'})),
    path('user/<int:pk>/', views.UserView.as_view({'get': 'retrieve'})),

    path('social/', views.SocialLinkView.as_view({'get': 'list', 'post': 'create'})),
    path('social/<int:pk>/', views.SocialLinkView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('google-callback/', auth_views.google_auth),
    path('google-login/', auth_views.google_login),
]
