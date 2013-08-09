class Foo(Bar,str,  baz.Baz):
    """Fooing"""
    s = 'a string'

    def __init__(self):
        super().__init__()

class Foo:
    """Fooing"""
    s = 'a string'    
    pass

class Foo():
    """Fooing"""
    s = 'a string'    
    pass
