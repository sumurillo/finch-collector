from django.shortcuts import render

#usually Model is used
finches = [
  {'name': 'Lolo', 'breed': 'cardinal', 'description': 'red and crazy', 'age': 3},
  {'name': 'Sachi', 'breed': 'canary', 'description': 'sings pretty songs', 'age': 2},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })