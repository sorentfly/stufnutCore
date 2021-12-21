from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
    {'id': 4, 'name': 'Room 4'},
]


def home(request):
    return render(request, 'core/home.html', {'rooms': rooms})
