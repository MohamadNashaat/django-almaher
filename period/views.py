from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Max
from django.db.models import Q
import xlwt
import tempfile
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
# Import models
from period.models import Time


# Create your views here.

@login_required(login_url='login')
def period(request):
    period = Time.objects.all()
    context = {'period': period,
                }
    return render(request, 'period/period.html', context)

@login_required(login_url='login')
def add_period(request):
    if request.method == 'POST':
        nperiod = request.POST['period_name']
        Time.objects.create(time_name = nperiod)
        messages.success(request, 'تم الاضافة بنجاح')
        return HttpResponseRedirect(reverse('period'))
    context = {}
    return render(request, 'period/add_period.html', context)

@login_required(login_url='login')
def del_period(request, pk):
    get_period = Time.objects.get(pk=pk)
    get_period.delete()
    return redirect('period')