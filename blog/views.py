from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect     #302重定向方法
from django.shortcuts import HttpResponsePermanentRedirect      #301重定向
#from django.core.urlresolvers import reverse    #重定向传参
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page


import time
from . import models
import pdb

# Create your views here.

def index(request):
    timenow = time.strftime('[%y-%m-%d/%H:%M:%S]', time.localtime())
    username = request.session.get('username')
    userinfo = models.user()
    if(username != None):
        try:
            userinfo = models.user.objects.filter(username=username)[0]
        except Exception as e:
            print('---- ' + str(e))
            userinfo = None
    else:
        userinfo = None
    articles = models.Article.objects.all()
    print('---- arc.len [' + str(len(articles)) + ' ]')
    print('---- user.len [' + str(userinfo) + ']')
    return render(request, 'blog/index.html', {'time': timenow , 'userinfo': userinfo, 'articles': articles })

@cache_page(60 * 5) #缓存5分钟
def login(request):
    '''
    用户登录
    '''
    #pdb.set_trace()
    if(request.method == 'POST'):
        username = request.POST['username'].strip()
        pwd = request.POST['pwd'].strip()
        if(username == '' or username == None or pwd == '' or pwd == None):
            return JsonResponse({ 'msg': '信息不完整！', 'error': 'true'})
        elif(models.user.objects.filter(username=username)):
            #存在此账号
            if(pwd == models.user.objects.filter(username=username).values()[0]['passwd']):
                #密码正确
                request.session['username'] = username
                request.session.set_expiry(300)
                return JsonResponse({'error': 'false', 'redirect': 'true', 'url': '/index' })
            else:
                #密码错误
                return JsonResponse({'msg': '密码错误', 'error': 'true' })
        else:
            return JsonResponse({'msg': '用户不存在',  'error': 'true' })
    else:
        return render(request, 'blog/login.html')

def signup(request):
    '''
    用户注册
    '''
    if(request.method == 'GET'):
        #首次请求
        return render(request, 'blog/signup.html')
    elif(request.method == 'POST'):
        #pdb.set_trace()
        #提交注册信息
        username = request.POST['username']
        pwd = request.POST['pwd']
        pwd_repeat = request.POST['pwd_repeat']
        if(username == None or pwd == None or username == '' or pwd == '' or pwd_repeat == '' or pwd != pwd_repeat):
            return JsonResponse({ 'msg': '信息不完整!', 'code': '3' })
        else:
            #前端提交的表单完整
            try:
                models.user.objects.create(username = username, passwd=pwd)
                return JsonResponse({ 'msg': '注册成功！', 'code': '0', 'redirect': 'true', 'url': 'login' })
            except Exception as e:
                print('---- 插入数据库失败 ')
                print('--- ' + str(e))
                return JsonResponse({ 'msg': '注册失败！', 'code': ' 2'})

def article(request, id = 0):
    '''
    获取文章详情页
    '''
    if(request.session.get('userinfo') == None):
        return render(request, 'blog/error.html', { 'error': {'type':'Permission denied', 'msg': '访问此页面请先登录！' }})
    if(request.method == 'GET'):
        return render(request, 'blog/articledetail.html')
    else:
        try:
            article = models.Article.objects.get(pk=(int)(id))
            return JsonResponse({'success': 'True', 'msg': '获取文章详情成功！', 'data': {'article' : article }})
        except Exception as e:
            print('--- ' + str(e))
            article = models.Article()
            return JsonResponse({ 'success': 'False', 'msg': "读取数据库失败！" })

def articles(request):
    '''
    获取整个文章列表
    '''
    if(request.session.get('userinfo') == None):
        return render(request, 'blog/error.html', { 'error': {'type':'Permission denied', 'msg': '访问此页面请先登录！' }})
    try:
        print('---- 正要获取list')
        articles = models.Article.objects.all()
        print('---- 以获取文章列表 --' + str(len(articles)))
        return render(request, 'blog/articlelist.html', { 'articles': articles })
    except Exception as e:
        print('---- 获取article列表失败  ---')
        print('--- ' + str(e))
        articles = []
        return render(request, 'blog/articlelist.html', { 'articles': articles })

def reporterror(request, errorinfo):
    pass








def gettime(request):
    timenow = time.strftime('[%y-%m-%d/%H:%M:%S]', time.localtime())
    return JsonResponse({ 'timenow': timenow })
def articledemo(request):
    return render(request, 'blog/article.html')

def test(request):
    return HttpResponse({ '\\test msg/', '| test_msg2 |' })

def load(request):
    return render(request, '/blog/load.html')
