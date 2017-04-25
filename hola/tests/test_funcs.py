
def test_func_a():
    from ..func_a import function_a
    assert function_a() > 10000
    assert abs(function_a(0.0001)-0.5) < 0.00001
    
def test_func_b():
	from ..func_b import function_b
	assert function_b(-1) == -2

def test_somethingelse():
    from ..code import do_somethingelse
    assert do_somethingelse(2) == 4
