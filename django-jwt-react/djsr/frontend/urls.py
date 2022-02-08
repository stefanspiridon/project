from django.urls import path

urlpatterns = [
    path('', index_view),  # for the empty url
    url(r'^.*/$', index_view)  # for all other urls
]