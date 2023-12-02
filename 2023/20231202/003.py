#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 or l2

    return dummy.next

n0 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(4)

n3 = ListNode(1)
n4 = ListNode(3)
n5 = ListNode(4)

n0.next = n1
n1.next = n2

n3.next = n4
n4.next = n5

merged_list = merge_two_lists(n0, n3)
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
print()

merged_list = merge_two_lists(None, None)
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
print()

n6 = ListNode(0)
merged_list = merge_two_lists(None, n6)
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next