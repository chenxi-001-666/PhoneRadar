from django import forms
from django.contrib.auth.models import User
from phoneReview.models import Review, MobileModel


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CommentForm(forms.ModelForm):
    # 使用 ModelChoiceField 实现单选下拉框
    models_covered = forms.ModelChoiceField(
        queryset=MobileModel.objects.all(),
        label="Choose related phone",
        empty_label="-- Please choose related phone --",
        widget=forms.Select(attrs={'class': 'form-select'}) # 使用 Bootstrap 的单选样式
    )

    class Meta:
        model = Review
        fields = ['models_covered', 'title', 'content'] # 调整顺序，先选手机
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please input review title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Please input detailed review content...'}),
        }

class RegisterForm(forms.ModelForm):
    # 定义密码字段，并使用密码输入插件（隐藏输入内容）
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please Input Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    # 验证两次密码是否一致
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Two password fields must match.")
        return cleaned_data