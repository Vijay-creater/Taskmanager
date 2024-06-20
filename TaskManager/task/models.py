from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **kwargs):
        if not user_name:
            raise ValueError({'message':'User Name Requied'})
        user = self.model(user_name=user_name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, password=None, **kwargs):
        user = self.create_user(
            user_name=user_name,
            password=password,
            is_super_admin=True,
            is_staff=True,
            is_active=True,
            **kwargs
        )
        return user


class User(AbstractBaseUser):
    user_name = models.CharField(unique=True,max_length=100)
    email = models.EmailField(null=True,blank=True)
    # personal Detail 
    display_name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    brith_date = models.DateField(null=True)
    gender = models.IntegerField(default=1)
    qualification = models.CharField(max_length=1000, null=True, blank=True)
    current_adress = models.TextField()
    permanent_adress = models.TextField()
    employee_image = models.ImageField(upload_to='employeeimage/',null=True,blank=True)
    blood_group = models.CharField(max_length=100,null=True,blank=True)
    # employee status
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "self",  # Use "self" to create a recursive relationship
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_by_user",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_super_admin

    def has_module_perms(self, app_label):
        return self.is_super_admin

    def __str__(self):
        return self.user_name
    
class TaskStatus(models.Model):
    Status_name = models.CharField(max_length = 100) 


class Task(models.Model):
    title = models.CharField(max_length = 1000,unique=True)
    description = models.TextField()
    due_date = models.DateField()
    status = models.ForeignKey('TaskStatus',default=1,on_delete=models.RESTRICT,related_name='taskstatus')


