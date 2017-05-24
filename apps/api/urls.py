from .views import NewsList
from django.conf.urls import url

urlpatterns = [
    url(r'^posts/$', NewsList.as_view({'get': 'list'})),
    url(r'^posts/(?P<site>.[A-z0-9.-]+)/$', NewsList.as_view({'get': 'retrieve'})),
]

