from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .ecncrypter import *
from .ecncrypter import handler

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=150)
    website_url = models.URLField(null=True, blank=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=1024, blank=False, null=False)
    note = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Website: {} User: {}'.format(self.website, self.user.username)

    def save(self, *args, **kawrgs):
        super().save( *args, **kawrgs)

        try:
            init = os.environ.get(self.user.username.upper()+'_IV')
        except KeyError:
            init = None

        en_obj = handler.encrypt_obj(
            generator('yourpasswordPIN'.encode()),
            self.user.username,
            init
        )

        self.password = handler.encrypt(en_obj, self.password.encode()).decode('cp1252')