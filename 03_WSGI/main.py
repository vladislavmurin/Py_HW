from pprint import pprint


def app(environ, start_response):
    pprint(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield b'<h1>Hello World!</h1>\n'


# Use Terminal:
# gunicorn --bind 127.0.0.1:5000 main:WSGI_gunicorn
# http GET 127.0.0.1.:8000/DOG
# http POST 127.0.0.1.:8000/DOG
