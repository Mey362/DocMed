from django.urls import path
from .views import SearchEcritApiView,GetComments,GetFavoris

urlpatterns = [
    path('search-ecrit/', SearchEcritApiView.as_view(), name='search-ecrit'),
    path('getComments/',GetComments.as_view(), name='getComments'),
    path('getFavoris/',GetFavoris.as_view(),name='getFavoris')
]






