from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **argv):
        if request.user.is_authenticated:
            return redirect('CustomerProfile')
        else:
            return view_func(request, *args, **argv)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **argv):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **argv)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorators