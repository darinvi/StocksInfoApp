from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import generic as views
from stocks.stocks_app.models import Profile
from django import forms
from django.urls import reverse_lazy

UserModel = get_user_model()

class UserRegisterForm(auth_forms.UserCreationForm):    
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
    )
    accept = forms.BooleanField()

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user = user,  
        )
        if commit:
            profile.save()
        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields =('email',)

class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

class UserReisterView(views.CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLogoutVeiw(auth_views.LogoutView):
    pass