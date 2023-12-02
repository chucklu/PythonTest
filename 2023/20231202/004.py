from collections import deque
class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None # 右子节点引用

def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res

def pre_order(root: TreeNode | None, res: list):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root.left, res)
    pre_order(root.right, res)

def in_order(root: TreeNode | None, res: list):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root.left, res)
    res.append(root.val)
    in_order(root.right, res)

def post_order(root: TreeNode | None, res: list):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root.left, res)
    post_order(root.right, res)
    res.append(root.val)

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

levelorderResult = level_order(n1)
print(levelorderResult)

preorderResult = []
pre_order(n1, preorderResult)
print(preorderResult)

inorderResult = []
in_order(n1, inorderResult)
print(inorderResult)

postorderResult = []
post_order(n1, postorderResult)
print(postorderResult)