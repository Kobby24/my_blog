from django import forms


class Login(forms.Form):
    admin_name = forms.CharField(label="Your Name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=100,label='Password')


class CreatePost(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Post Title',
        }))
    subtitle = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Subtitle',
        }))
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Enter the body here',
        }),label='Body')
    url = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Post Picture URL',
        }))
