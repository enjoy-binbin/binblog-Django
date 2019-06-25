# Generated by Django 2.1.5 on 2019-06-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_setting_enable_multi_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='desc',
            field=models.TextField(blank=True, default='', verbose_name='站点描述'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='enable_multi_user',
            field=models.BooleanField(default=False, help_text='是否启用多用户博客系统, 注册用户只具有对自己文章的增删改查权限', verbose_name='是否启用多用户博客系统'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='github_repository',
            field=models.CharField(default='Django-blog', help_text='https://github.com/enjoy-binbin/Django-blog', max_length=50, verbose_name='github仓库'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='github_user',
            field=models.CharField(default='enjoy-binbin', help_text='https://github.com/enjoy-binbin', max_length=50, verbose_name='github账号'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keyword',
            field=models.TextField(blank=True, default='', verbose_name='站点关键字'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='name',
            field=models.CharField(max_length=100, verbose_name='站点名称'),
        ),
    ]
