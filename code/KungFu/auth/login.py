from kungfu import index
from kungfu.server.frame import result

@page('login.html')
def login(arg):
    user_name = arg.POST.get('username', '')
    password = arg.POST.get('password', '')

    if user_name == 'yun' and password == '123':
        return {'rel' : 0}
    else:
        return {'rel' : -1}

def check_code(arg):
    code = arg.POST.get('code', '')
    wode = heihei
    return result()
