from django.urls import path

from forecast import views

urlpatterns = [
    path("locations/<str:city>/", views.forecast_view),
]
