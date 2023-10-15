# Python3 program to detect loop in a linked list

''' Link list node '''


class Node:

	def __init__(self):
		self.data = 0
		self.next = None
		self.flag = 0


def push(head_ref, new_data):
	''' allocate node '''
	new_node = Node()

	''' put in the data '''
	new_node.data = new_data

	new_node.flag = 0

	''' link the old list of the new node '''
	new_node.next = (head_ref)

	''' move the head to point to the new node '''
	(head_ref) = new_node
	return head_ref

# Returns true if there is a loop in linked list
# else returns false.


def detectLoop(h):

	while (h != None):
		# If this node is already traverse
		# it means there is a cycle
		# (Because you we encountering the
		# node for the second time).
		if (h.flag == 1):
			return True

		# If we are seeing the node for
		# the first time, mark its flag as 1
		h.flag = 1
		h = h.next
	return False


''' Driver program to test above function'''
if __name__ == '__main__':

	''' Start with the empty list '''
	head = None

	head = push(head, 20)
	head = push(head, 4)
	head = push(head, 15)
	head = push(head, 10)

	''' Create a loop for testing '''
	head.next.next.next.next = head

	if (detectLoop(head)):
		print("Loop Found")
	else:
		print("No Loop")

# This code is contributed by rutvik_56
