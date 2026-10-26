# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        '''

        reverse a linkedlist 

        store a previous value? set the .next to the prev value 

        2 3 null

        3.next = 2 

        but how can we keep track of all the previous? 

        recursion? 

        if recursive how

        pass through the next and if we 

        '''



        if( head == None or head.next == None):
            return head


        new_head = self.reverseList(head.next)

        head.next.next = head

        head.next = None

        return new_head

            



        


        