from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import AbstractUser, BaseUserManager

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)

class Category(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    image = models.ImageField(upload_to='media/images/categories', blank=True, null=True,verbose_name='Image')
    name = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(max_length=45, blank=True, null=True)
    parent_category = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = QuillField()
    status = models.CharField(max_length=45, blank=True, null=True,choices=status_choices)
    meta_title = models.CharField(max_length=45, blank=True, null=True)
    meta_description = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return str(self.name)+'  '+str(self.parent_category)
    class Meta:
        managed = False
        db_table = 'category'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Product(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')  # Field renamed because of name conflict.
    weigth = models.CharField(max_length=45, blank=True, null=True)
    units = models.CharField(max_length=45, blank=True, null=True)
    images = models.ImageField(upload_to='media/images/products', blank=True, null=True, verbose_name='Image', max_length=255)
    price = models.CharField(max_length=45, blank=True, null=True)
    sale_price = models.CharField(db_column='sale_price', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    description = QuillField()
    meta_title = models.CharField(db_column='meta_title', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    meta_description = models.CharField(db_column='meta_description', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=45, blank=True, null=True,choices=status_choices)
    in_stock = models.CharField(db_column='in_stock', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    code = models.CharField(max_length=45, blank=True, null=True)
    sku = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.category.name
    
    class Meta:
        managed = False
        db_table = 'product'


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=45)
    auth_user_id = models.IntegerField()
    date_received = models.CharField(max_length=45, blank=True, null=True)
    date_ordered = models.DateField(blank=True, null=True)
    total = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderDetails(models.Model):
    order_id = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    product_id = models.IntegerField()
    product_category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_details'

class User(AbstractUser):
    image = models.ImageField(upload_to='media/images/users', blank=True, null=True,verbose_name='Image')

    class Meta:
        managed = False
        db_table = 'user' 