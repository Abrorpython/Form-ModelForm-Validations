from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User

class MainIndex(TemplateView):
    template_name = 'main/index.html'

    # def get_context_data(self, **kwargs):
    #     kwargs['hiha'] = RegistrationForm()
    #     return super().get_context_data(**kwargs)

@require_POST
def hiha_form_post(request):
    hiha = RegistrationForm(data=request.POST)
    if hiha.is_valid():
        data = hiha.cleaned_data
        del data['password'], data['confirm']
        user = User(**data)
        # user = User(
        #     first_name=hiha.cleaned_data['first_name'],
        #     last_name=hiha.cleaned_data['last_name'],
        #     username=hiha.cleaned_data['username'],
        #     email=hiha.cleaned_data['email']
        # )
        user.set_password(hiha.cleaned_data['password'])
        user.save()
        return redirect('main:index')
    ctx = {
        'hiha': hiha
    }
    return render(request, 'main/index.html', ctx)