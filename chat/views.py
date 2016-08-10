from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from chat.forms import ChatForm
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
#    chat = get_object_or_404(Chat)
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.created_date = timezone.now()
            form.save()
            return redirect('chatroom')
    else:
        form = ChatForm()
        chat = Chat.objects.all()
        return render(request,'chat/chatroom.html', {'form': form, 'chat': chat})