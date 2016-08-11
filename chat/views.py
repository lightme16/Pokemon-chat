from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import render
from untitled import settings
from chat.models import Chat


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/homepage/')
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
def homepage(request):
    msg_history = Chat.objects.all()
    return render(request, 'chat/base.html', {'messages': msg_history})


@login_required
def get_new_messages(request):
    messages = Chat.objects.all()
    return JsonResponse({'messages': render_to_string('chat/messages.html', {'messages': messages})})


@login_required
def save_new_msg(request):
    if request.is_ajax():
        msg = request.POST.get('new_msg', None)  # store new chat message
        chat = Chat(user=request.user, message=msg)
        chat.save()
    return HttpResponse('')  # just empty response in order to not cause an ajax error
