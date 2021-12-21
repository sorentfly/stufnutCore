from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
    {'id': 4, 'name': 'Room 4'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'core/home.html', context)


def room(request, roomId):
    room = None
    for i in rooms:
        if i['id'] == int(roomId):
            room = i

    context = {'room': room}
    return render(request, 'core/room.html', context)
