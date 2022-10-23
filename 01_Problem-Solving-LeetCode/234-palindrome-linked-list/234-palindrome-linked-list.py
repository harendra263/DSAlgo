'''
Go to the middle node and reverse the right-side linkedlist.
Then take 2 pointers one from start and another from middle and check
equality of value.
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True

        # Find Middle       
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the just previous node of middle as we need to reverse the Linkedlist also

        # Reverse LinkedList right-side of middle
        pre = slow
        cur = pre.next
        while nex := cur.next:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
        # start checking equality of values
        left =  head
        right = slow.next
        while left and right:
            if left.val != right.val: return False
            left = left.next
            right = right.next

        return True