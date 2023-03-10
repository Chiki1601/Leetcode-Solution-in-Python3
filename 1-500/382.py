# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.mapping = dict()
        self._fill_dict()

    def getRandom(self) -> int:
        l = list(self.mapping.keys())
        return self.mapping[random.choice(l)].val

    def _fill_dict(self):
        ptr = self.head
        i = 0
        while ptr:
            self.mapping[i] = ptr
            ptr = ptr.next
            i += 1
        


