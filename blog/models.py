from django.db import models
import time

# Create your models here.


class user(models.Model ):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField('用户名', max_length=50)
    #usercode = models.IntegerField(auto_created=True)
    role = models.CharField('用户对应的角色', max_length=50, default='user')
    passwd = models.CharField('密码', max_length=50)
    is_delete = models.BooleanField('是否删除', default=False)  #假删除

    def __str__(self):
        delete = ''
        if(self.is_delete == True):
            delete = '(无效)'
        return self.username + delete 

class Article(models.Model ):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('标题', max_length=50)
    change_time = models.DateTimeField('最后修改时间', auto_now=True)
    author = models.CharField('作者', max_length=50)
    content = models.TextField('文章内容', max_length=20000)
    img_url = models.CharField('图片URL', max_length=100)
    is_delete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        delete = ''
        if(self.is_delete == True):
            delete = '(无效)'
        return str(self.id ) + ' / ' + self.title + delete + '  --->  ' + str(self.change_time)

class contact(models.Model):
    id = models.AutoField(auto_created = True, primary_key=True, serialize=False,verbose_name='ID')
    visitors_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)
    msgtime = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        delete = ''
        if(self.is_delete == True):
            delete = '(无效)'
            timearray = time.strptime(self.msgtime, '%m/%d-%H:%M')
        return visitors_name + delete + ' -> ' +  str(timearray)

class error():
    msg='无数据'
