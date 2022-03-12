from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
TYPE_CHOICES = (
	('Open Width','Open Width'),
	('Tabular','Tabular'),
)

G_CHOICES = (
	('28','28'),
	('24','24'),
)

M_CHOICES=(
	('28A','28A'),
	('28B','28B'),
	('30A','30A'),
	('30B','30B'),
	('30C','30C'),
	('32A','32A'),
	('32B','32B'),
	('34A','34A'),)

class User_Manager(BaseUserManager):
	def _create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password=None, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)

class Users(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = User_Manager()

class work(models.Model):
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	m_name=models.CharField(max_length=3,choices=M_CHOICES,verbose_name="machine")
	date=models.DateField()
	party_name=models.CharField(max_length=100)
	types=models.CharField(max_length=10,choices=TYPE_CHOICES)
	denier=models.CharField(max_length=100)
	dia=models.CharField(max_length=100)
	guage=models.CharField(max_length=2,choices=G_CHOICES)
	gsm=models.FloatField()
	loop_length=models.FloatField()
	quantity=models.FloatField()
	wastage=models.FloatField()
	queries=models.TextField()

class status(models.Model):
	date=models.DateField()
	party_name=models.CharField(max_length=100)
	total=models.FloatField()
	today=models.FloatField()
	remaining=models.FloatField()