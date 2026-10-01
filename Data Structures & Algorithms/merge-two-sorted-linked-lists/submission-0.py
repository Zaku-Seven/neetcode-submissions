class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        currentNode = ListNode(0)
        nodeTail = currentNode

        
        while list1 != None or list2 != None:
            
            if list1 == None:
                nodeTail.next = ListNode(list2.val)
                list2 = list2.next
                nodeTail = nodeTail.next
            
            elif list2 == None:
                nodeTail.next = ListNode(list1.val)
                list1 = list1.next
                nodeTail = nodeTail.next
                
            else:
                
                if list1.val < list2.val:
                    nodeTail.next = ListNode(list1.val)
                    list1 = list1.next
                    nodeTail = nodeTail.next

                else:
                    nodeTail.next = ListNode(list2.val)
                    list2 = list2.next
                    nodeTail = nodeTail.next
    
        return currentNode.next