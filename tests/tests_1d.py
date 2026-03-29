
import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
	assert two_sum([2, 7, 11, 15], 9) == [0, 1]
	assert two_sum([3, 2, 4], 6) == [1, 2]
	assert two_sum([3, 3], 6) == [0, 1]
	assert two_sum([1, 2, 3], 7) == []
	assert two_sum([], 5) == []
	assert two_sum(None, 5) == []
	assert two_sum([1, "mit", 3], 4) == [0, 2]

if __name__ == "__main__":
	pytest.main()