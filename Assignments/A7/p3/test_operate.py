#unit testing for function operate

import pytest
import operate as op

def test_operate():
    with pytest.raises(TypeError) as excinfo:
        op.operate(1, 1, 7)
    assert excinfo.value.args[0] == "oper must be a string"
    assert op.operate(3, 5, '+') == 8, "unexpected value using addition"
    assert op.operate(7, 8, '-') == -1, "unexpected value using subtraction"
    assert op.operate(3, 0, '*') == 0, "unexpected value using mutiplication"
    assert op.operate(5, 2, '/') == 2.5, "unexpected value using division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(2, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        op.operate(1, 4, '^')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

