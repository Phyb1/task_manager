from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'taska/index.html', {'tasks':tasks})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 
                          'taska/register.html', {'new_user':new_user})
    else:
        user_form =UserRegistrationForm()
    return render(request, 'taska/register.html', {'user_form':user_form})