def minimum(u):
    while u.left:
        u = u.left
    return u

def maximum(u):
    while u.right:
        u = u.right
    return u

def search(u, k):
    if not u or k == u.key:
        return u
    if k < u.key:
        return search(u.left, k)
    else:
        return search(u.right, k)

def inorder(u):
		if u: #if the node is not null (exists)
				inorder(u.left)
				print(u.key)
				inorder(u.right)

def preorder(u):
    if u:
        print(u.key)
        preorder(u.left)
        preorder(u.right)

def postorder(u):
    if u:
        postorder(u.left)
        postorder(u.right)
        print(u.key)

def insert(bst, v):
    u = bst.root
    par = None
    while u:
        par = u
        # if v.key < u.key:
        #     u = u.left
        # else:
        #     u = u.right
        u = u.left if v.key < u.key else u.right
    v.parent = par
    if not par:
        bst.root = v
    elif v.key < par.key:
        par.left = v
    else:
        par.right = v

# Copilot code for insertions
# def insert(bst, u):
#     if not bst.root:
#         bst.root = u
#     else:
#         insert_node(bst.root, u)

# def insert_node(u, v):
#     if v.key < u.key:
#         if not u.left:
#             u.left = v
#             v.parent = u
#         else:
#             insert_node(u.left, v)
#     else:
#         if not u.right:
#             u.right = v
#             v.parent = u
#         else:
#             insert_node(u.right, v)

def delete(bst, u):
    if not u.right:
        shift_nodes(bst, u, u.left)
    elif not u.left:
        shift_nodes(bst, u, u.right)
    else:
        u_successor = minimum(u.right)
        if u_successor != u.right:
            shift_nodes(bst, u_successor, u_successor.right)
            u_successor.right = u.right
            u_successor.right.parent = u_successor
        shift_nodes(bst, u_successor, u_successor.right)
        u_successor.left = u.left
        u_successor.left.parent = u_successor

def shift_nodes(bst, u, v):
    if not u.parent:
        bst.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v:
        v.parent = u.parent
