from django.urls import path, include
from . import views

app_name="pizza"

urlpatterns = [
    path('', views.Main.as_view(),name='main'),
    path('menu/', views.MenuView.as_view(),name='menu'),
    path('order/', views.OrderView.as_view(),name='order'),
    path('contact/', views.ContactView.as_view(),name='contact'),
    path('rest/', views.RestaurantsView.as_view(),name='restaurants'),
    path('search/', views.SearchMenuView.as_view(),name='search-menu'),
    path('test/',views.TestView.as_view(),name="test"),
    path('image/',views.ImageView.as_view(),name='image'),
]