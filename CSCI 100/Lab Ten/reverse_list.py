from reverse_list import reverse_list

def test_reverse_list():
	# Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert reverse_list([1, 2, 3, 4, 5, 6, 7]) == None
    assert reverse_list([9, 8, 7, 6, 5]) == None
    assert reverse_list([1]) == None

	# Write tests above this line. Do not remove.
test_reverse_list()