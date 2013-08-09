def foobar():
    raise AttributeError('foobar')

def bar():
    raise bar.AttributeError('bar')
