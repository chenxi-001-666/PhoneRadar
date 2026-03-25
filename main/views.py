from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, CommentForm
from phoneReview.models import Brand, MobileModel, Review
from django.shortcuts import render, redirect
from django.contrib import messages # 用于显示“注册成功”的提示信息
from django.contrib.auth.models import User
from .forms import RegisterForm # 假设你在 forms.py 中定义了表单


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)  # 加密密码
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def phone_detail(request, pk):
    # 获取指定的手机机型
    phone = get_object_or_404(MobileModel, pk=pk)
    # 获取所有关联了该机型的评论
    reviews = Review.objects.filter(models_covered=phone)

    return render(request, 'main/phone_detail.html', {
        'phone': phone,
        'reviews': reviews
    })

def custom_logout(request):
    logout(request) # 执行退出逻辑
    return redirect('login') # 退出后跳到登录页

@login_required(login_url='login')
def index(request):
    # 打印要求的响应逻辑
    print("HTTP Response: 'This is the main page for Phone Radar website' has been sent.")

    brands = Brand.objects.all()
    models = MobileModel.objects.all()
    # 修复报错：现在模型里有 user 字段了，可以进行过滤
    user_reviews = Review.objects.filter(user=request.user).order_by('-pub_date')

    context = {
        'welcome_msg': "This is the main page for Phone Radar website",
        'brands': brands,
        'models': models,
        'user_reviews': user_reviews,
    }
    return render(request, 'main/index.html', context)


@login_required(login_url='login')
def add_review(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()

            # 因为模型是多对多，即使表单是单选，也要用 set() 或 add() 传入
            selected_phone = form.cleaned_data['models_covered']
            review.models_covered.set([selected_phone])

            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'main/add_review.html', {'form': form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 保存用户，但不立即提交到数据库，为了处理密码加密
            user = form.save(commit=False)
            # 设置加密密码
            user.set_password(form.cleaned_data['password'])
            user.save()

            # 发送成功消息（会在下一个页面显示）
            messages.success(request, f'账号 {user.username} 注册成功！请登录。')

            # 关键：重定向到登录页面
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form})

def fast_logout(request):
    logout(request) # 这一步会清除当前浏览器所有的登录 Session
    return redirect('login') # 退出后跳转到登录页
