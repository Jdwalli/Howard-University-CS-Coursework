from Queue import QueueLL

# Procedure
# Add each item to the queue
# If the size of the queue is greater than k, popleft the first item
# Take the average of the queue with each iteration
# make sure to round to fit decimal places

def moving_average(input_list, k):
  queue = QueueLL()
  solution = []
  for element in input_list:
    queue.enqueue(element)
    if len(queue) > k:
      queue.dequeue()
    average = float(sum(queue.queue()) / len(queue))
    solution.append(round(average, 2))
  return solution


if __name__ == '__main__':
  assert moving_average(input_list = [1, 2, 3, 4, 5, 6, 7], k = 3) == [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]

