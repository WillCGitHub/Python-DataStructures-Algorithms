import random
class Node():
	def __init__(self,val,left,right):
		self.val = val
		self.left = left
		self.right = right
class BTree():
	def __init__(self,root):
		self.root = root

	def DFS_preorder(self):
		ans = []
		root = self.root
		stack = []
		stack.append(root)


		while (stack):
			curr = stack.pop(0)
			ans.append(curr.val)
			if curr.left is not None:
				stack.append(curr.left)
			if curr.right is not None:
				stack.append(curr.right)

		return ans

	def DFS_inorder(self):
		ans = []
		root = self.root
		stack = []
		
		if root is None:
			return ans

		curr = root
		while((len(stack) > 0) or (curr is not None) ):
			if curr is not None:
				stack.append(curr)
				curr = curr.left
			else:
				out = stack.pop()
				ans.append(out.val)
				curr = out.right

		return ans

	def DFS_postorder(self):
		ans = []
		root = self.root
		stack = []
		stack.append(root)
		if root is None:
			return ans

		while (stack):
			curr = stack.pop(0)
			if curr.left is not None:
				stack.insert(0,curr.left)
			if curr.right is not None:
				stack.insert(0,curr.right)

			ans.append(curr.val)

		ans = [a for a in reversed(ans)]

		return ans

			

	def DFS_recursive(self):
		root = self.root
		ans = []
		self._DFS_recursive(root,ans)
		return ans

	def _DFS_recursive(self,node,ans):

		
		if node.left is not None:
			self._DFS_recursive(node.left,ans)
		
		if node.right is not None:
			self._DFS_recursive(node.right,ans)
		ans.append(node.val)
		return ans




def buildTree(nodes):
	root = Node(0,None,None)
	bt = BTree(root)

	root.left = Node(1,None,None)
	root.right = Node(2,None,None)
	root.left.left = Node(3,None,None)
	root.left.right = Node(4,None,None)
	root.right.left = Node(5,None,None)
	root.right.right = Node(6,None,None)

	return bt




if __name__ == "__main__":
	t = buildTree([1,2,3,4,5,6,7,8,9])

	print(t.DFS_recursive())

	print(t.DFS_preorder())
	print(t.DFS_inorder())
	print(t.DFS_postorder())

