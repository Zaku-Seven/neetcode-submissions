# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        '''


        boolean return, 

        hashmap values key value pair when visited and if we have to increase the value, then return true since we're revisiting a value?


        '''

        if( head == None):
            return False

        pointer1 = head 

        pointer2 = head

        while( pointer2 and pointer2.next ) :

            pointer1 = pointer1.next

            pointer2 = pointer2.next.next

          

            if(pointer1 ==  pointer2 ):
                return True
            


        return False


        