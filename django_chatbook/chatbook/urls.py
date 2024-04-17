"""
Django Routes

https://www.youtube.com/watch?v=qrZGfBBlXpk
"""

__version__ = "1.0.0-a.1"

# Standard library imports. 

# Third party imports.
from django.urls import path

from . import views 

urlpatterns = [
    # Path to create,  Page to render
    path("", views.chatbook, name="chatbook")
]
