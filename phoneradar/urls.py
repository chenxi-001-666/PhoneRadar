"""
URL configuration for phoneradar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views # 如果 phoneradar 是父级目录
from django.contrib.auth import views as auth_views
from main import views as main_views

admin.site.site_header = "Phone Radar Admin"
admin.site.site_title = "Phone Radar Admin"
admin.site.index_title = "Welcome to Phone Radar Admin website"

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页
    path('index/', main_views.index, name='index'),
    # 登录页：确保 template_name 指向的是包含登录表单的那个 html
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    # 退出页
    path('logout/', main_views.fast_logout, name='logout'),
    # 注册页
    path('register/', main_views.register_view, name='register'),
    # 手机详情页
    path('phone/<int:pk>/', main_views.phone_detail, name='phone_detail'),
    # 发表评论页
    path('add_review/', main_views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
