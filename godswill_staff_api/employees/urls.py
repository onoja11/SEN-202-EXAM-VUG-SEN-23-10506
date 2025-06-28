from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import StaffBaseViewSet, ManagerViewSet, InternViewSet

router=DefaultRouter()
router.register(r'staff', StaffBaseViewSet, basename='staffbase')
router.register(r'manager', ManagerViewSet, basename='manager')
router.register(r'intern', InternViewSet, basename='intern')

urlpatterns = [
    path("", include(router.urls))
]


