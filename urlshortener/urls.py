'''
Urls for shortener app urlshortener/urls.py
'''

from django.urls import path

# Import the home view
from .views import home_view, redirect_url_view, show_url_info, redirect_home, delete_url

appname = "shortener"

urlpatterns = [
    # Home view
    path('', home_view, name='home'),
    path('return', redirect_home, name="return"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('info/<str:shortened_part>', show_url_info, name='info'),
    path('delete/<str:shortened_part>', delete_url, name='delete'),
]