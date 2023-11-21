from django.urls import path
from .views import index, download_view, python, explain
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', index, name='index'),
    path('download/', download_view, name='download_view'),
    path('python/', python, name='python'),
    path('explain/', explain, name='explain')
]
