class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None # 右子节点引用

def preorder_traversal(root):
    """二叉树先序遍历函数 NLR"""
    result = []
    if root is None:
        return result
    node = root
    while(node is not None):
        result.append(node.val)
        if(node.left is None and node.right is None):
            break
        if(node.left is not None):
            node = node.left
        else:
            node = node.right

    return result

# 初始化二叉树
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
n6 = TreeNode(val=6)
# 构建节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.right = n4
n3.left = n5
n3.right = n6

preorderResult = preorder_traversal(n1)
print(preorderResult)