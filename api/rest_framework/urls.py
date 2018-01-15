from api.urls import *
import api.rest_framework.views as api_views

urlpatterns += [
    url(r'^posts$', api_views.PostViewSet.as_view({'get': 'list'})),
    url(r'^posts/(?P<pk>[0-9]+)$', api_views.PostViewSet.as_view({'get': 'retrieve'})),
]

