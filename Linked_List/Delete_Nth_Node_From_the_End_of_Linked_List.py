def deleteNthNodeFromEnd(head, n):
    if head is None:
        return head
    k = 0
    curr = head
    while curr is not None:
        curr = curr.next
        k += 1
    if n > k:
        return head
    if k - n == 0:
        temp = head
        head = head.next
        return head
    curr = head
    for i in range(1, k - n):
        curr = curr.next
    temp = curr.next
    curr.next = temp.next
    return head


def deleteNthNodeFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    for i in range(n + 1):
        if fast is None:
            return head
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    nodeDeleted = slow.next
    if nodeDeleted is not None:
        slow.next = nodeDeleted.next
    newHead = dummy.next
    return newHead


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
