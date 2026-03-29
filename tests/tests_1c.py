
import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
	assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
	assert max_subarray_sum([3,4,1,6,1,-5,6,-2,-9,2]) == 16
	assert max_subarray_sum([1]) == 1
	assert max_subarray_sum([-1]) == 0
	assert max_subarray_sum([1,"mit",3]) == 4
	assert max_subarray_sum([-2,-3,-1]) == 0
	assert max_subarray_sum([]) == 0

if __name__ == "__main__":
	pytest.main()