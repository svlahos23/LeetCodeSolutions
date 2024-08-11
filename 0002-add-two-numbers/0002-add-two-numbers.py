class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summed = ListNode()
        current_sum = summed
        carry = 0
        while l1 or l2 or carry:
            temp_sum = carry
            temp_sum += l1.val if l1 else 0
            temp_sum += l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = temp_sum // 10
            current_sum.next = current_sum = ListNode(temp_sum % 10)
        return summed.next