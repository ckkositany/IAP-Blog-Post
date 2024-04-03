from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


#creating the users register view
def register(request):
    # validating the form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created and you can now successfully log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#creating the user's profile page
@login_required #Adds functionality to the profile view
def profile(request):
    return render(request, 'users/profile.html')





# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # Log the user in
#             return redirect('home')  # Redirect to the home page after successful login
#     else:
#         form = AuthenticationForm()

#     return render(request, 'users/login.html', {'form': form})


