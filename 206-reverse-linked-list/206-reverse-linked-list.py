# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head
        
        while current:
            # copy to make sure I don't break the links in head
            next = current.next
            
            # reversing the link
            current.next = previous
            previous = current 
            
            # making sure I keep going through every element in the link list
            current = next
            
        return previous 
            
            
        
        