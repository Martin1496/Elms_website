# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm, LoginForm, LogoutForm
#
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('accounts:home')
#     else:
#         form = RegistrationForm()
#     return render(request, 'account/register.html', {'form': form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('accounts:home')
#             else:
#                 form.add_error(None, 'Invalid username or password')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
#
# def user_logout(request):
#     if request.method == 'POST':
#         form = LogoutForm(request.POST)
#         if form.is_valid():
#             logout(request)
#             return redirect('accounts:home')
#     else:
#         form = LogoutForm()
#     return render(request, 'account/logout.html', {'form': form})
