from django.shortcuts import render

# Create your views here.
def index(request):
    """Home Page for Sign In."""
    return render(request, 'visitors/index.html')