from django.urls import path
from .views import DashboardHomeView, AnalyticsView, SettingsView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardHomeView.as_view(), name="home"),
    path("analytics/", AnalyticsView.as_view(), name="analytics"),
    path("settings/", SettingsView.as_view(), name="settings"),
]
