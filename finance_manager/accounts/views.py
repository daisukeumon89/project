from .forms import CustomUserCreationForm, CustomUserChangeForm, ExpenseForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = CustomUserChangeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })
@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expenses")
    else:
        form = ExpenseForm()
    return render(request, "accounts/add_expense.html", {"form": form})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "accounts/expense_list.html", {"expenses": expenses})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
