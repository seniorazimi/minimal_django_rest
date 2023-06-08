from minimal_django_rest.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'samples', SampleModelViewSet, basename='sample')

urlpatterns = router.urls
