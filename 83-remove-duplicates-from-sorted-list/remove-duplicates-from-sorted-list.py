# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        dummy = ListNode(0, head)
        prev = dummy

        while prev and prev.next:
            
            if prev.next.val in nums:
                prev.next = prev.next.next
            else:
                nums.append(prev.next.val)
                prev = prev.next
        
        return dummy.next