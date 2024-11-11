from django.shortcuts import render

# Existing home view
def home(request):
    return render(request, 'mywebpage/home.html')

# New resume view
def resume(request):
    return render(request, 'mywebpage/resume.html')
