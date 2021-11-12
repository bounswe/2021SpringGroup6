from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, identifier, email, password, **extra_fields):
        """
        Create and save a user with the given identifer, email, and password.
        """
        if not identifier:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        identifier = GlobalUserModel.normalize_username(identifier)
        user = self.model(identifier=identifier, email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, identifier, email, password, **extra_fields):
        return self._create_user(identifier, email, password, **extra_fields)

    def create_superuser(self, identifier, email, password, **extra_fields):
        return self._create_user(identifier, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    identifier = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=300,blank=True)
    familyName = models.CharField(max_length=30,blank=True)
    birthDate = models.DateField(blank=True, null=True)
    gender = models.SmallIntegerField(blank=True, null=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['email']

    def add_sport_interest(self, sport_name, skill_level):
        SportSkillLevel.objects.create(user_id=self.user_id,sport_id=sport_name, skill_level=skill_level)
    
    def get_sport_skills(self):
        skills = SportSkillLevel.objects.filter(user=self.user_id)
        return [{"@type":"PropertyValue","name": skill.sport_id, "value":skill.skill_level} for skill in skills]


class SportSkillLevel(models.Model):
    class Meta:
        db_table = 'sport_skill_level'
        unique_together = (('user', 'sport'),)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    skill_level = models.SmallIntegerField()


class Block(models.Model):
    class Meta:
        db_table = 'block'

    blocker = models.ForeignKey('User', related_name='+', on_delete=models.CASCADE)
    blocked = models.ForeignKey('User', related_name='+', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

class Follow(models.Model):
    class Meta:
        db_table = 'follow'

    follower = models.ForeignKey('User', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('User', related_name='follower', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)