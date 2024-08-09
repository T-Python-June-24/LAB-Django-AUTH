from django.urls import path
from . import views
app_name = 'registration'

urlpatterns = [
    path('login/',views.login_view,name="login_view"),
    path('signup/',views.signup_view,name="signup_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('profile/<user_name>',views.profile_view,name="profile_view"),
    path('profile/edit/<user_name>',views.edit_profile,name="edit_profile"),
    
]