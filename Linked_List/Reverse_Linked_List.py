def reverseList(head):
    curr = head
    prev = None
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

def reverseList(head):
    if head is None or head.next is None:
        return head
    rest = reverseList(head.next)
    head.next.next = head
    head.next = None
    return rest


def reverseList(head):
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
    head = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
    return head
