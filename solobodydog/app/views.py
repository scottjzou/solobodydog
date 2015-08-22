from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import LoginHistory, UserProfile


def index(request):
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def users(request):
    return HttpResponse('\n'.join(user.name+' '+user.password for user in User.objects.all()))


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/app')

    if request.method == 'POST':
        try:
            username = request.POST['login']
            password = request.POST['password']
        except KeyError:
            template = loader.get_template('app/login.html')
            context = RequestContext(request, {})
            return HttpResponse(template.render(context))
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                lh = LoginHistory()
                lh.user = user
                lh.save()
                if user.is_active:
                    auth_login(request, user)
                    next = request.GET.get('next', '/app')
                    return HttpResponseRedirect(next) if next else HttpResponse('success lol')
                else:
                    return HttpResponse(' user is inactive')

            return HttpResponse('fail')



    template = loader.get_template('app/login.html')
    context = RequestContext(request, {'next': request.GET.get('next', '')})
    return HttpResponse(template.render(context))

@login_required(login_url='/app/login/', redirect_field_name='next')
def my_profile(request):
    template = loader.get_template('app/profile.html')
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    finally:
        context = RequestContext(request, {'profile': profile})

    return HttpResponse(template.render(context))


def todo(request):
    template = loader.get_template('app/todo.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/app')


def signup(request):
    if request.user.is_authenticated():
        return HttpResponse('you are already signed in')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except KeyError:
            return render_to_response('app/signup.html')
        else:
            if User.objects.filter(email=email):
               return HttpResponse('email has already been used')
            User.objects.create_user(username, email, password).save()
            next = request.GET.get('next', '/app')
            return HttpResponseRedirect(next) if next else HttpResponse('success lol')
    else:
        template = loader.get_template('app/signup.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))




