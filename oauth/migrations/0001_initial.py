# Generated by Django 2.1.5 on 2019-05-03 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='OAuth类型')),
                ('app_key', models.CharField(max_length=200, verbose_name='AppKey')),
                ('app_secret', models.CharField(max_length=200, verbose_name='APPSecret')),
                ('callback_url', models.CharField(default='', max_length=200, verbose_name='回调地址')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': 'OAuth配置',
                'verbose_name_plural': 'OAuth配置',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='类型')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('avatar_url', models.CharField(blank=True, max_length=350, null=True, verbose_name='头像链接')),
                ('user_info', models.TextField(blank=True, null=True, verbose_name='OAuth获取的用户信息')),
                ('openid', models.CharField(max_length=50, verbose_name='用户openid')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'oauth用户',
                'verbose_name_plural': 'oauth用户',
                'ordering': ['-add_time'],
            },
        ),
    ]
