from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=264,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=264)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=264,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=264)
    email = forms.EmailField(max_length=264,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=264,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=264,widget=forms.TextInput(attrs={'class': 'form-control'}))

