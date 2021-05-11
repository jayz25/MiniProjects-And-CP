#Explaination : https://iq.opengenus.org/detect-and-remove-loop-in-linked-list/
#Code source  : https://www.codesdope.com/blog/article/detect-and-remove-loop-in-a-linked-list/



class ListNode:
    	def __init__(self, x):
    	self.val = x
    	self.next = None

def removeLoop(head: ListNode):
	# Initialize ptr1 and ptr2 to head node.
	ptr1 = head
	ptr2 = head
	# Boolean to check if a loop exists in the given Linked List.
	flag = False
	# Traverse the Linked List.
	while ptr2 != None and ptr2.next != None:
    	# Move ptr1 forward by one node.
    	ptr1 = ptr1.next
    	# Move ptr2 forward by two nodes.
    	ptr2 = ptr2.next.next
    	# Check if ptr1 and ptr2 meet at some node, then there is a loop in the Linked List and So make flag true and break.
    	if ptr1 == ptr2:
        	flag = True
        	break
	# When there is a loop in the Linked List.
	if flag:
    	# Assign head to ptr1.
    	ptr1 = head
    	# Loop until next of ptr1 and ptr2 are not equal.
    	while ptr1.next != ptr2.next:
        	ptr1 = ptr1.next
        	ptr2 = ptr2.next
    	# Make next of ptr2 i.e last node of Linked List None.
    	ptr2.next = None
	return head

if __name__ == '__main__':
	head = ListNode(2)
	head.next = l1 = ListNode(8)
	l1.next = l2 = ListNode(3)
	l2.next = l3 = ListNode(5)
	l3.next = l4 = ListNode(10)
	l4.next = l2
	# 2->8->3->5->10--
	#   	^    	|
	#   	|    	|
	#   	---------
	removeLoop(head)
	while head != None:
    	print(f'{head.val}->',end="")
    	head = head.next;
	print("NULL")