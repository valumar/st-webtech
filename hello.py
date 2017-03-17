def app(environ, start_response):
    d = (environ['QUERY_STRING'].split('&'))
    data = bytes('\n'.join(d), 'ascii')
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ('Content-Length', str(len(data)))
    ])
    return iter([data])

