from django.urls import path
import accounts.views
from post.views import *
app_name = 'accounts'

urlpatterns = [
    path('signup/',accounts.views.signup, name='signup'),
    path('login/',accounts.views.login_check, name='login'),
    path('logout/',accounts.views.logout, name='logout'),
    path('follow/', accounts.views.follow, name='follow'),
]
