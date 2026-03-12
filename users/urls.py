from django.urls import path

from .views import *

urlpatterns=[
    path('signup/',SignUpView.as_view()),
    path('code-verify/',CodeVerifyView.as_view()),
    path('get-new-code/',GetNewCode.as_view()),
    path('user-change-info/',UserChangeInfoView.as_view())
]