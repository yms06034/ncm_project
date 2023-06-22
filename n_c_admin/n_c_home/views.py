from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django. contrib import auth
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text, intersect

import pandas as pd
import numpy as np
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def naverCafeInfo(request):
    if request.method == 'POST':
        naver_id = request.POST['naverid']
        naver_pw = request.POST['naverpw']
        nick_name = request.POST['nickname']
        cafe_name = request.POST['cafename']
        cafe_B_name = request.POST['cafeBname']
        keyword = request.POST['keyword']
        comments = request.POST['comments']
    
    context = {'naver_id':naver_id,
                'naver_pw':naver_pw,
                'nick_name':nick_name,
                'cafe_name':cafe_name,
                'cafe_B_name':cafe_B_name,
                'keyword':keyword,
                'comments':comments}
    print(context)
    return render(request, 'index.html', context=context)