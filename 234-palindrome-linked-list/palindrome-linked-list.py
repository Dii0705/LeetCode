# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # Find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the 2nd half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check if palindrome
        left, right = head, prev # prev should be at the end now
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True