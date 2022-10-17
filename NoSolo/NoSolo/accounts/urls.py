from django.urls import path

from NoSolo.accounts.views import LoginUserView
from NoSolo.main.views import login_view

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
]