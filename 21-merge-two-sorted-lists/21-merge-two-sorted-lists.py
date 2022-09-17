# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        # avoid edge case of the inital empty list
        dummy = ListNode()
        tail = dummy
        
        # while the lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # what if one list is empty and the other is not empty
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
        
                