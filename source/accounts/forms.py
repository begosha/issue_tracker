from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class MyUserCreationForm(UserCreationForm):

    email  = forms.EmailField(required=True, widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")
        if last_name == '' and first_name == '':
            raise forms.ValidationError('Fill Out First Name Field!')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_email(self):
          data = self.cleaned_data['email']
          if User.objects.filter(email=data).count() > 0:
              raise forms.ValidationError("We have a user with this user email-id")
          return data


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']