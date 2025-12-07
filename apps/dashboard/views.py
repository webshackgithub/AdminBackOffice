from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    title = "Dashboard"

class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/analytics.html"
    title = "Analytics"

class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/settings.html"
    title = "Settings"
