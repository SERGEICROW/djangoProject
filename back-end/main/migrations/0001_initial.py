# Generated by Django 3.2.7 on 2021-10-23 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_img')),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('curp', models.CharField(blank=True, max_length=18, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_img')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]