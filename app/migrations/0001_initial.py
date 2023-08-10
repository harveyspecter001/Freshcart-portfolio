# Generated by Django 4.2.2 on 2023-06-16 02:22

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/categories', verbose_name='Image')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('slug', models.CharField(blank=True, max_length=45, null=True)),
                ('parent_category', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', django_quill.fields.QuillField()),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=45, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=45, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('auth_user_id', models.IntegerField()),
                ('date_received', models.CharField(blank=True, max_length=45, null=True)),
                ('date_ordered', models.DateField(blank=True, null=True)),
                ('total', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=45)),
                ('quantity', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.CharField(blank=True, max_length=45, null=True)),
                ('product_id', models.IntegerField()),
                ('product_category', models.IntegerField()),
            ],
            options={
                'db_table': 'order_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('weigth', models.CharField(blank=True, max_length=45, null=True)),
                ('units', models.CharField(blank=True, max_length=45, null=True)),
                ('images', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/products', verbose_name='Image')),
                ('price', models.CharField(blank=True, max_length=45, null=True)),
                ('sale_price', models.CharField(blank=True, db_column='sale_price', max_length=45, null=True)),
                ('description', django_quill.fields.QuillField()),
                ('meta_title', models.CharField(blank=True, db_column='meta_title', max_length=45, null=True)),
                ('meta_description', models.CharField(blank=True, db_column='meta_description', max_length=45, null=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=45, null=True)),
                ('in_stock', models.CharField(blank=True, db_column='in_stock', max_length=45, null=True)),
                ('code', models.CharField(blank=True, max_length=45, null=True)),
                ('sku', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
