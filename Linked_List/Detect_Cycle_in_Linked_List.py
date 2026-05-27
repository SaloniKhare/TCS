def detectLoop(head):
    st = set()
    while head is not None:
        if head in st:
            return True
        st.add(head)
        head = head.next
    return False


def detectLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
