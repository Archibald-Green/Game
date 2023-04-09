"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from main import api_views


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('index', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('register', views.RegisterView.as_view(), name = 'register'),
    path('book/<int:book_id>',views.book, name='book'),
    path('book/<int:book_id>/page/<int:page_id>',views.page, name='page'),
    path('book/<int:book_id>/page/<int:page_id>/take/<int:item_id>',views.take, name='take'),
    path('page_add',views.AddPageView.as_view(), name = 'add'),
    path('logout_user', views.logout_user, name= 'logout' ),
    path('about', views.about, name="about"),
    path('api/api/dfdasdas/', api_views.BookView.as_view()), 
    
    path('password_reset/', views.password_reset_request, name = 'password_reset' ),
    path('password_reset_done', auth_view.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('main_game', views.index),
    
    
    
    
    path ('api/users/', views.UserListView.as_view(), name ='get_users'),
    path ('api/token/', TokenObtainPairView.as_view(), name ='token_obtain_pair' ),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name ='token_refresh' ),
    path('api/token/verify', TokenVerifyView.as_view(), name = 'token_varify'),
    
    # path('sign_up/', views.sign_up, name='users-sign-up'),
    # path('profile/', views.profile, name='users-profile'),
    # path('log', auth_view.LoginView.as_view(template_name='login.html'),
    #      name='users-login'),
    # path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),
    #      name='users-logout'),
    # path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
    #      name='password_reset'),
    # path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
    #      name='password_reset_complete'),
    ]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)