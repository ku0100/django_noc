from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    View function for the NOC Homepage
    """

    # Render the HTML template 'index.html' with the data in the context variable (nothing yet included)
    return render(request, 'homepage/index.html', context={})