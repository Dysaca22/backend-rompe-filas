from django.urls import include, path


urlpatterns = [
    path('api/', include('register.urls')),
    path('api/', include('turn.urls')),
    path('api/', include('qualification.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]