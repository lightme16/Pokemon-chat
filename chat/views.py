from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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
                return HttpResponseRedirect('/get_messages/')
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
def get_messages(request):
    messages = Chat.objects.all()
    return render(request, 'chat/base.html', {'messages': messages})

def get_messagesJSON(request):
    messages = Chat.objects.all()
    return JsonResponse({'messages': render_to_string('chat/messages.html', {'messages': messages})})

@login_required
def process_msg(request):
    if request.is_ajax():
        msg = request.POST.get('new_msg', None)
        if msg:
            chat = Chat(user=request.user, message=msg)
            chat.save()

            messages = Chat.objects.all()
            rendered = render_to_string('chat/messages.html', {'messages': messages})
            return JsonResponse({'messages': rendered})


