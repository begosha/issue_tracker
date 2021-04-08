from django.contrib.auth.models import User
from django import forms



class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput, strip=False)
    email  = forms.EmailField(required=True, widget=forms.EmailInput)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
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
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']