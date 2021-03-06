# Generated by Django 2.0.1 on 2018-01-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180130_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=50, verbose_name='用户对应的角色'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='change_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=20000, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_url',
            field=models.CharField(max_length=100, verbose_name='图片URL'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
    ]
