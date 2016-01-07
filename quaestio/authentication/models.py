from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

MAX_LEN = 40


class AccountManager(BaseUserManager):
    # FIXME: Cleanup
    def create_user(self, email, username, password=None, **kwargs):
        # TODO: Add email validation with legitimate emails (no mailinator, etc.)
        if not email:
            raise ValueError('Valid email required')
        # TODO: Only allow certain characters in the username (english alphabet, digits and underscores/dashes maybe)
        if not username:
            raise ValueError('Username required')

        acct = self.model(
            email=self.normalize_email(email), username=username
        )
        acct.set_password(password)
        acct.save()
        return acct

    def create_superuser(self, email, username, password, **kwargs):
        acct = self.create_user(email, username, password, **kwargs)
        acct.is_admin = True
        acct.save()
        return acct


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=MAX_LEN, unique=True)

    first = models.CharField(max_length=MAX_LEN, blank=True)
    last = models.CharField(max_length=MAX_LEN, blank=True)
    battle_cry = models.CharField(max_length=100+MAX_LEN, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    # Django's User requires a username for logging in - we're using email in this case
    USERNAME_FIELD = 'email'
    # Why not add 'email' to the below as well?
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first, self.last])

    def get_short_name(self):
        return self.first
