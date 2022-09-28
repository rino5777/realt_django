from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm


from django.views.generic.edit import FormMixin


class ChangePass(FormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'Old password!!!'})
        self.fields['new_password1'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'new password'})
        self.fields['new_password2'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'confirm password'})



class ChangeUserInfoForm(UserChangeForm):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    username = forms.CharField( label='Никнейм')
    last_name = forms.CharField( label='Никнейм')
    email = forms.EmailField(required=True, label='Адрес электронной почты')


    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'E-mail Address' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Username' , 'rows': 1, })
        self.fields['last_name'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'last_name' , 'rows': 1, })


   


class LoginForm(AuthenticationForm): 
    
    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Password' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Username' , 'rows': 1, })
       



class RegisterUserForm(forms.ModelForm):
    username = forms.CharField( label='Никнейм')
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput, help_text='Введите тот же самый пароль еще раз для проверки')

    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Password' , 'rows': 1, })
        self.fields['password2'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Confirm Password' , 'rows': 1, })
        self.fields['email'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'E-mail Address' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Username' , 'rows': 1, })
        self.fields['name'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'user' , 'rows': 1, })



    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
              'Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = False
        if commit:
            user.save()
        
        return user

    class Meta:
        model = User
        fields = ('name','username', 'email', 'password1', 'password2', )



