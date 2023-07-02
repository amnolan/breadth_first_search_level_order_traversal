  # Example:
  #      3
  #    9   20
  #      15  7
  #
  # we must do Breadth First Search (BFS) to traverse this tree
  # outer loop will process while there is a value in the queue
  # basically you add the root to the queue [3]
  # pop 3 from the queue
  # add it's two children to the queue [9, 20]
  # queue is not null so examine 9
  # pop it
  # add its children to the queue (there aren't any) [20]
  # queue is not null so examine 20
  # pop 20
  # add the next numbers [15,7]
  # pop 15
  # no children to add
  # pop 7
  # no children to add
  # queue is empty, exit
def level_order_traversal(root):
  result = ""

  q = deque()
  q.append(root)

  while q:
    for i in range(len(q)):
      node = q.popleft()
      if node:
        if node.data:
          result = result + str(node.data) + " "
        q.append(node.left)
        q.append(node.right)


  return result
