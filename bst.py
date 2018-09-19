class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.size = 1
    self.parent = None

  
def Select(root, k):
  if root.left.size == k - 1:
    return root
  elif root.left.size + 1 < k:
    return Select(root.right, k - root.left.size - 1)
  else:
    return Select(root.left, k)


def Rank(root, x):
  cur = x
  rank = x.left.size + 1
  while cur != root:
    parent = cur.parent
    if cur = parent.right:
      rank += parent.left.size + 1
    cur = parent
 
   return rank
      
    
  
