from django.db import models
from django.core.validators import MinValueValidator,RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)  
from django.forms import ValidationError
import datetime


class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'MyUser':
        if not email:
            raise ValidationError('Email required')

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return


class MyUser(AbstractBaseUser,PermissionsMixin):
    class Currencies(models.TextChoices):
        TENGE = 'KZT', 'Tenge'
        RUBLI = 'RUB', 'Rubli'
        EURO = 'EUR', 'Euro'
        DOLLAR = 'USD', 'Dollar'


    email =  models.EmailField(
        verbose_name='почта/логин',
        max_length=200,
        unique=True
    )
    nickname = models.CharField(
        verbose_name='ник',
        max_length=120
    )
    currency = models.CharField(
        verbose_name='валюта',
        max_length=4,
        choices=Currencies.choices,
        default=Currencies.TENGE
    )
    is_staff = models.BooleanField(
        verbose_name='staff',
        default=False
    )

    objects = MyUserManager()
    
    @property
    def balance(self) -> float:
        ...


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ActivationCode(models.Model):
    user = models.OneToOneField(
        verbose_name='пользователь',
        related_name='code',
        to=MyUser,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        verbose_name='код',
        unique=True,
        max_length=200
    )
    is_active = models.BooleanField(
        verbose_name='активный?',
        default=True
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_created=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Код',
        verbose_name_plural = 'Коды активации'



class BankCard(models.Model):
    number = models.CharField(
        verbose_name='номер',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{16}$')
        ]
    )
    cvv = models.CharField(
        verbose_name='номер',
        max_length=3,
        validators=[
            RegexValidator(regex=r'^\d{3}$')
        ]
    )
    owner = models.OneToOneField(
        verbose_name='пользователь',
        related_name='card',
        to=MyUser,
        on_delete=models.CASCADE
    )
    experation_time = models.DateField(
        verbose_name='срок действия'
    )
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Банкоская карта',
        verbose_name_plural = 'Банкоская карты'


class Transaction(models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        related_name='transactions',
        to=MyUser,
        on_delete=models.PROTECT
    )
    amount = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    datetime_created = models.DateField(
        verbose_name='дата транкзации',
        auto_now_add=True,
    )
    is_filled = models.BooleanField(
        verbose_name='пополнение?',
        default=False
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
