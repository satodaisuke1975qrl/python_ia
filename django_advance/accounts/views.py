from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# 関数ビューを、views.pyでログイン必須にする
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import AuthenticationForm


class AccountCreateView(generic.CreateView):
    Model = CustomUser
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')


class Login(LoginView):
    template_name = 'accounts/login.html'
    # 元々のログインビューは以下のような記述があって
    # ログインの入力欄を作成している
    # authentication_form = Authentication


class Logout(LogoutView):
    # next_page = '/accounts/login/'
    # ログアウト後に、移動するページ
    next_page = reverse_lazy('accounts:login')


# LoginRequiredMixinは継承の1番目に書く
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/home.html'


# @をつける、デコレーターと呼ばれる機能
# @login_required
# def top(request):
#   render ...


