from django.shortcuts import render

def home(request):
    response = render(request, 'invitation/home.html')
    print("TEMPLATE RESPONSE:", response.status_code)
    return response
def details(request):
    return render(request, 'invitation/details.html')
def venue(request):
    return render(request, 'invitation/venue.html')