from django.urls import path
from . import views


app_name='login'


urlpatterns= [
    path('', views.sign_in , name='sign_in'),
    path('create/account' , views.sign_up , name='sign_up'),
    path('account/update/<user_id>/' , views.update_user , name='update_user'),
    path('logout/' , views.logout_user , name='logout_user')
]