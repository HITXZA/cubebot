"""mofang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
#from django.conf.urls import re_path
from django.conf.urls import url
import json
import ast
from django.http import JsonResponse

from cube.python_code.tools import getResults

def mofang(req):
    return render(req,"mofang.html")
def initState(request):
    print("start")
    if request.method=='POST':
        #rev=request.get_json()['city']
        #result=selcity(rev)
        with open('initState.json', 'r') as f:
            result = json.load(f)
        print(result)
        return HttpResponse(json.dump(result), content_type="application/json")
def solve(request):
    print("solve")
    if request.method == 'POST':
        rev = request.POST
        print(rev)
        print("computing...")
        data = rev['state']
        data = data[1:len(data) - 1]
        data = data.split(",")
        print(data)

        state = []
        for i in data:
            state.append(int(i))
        result = getResults(state)
        print("complete!")
        
        return JsonResponse(result)

urlpatterns= [
    #path('admin/', admin.site.urls),
    url(r'^$',mofang),
   # url('mofang/',mofang),
    url(r'^solve$',solve)
   # url('initState/', initState)
]
