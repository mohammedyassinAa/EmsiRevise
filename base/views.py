from django.shortcuts import render
# Render the lobby page 
def lobby(request):
    return render(request , 'base/lobby.html')
# Render the room page 
def room(request):
    return render(request , 'base/room.html')