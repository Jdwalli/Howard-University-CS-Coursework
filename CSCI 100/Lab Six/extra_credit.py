def two_sum(numbers, target):
  Solutions = []
  for first_index, first_value in enumerate(numbers):
    lookup_value = target - first_value
    for second_index, second_value in enumerate(numbers):
      if second_value == lookup_value:
        if first_index != second_index:
          Solutions.append(first_index)
          Solutions.append(second_index)

  return list(set(Solutions))