from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
    
def academic(request):
    return render(request, 'academic.html', {})

def profesional(request):
    return render(request, 'profesional.html', {})

def personal(request):
    return render(request, 'personal.html', {})

def predictive(request):
    return render(request, 'predictive.html', {})

def algorithm(request):
    return render(request, 'algorithm.html', {})

def optimization(request):
    return render(request, 'optimization.html', {})

def machine(request):
    return render(request, 'machine.html', {})

def spatial(request):
    return render(request, 'spatial.html', {})

def travel(request):
    return render(request, 'travel.html', {})

def places(request):
    return render(request, 'places.html', {})

def opinion(request):
    return render(request, 'opinion.html', {})

def album(request):
    return render(request,  'album.html', {})

def contact(request):
    return render(request,  'contact.html', {})