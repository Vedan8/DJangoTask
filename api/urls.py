from django.urls import path
from .views import PublicHelloView, ProtectedDataView

urlpatterns = [
    path("public/", PublicHelloView.as_view()),
    path("protected/", ProtectedDataView.as_view()),
]
