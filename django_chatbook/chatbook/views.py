"""
Django Views
"""

__version__ = "1.0.0-a.1"

# Standard library imports.

# Third party imports.
from django.shortcuts import render

# Create your views here.
def chatbook(request):
    return render(request, 'chatbot.html')
