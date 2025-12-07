from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(LoginRequiredMixin, TemplateView):
    template_name = "users/user_list.html"
    title = "Users"
