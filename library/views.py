from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm


def home(request):
    return render(request, 'layout/index.html')


class BookLoginView(LoginView):
    template_name = 'main/login.html'


class BookLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class ChangeUserInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('library:home')
    success_message = 'Данные успешно обновлены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BookChangePasswordView(PasswordChangeView, LoginRequiredMixin, SuccessMessageMixin):
    template_name = 'main/change_password.html'
    success_url = reverse_lazy('library:home')
    success_message = 'Пароль успешно изменен'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('library:register_done')

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Вы зарегестрировались')
        return super().post(request, *args, **kwargs)


class RegisterDone(TemplateView):
    template_name = 'main/register_done.html'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('library:home')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)