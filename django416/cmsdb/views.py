from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


# def login(request):
    #Simple debugging
    # str = '''
    # <form>
    #     <input type="text"/>
    # </form>
    # '''
    # with open('templates/login.html','r',encoding='utf-8') as f:
    #     data = f.read()
    # return HttpResponse(data)
    # return render(request, 'login.html')

def login(request):
    #get the user submitted data the ways
    # print('request',request.method)
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == '123':
            return redirect('/home')    #Do need to use redirect jump(跳跃,暴涨)
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html',{'error_msg':error_msg})

USER_LIST = [
    {'username':'test','gender':'男','email':'test@qq.com'},
    {'username':'tom','gender':'男','email':'tom@qq.com'},
    {'username':'linxinru','gender':'女','email':'linxinru@qq.com'},
]

# for info in range(10):
#     temp_user = {'username':'test'+str(info),'gender':'男','email':'test'+str(info)+'@qq.com'}
#     USER_LIST.append(temp_user)
def home(request):
    '''get post the form data is added to the list'''
    if request.method == 'POST':
        user = request.POST.get('username',None)
        gender = request.POST.get('gender',None)
        email = request.POST.get('email',None)
        temp_user = {'username': user, 'gender': gender, 'email': email}
        USER_LIST.append(temp_user)
    return render(request,'home.html',{'user_list':USER_LIST})