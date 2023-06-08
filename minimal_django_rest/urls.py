from django.urls import path
from minimal_django_rest.views import *
from rest_framework.routers import DefaultRouter
from knox.views import *
from .auth_views import *

router = DefaultRouter()
router.register(r'samples', SampleModelViewSet, basename='sample')

urlpatterns = router.urls
urlpatterns += [
    path('auth/create/', CreateUserView.as_view()),
    path('auth/signin/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view(), name="knox-logout"),
    path('auth/logout/all/', LogoutAllView.as_view(), name="knox-logout-all"),
]
