from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    # path("", views.),
    path("login/",views.login_view),
    path("logout/",views.logout_view),
    path("signup/",views.signup_view)
    
]