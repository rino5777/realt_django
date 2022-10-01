from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm
from advert.models import Ads, RealtType

from django.views.generic.edit import FormMixin

class AddAdvert(forms.ModelForm):

    # image1 = forms.ImageField()
    # image2 = forms.ImageField()
    # image3 = forms.ImageField()
    # image4 = forms.ImageField()
    # image5 = forms.ImageField()
    # image6 = forms.ImageField()

    # description = forms.CharField(widget=forms.Textarea)
    # # rubric = forms.ChoiceField()
    # realt_type = forms.ModelChoiceField(queryset= RealtType.objects.all())
    # overall_size = forms.DecimalField()
    # residential_size = forms.DecimalField()
    # kitchen_size = forms.DecimalField()
    # number_of_rooms = forms.DecimalField()
    # floor = forms.DecimalField()
    
    # number_of_building = forms.DecimalField()
    
    # building_freshness = forms.CharField()
    
    # title = forms.CharField()
 
    # price = forms.FloatField()
   
    # contacts = forms.CharField()
   
    
                             
    # is_active = forms.BooleanField()
                                   
    # author = forms.ModelChoiceField(queryset= User.objects.all())





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['image1'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})
        # self.fields['image2'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})
        # self.fields['image3'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})
        # self.fields['image4'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})
        # self.fields['image5'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})
        # self.fields['image6'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'image1'})

        self.fields['description'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'description', 'rows': 4,})
        self.fields['rubric'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'rubric', })
        self.fields['realt_type'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'realt_type', 'rows': 1,})
        self.fields['realt_type'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'realt_type', 'rows': 1,})
        self.fields['overall_size'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'overall_size', 'rows': 1,})

        self.fields['residential_size'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'residential_size', 'rows': 1,})
        self.fields['kitchen_size'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'kitchen_size', 'rows': 1,})
        self.fields['number_of_rooms'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'number_of_rooms', 'rows': 1,})
        self.fields['floor'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'floor', 'rows': 1,})
        self.fields['number_of_building'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'number_of_building', 'rows': 1,})
        self.fields['building_freshness'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'building_freshness', 'rows': 1,})
        self.fields['title'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'title', 'rows': 1,})
        self.fields['price'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'price', 'rows': 1,})
        self.fields['contacts'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'contacts', 'rows': 1,})
        

    class Meta:
        model = Ads
        fields = (  'description', 'rubric',\
                     'realt_type', 'overall_size', 'residential_size', 'kitchen_size',  'number_of_rooms',\
                      'floor', 'number_of_building', 'building_freshness', 'title', 'price', 'contacts',\
                       'author',)


    


class ChangePass(FormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'Old password!!!'})
        self.fields['new_password1'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'new password'})
        self.fields['new_password2'].widget.attrs.update({'class' : 'form-control bg-light border-0','placeholder':'confirm password'})



class ChangeUserInfoForm(UserChangeForm):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # username = forms.CharField( label='Никнейм')
    # last_name = forms.CharField( label='Никнейм')
    # email = forms.EmailField(required=True, label='Адрес электронной почты')


    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'E-mail Address' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'Username' , 'rows': 1, })
        self.fields['last_name'].widget.attrs.update({ 'class': 'form-control bg-light border-0', 'placeholder': 'last_name' , 'rows': 1, })

    class Meta:
        model = User
        fields = ('username', 'email',  'last_name' )

    

   


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



