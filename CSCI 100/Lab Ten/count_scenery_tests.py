from count_scenery import count_scenery

def test_count_scenery():
	
	# Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert count_scenery(['tree', 'tree',  'tree', 'tree', 'tree', 'mountain']) == {'mountain': 1, 'tree': 5 }
    assert count_scenery(['river', "river", "people", 'mountain', 'creek', 'lake', 'mountain', 'glacier', 'creek', 'tree', 'lake', 'tree', 'mountain']) == {'river': 2, 'people': 1, 'mountain': 3, 'creek': 2, 'lake': 2, 'glacier': 1, 'tree': 2}
    assert count_scenery(["tree", "creek", "mountain"]) == {'tree': 1, 'creek': 1, 'mountain': 1}
    
	# Write tests above this line. Do not remove.
  
test_count_scenery()