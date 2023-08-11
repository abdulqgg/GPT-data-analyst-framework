from django.urls import path
from .views import index, download_view, python
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', index, name='index'),
    path('download/', download_view, name='download_view'),
    path('python/', python, name='python'),
]
