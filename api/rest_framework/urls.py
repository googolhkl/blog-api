from api.urls import *
import api.rest_framework.views as api_views

urlpatterns += [
    url(r'^posts', api_views.PostViewSet.as_view({'get': 'list'})),
]

