class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        n=0
        while temp is not None:
            temp=temp.next
            n+=1
        t=1
        temp=head.next
        pre=head
        if n==0:
            return None
        if n==1:
            return None
        while temp is not None:
            if t==n//2:
                pre.next=temp.next
                temp=temp.next
                break
            else:
                t+=1
                pre=temp
                temp=temp.next
        return head