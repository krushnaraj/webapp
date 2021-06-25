from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_view, name='colorswatch-listview'),
    path('detail_view/<slug:name>', views.detail_view, name='colorswatch-detailview'),  
    path('detail_view/color/<slug:name>', views.detail_view_color, name='colorswatch-detailview-color'),
    path('detail_view/random/', views.detail_view_random, name='colorswatch-detailview-random'),
    path('detail_view/search/', views.detail_view_search, name = 'colorswatch-detailview-search'),
]