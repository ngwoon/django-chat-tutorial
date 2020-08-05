# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json, random

user_id = []

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    while True:
        cur_user_id = random.randint(0, 9999)
        if cur_user_id not in user_id:
            user_id.append(cur_user_id)
            break
            
    print(user_id)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_id': json.dumps(cur_user_id),
    })