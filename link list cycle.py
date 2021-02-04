class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashd=set()
        x=head
        
        while  x:
            
                
            if x in hashd:
                return True
            hashd.add(x)
            
            x=x.next
            
        return False
            
            
                
            
        
