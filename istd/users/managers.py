from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save

from ._models_proxy import UserProfile


# UserManager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, username=None, is_confirm=True, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, is_confirm=is_confirm, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        profile = UserProfile.objects.create(user=user)
        profile.save()
        return user

    def create_user(self, email, password=None, username=None, is_confirm=False, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        if username is not None:
            is_confirm = True
        return self._create_user(email, password, username, is_confirm=is_confirm, **extra_fields)

    # post_save(create_user, )

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(email, password, **extra_fields)
