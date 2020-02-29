
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from libs.models import *
from libs.forms import *
from joins.models import *
from joins.forms import *
from client.models import *
from client.forms import *

# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def accounts_profile(request):

    dictionary = t_dict.objects.all()
    url = t_url.objects.raw("""SELECT u.id, u.icon, u.url, u.header, u.category
                                FROM libs_t_url u
                            """)

    sub_url = t_sub_url.objects.raw("""SELECT su.id, su.rootid_id, su.title
                                       FROM libs_t_sub_url su
                                    """)
    dash = CompanyProfile.objects.filter(rootid=request.user.id)
    


    
    form = CompanyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/')

    context = {
       "dictionary" : dictionary,
       "url" : url,
       "sub_url" : sub_url,
       "form":form,
       "dash" : dash,

    }

    template = "dashboard/accounts_profile.html"

    return render(request, template, context)

def highchart(request):

    context = {

    }

    template = "dashboard/highchart.html"

    return render(request, template, context)

def graphs(request):

    context = {

    }

    template = "dashboard/graphs.html"

    return render(request, template, context)

def graphs_b(request):

    context = {

    }

    template = "dashboard/graphs2.html"

    return render(request, template, context)
