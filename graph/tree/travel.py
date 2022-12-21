from collections import deque

pro = []
poo = []
ino = []
lvo = []


def inorder(tree, node):
    inorder(tree, tree[node][0])
    ino.append(node)
    inorder(tree, tree[node][1])


def postorder(tree, node):
    postorder(tree, tree[node][0])
    postorder(tree, tree[node][1])
    poo.append(node)


def preorder(tree, node):
    pro.append(node)
    preorder(tree, tree[node][0])
    preorder(tree, tree[node][1])


def lvorder(tree, root):
    q = deque([root])
    while q:
        node = q.popleft()
        lvo.append(node)
        q.append(tree[node][0])
        q.append(tree[node][1])
