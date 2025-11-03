from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Handles user registration
def register(request):
    if request.method == "POST":
        # Create a form instance with POST data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'User account created! You can login.')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Profile view (requires login)
@login_required
def profile(request):
    if request.method == "POST":
        # Create forms with current user data and uploaded files
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        # Validate and save forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # Show success message and redirect
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        # fill forms with current user data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Pass the forms to template
    context= {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)