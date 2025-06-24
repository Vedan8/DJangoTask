from django.urls import path
from .views import PublicHelloView, ProtectedDataView, RegisterView

urlpatterns = [
    path("public/", PublicHelloView.as_view()),
    path("protected/", ProtectedDataView.as_view()),
    path("register/", RegisterView.as_view()),
]
