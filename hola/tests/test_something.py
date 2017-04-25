
def test_something_func():
    from ..code import do_something
    assert do_something() is not None
    
def test_somethingelse():
    from ..code import do_somethingelse
    assert do_somethingelse(2) == 4