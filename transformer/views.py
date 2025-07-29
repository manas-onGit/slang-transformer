from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Feedback
from django.contrib.auth.models import User
import os
import json
import re

# ✅ Load and normalize slang dictionary to lowercase
SLANG_DICT_PATH = os.path.join(settings.BASE_DIR, 'slang_dictionary.json')
with open(SLANG_DICT_PATH, 'r') as file:
    original_dict = json.load(file)
    slang_dict = {k.lower(): v for k, v in original_dict.items()}  # Normalize keys

def transform_slang(sentence):
    # ✅ Split input while preserving punctuation
    words = re.findall(r'\w+|\W+', sentence)
    transformed_words = []

    for word in words:
        if word.strip() == "":
            transformed_words.append(word)
            continue

        if word.isalnum():
            lower_word = word.lower()
            if lower_word in slang_dict:
                formal_word = slang_dict[lower_word]
                # Preserve original capitalization
                if word.istitle():
                    formal_word = formal_word.capitalize()
                elif word.isupper():
                    formal_word = formal_word.upper()
                transformed_words.append(formal_word)
            else:
                transformed_words.append(word)
        else:
            transformed_words.append(word)  # punctuation or symbols

    return ''.join(transformed_words)

def home(request):
    result = ""
    if request.method == "POST":
        slang_input = request.POST.get("slang_input")
        result = transform_slang(slang_input)
        print("Input:", slang_input)
        print("Output:", result)  # Debugging output

    return render(request, "home.html", {"result": result})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, email=email, message=message)
        return render(request, 'feedback.html', {'success': True})
    return render(request, 'feedback.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Auto-login after signup
        return redirect('home')

    return render(request, 'signup.html')