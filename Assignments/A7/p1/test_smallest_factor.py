#unit testing for smallest_factor in problem 1
import smallest_factor as sf

def test_smallest_factor():
    assert sf.smallest_factor(1) == None, "failed on corner case 1"
    assert sf.smallest_factor(2) == 2, "failed on corner case 2"
    assert sf.smallest_factor(4) == 2, "failed on corner case 4"
    assert sf.smallest_factor(103) == 103, "failed on prime number"
    assert sf.smallest_factor(142) == 2, "failed on even integer"
    assert sf.smallest_factor(25) == 5, "failed on odd integer that is not a prime number"
