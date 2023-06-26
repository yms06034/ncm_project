from django.urls import path
from n_c_home import views as v

app_name='app'

urlpatterns = [
    path("", v.index, name='index'),
    path("result", v.naverCafeInfo, name='naverCafeInfo')
]