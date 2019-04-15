from wsgiref.simple_server import make_server
from controller import account


dict_func = {
    '/index':account.handler_index,
    '/date':account.handler_date,
}
def runserver(environ,start_response):
    '''
    :param environ: 客户来的所有数据
    :param start_response: 封装要返回给用户的数据，如响应头状态
    :return:
    '''
    start_response('200 OK',[('Content-Type','text/html')])
    current_url = environ['PATH_INFO'] #获取当前的访问url
    func = None
    if current_url in dict_func:
        func = dict_func[current_url]
    if func:
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8')]

if __name__ == '__main__':
    http = make_server('',8000,runserver)
    print('serving http on port 8000...')
    http.serve_forever()
    # with open('view/index.html','rb') as f:
    #     data = f.read()
    #     print(data)