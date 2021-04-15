from django.db import models
from django.contrib.auth import get_user_model



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='User')
    github = models.CharField(max_length=1000, null=False, blank=True, verbose_name='Github')
    summary = models.TextField(null=False, blank=True, verbose_name='About')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


