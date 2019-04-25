from django.conf.urls import url
from django.urls import include, path

from . import views



users = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


users_urls = [
    url(r'',users , name='trusted-person'),
]



urlpatterns = [
    path('', include(users_urls)),
    # url(r'users/', views.User.as_view(), name='account-create'),
]
