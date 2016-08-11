from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from chat.models import Chat
from untitled import settings


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/chatroom/')
            else:
                # Return a 'disabled account' error message
                return HttpResponseRedirect("Account is not active at the moment.")
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect(settings.LOGIN_URL)
    else:
        return render(request, 'chat/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def chatroom(request):
    messages = Chat.objects.all()
    return render(request, 'chat/base.html', {'messages': messages, 'user': request.user.username})

@login_required
def proccess_msg(request):
    if request.is_ajax():
        msg = request.POST.get('msg_text', None)
        if msg:
            chat = Chat(user=request.user, message=msg)
            chat.save()
            return JsonResponse({'msg': msg, 'user': chat.user.username})


