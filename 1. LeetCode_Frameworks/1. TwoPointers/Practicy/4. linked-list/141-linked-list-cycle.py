class Solution(object):
    def hasCycle(self, head):
        slow = head                            # slow pointer starts at head
        fast = head                            # fast pointer starts at head

        while fast and fast.next:              # fast must be able to move two steps
            slow = slow.next                   # move slow by 1
            fast = fast.next.next              # move fast by 2

            if slow == fast:                   # pointers met -> cycle exists
                return True

        return False                           # fast reached the end -> no cycle