def handler_index():
    with open('view/index.html','rb') as f:
        data = f.read()
        data = data.replace(b'index',b'88888')
        return [data,]

def handler_date():
    return ['<h1>Hello,date!</h1>'.encode('utf-8')]