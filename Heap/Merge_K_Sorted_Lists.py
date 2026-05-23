# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        h=[]

        for i,head in enumerate(lists):
            if head:
                heapq.heappush(h,(head.val,i,head))
        d=ListNode(0)
        t=d
        while h:
            v,i,n=heapq.heappop(h)
            t.next=n
            t=t.next
            if n.next:
                heapq.heappush(h,(n.next.val,i,n.next))
        
        return d.next
