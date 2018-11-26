# unit testing for function month_length in problem 2
import month_length as ml

def test_month_length():
    assert ml.month_length('January') == 31, "unexpected days for January"
    assert ml.month_length('February') == 28, "unexpected days for February, not leap year"
    assert ml.month_length('February', leap_year = True) == 29, "unexpected days for February, leap year"
    assert ml.month_length('March') == 31, "unexpected days for March"
    assert ml.month_length('April') == 30, "unexpected days for April"
    assert ml.month_length('May') == 31, "unexpected days for May"
    assert ml.month_length('June') == 30, "unexpected days for June"
    assert ml.month_length('July') == 31, "unexpected days for July"
    assert ml.month_length('August') == 31, "unexpected days for August"
    assert ml.month_length('September') == 30, "unexpected days for September"
    assert ml.month_length('October') == 31, "unexpected days for October"
    assert ml.month_length('November') == 30, "unexpected days for November"
    assert ml.month_length('December') == 31, "unexpected days for December"
    assert ml.month_length('foo') == None, "This is not a month"
