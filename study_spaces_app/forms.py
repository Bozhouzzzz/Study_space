from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from study_spaces_app.models import UserProfile, Post, PICTURE_NAME_MAX_LENGTH, DESCRIPTION_MAX_LENGTH, ADDRESS_MAX_LENGTH


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('username','email','password')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already taken')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Password is required')
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')

        if not confirm_password:
            raise ValidationError('Confirm password is required')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match')

        return confirm_password
      
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userType','userType','user_profile')
        labels = {'user_profile': 'Profile Picture'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postName', 'picture', 'description', 'address', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    postName = forms.CharField(
        label='Post Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    picture = forms.ImageField(
        label='Picture',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            self.instance.pictureName = picture.name
        return picture
