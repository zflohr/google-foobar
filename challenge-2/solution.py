def solution(h: int, q: list) -> list:
    """Find the parents for a list of nodes in a perfect binary tree.

    Retrieve the values of the nodes that are parents to nodes whose
    values are given - the nodes being in a perfect binary tree of given
    height and being valued by the order wherein they are visited during
    a post-order traversal.

    Args:
        h: An integer in the interval [1, 30] that represents the height
            of the tree.
        q: A list of unique integers in the interval [1, 2^h-1] whose
            length is in the interval [1, 10000]. Each integer
            represents the value of a node in the tree.
        
    Returns:
        A list of nonzero integers in the interval [-1, 2^h-1] whose
        length is the same as that of q. Each positive integer
        represents the value of a node that is the parent of the node
        whose value is the corresponding item in q. The integer -1 is
        returned in the list for the corresponding integer in q that
        represents the value of a parentless node, i.e., the root of the
        perfect binary tree.
    """
    if (h < 1) or (h > 30):
        raise ValueError("Tree height is {prohibited_integer}, which is "
                             "outside the expected interval [1, 30]."
                             .format(prohibited_integer = h))
    if not q or len(q) > 10000:
        raise ValueError("The length of the list is {prohibited_length}, "
                             "which is outside the expected interval [1, "
                             "10000]".format(prohibited_length = len(q)))
    global tree, order, parents
    parents = []
    tree, root_x_y, order = [[None] * 2 ** i for i in range(h)], [0, 0], [1]
    post_order_traversal(root_x_y, h)
    for child in q:
        if (child < 1) or (child > 2 ** h - 1):
            raise ValueError("List contains the integer {prohibited_integer}"
                                 ", which is outside the expected interval "
                                 "[1, {upper_limit}]."
                                 .format(prohibited_integer = child,
                                         upper_limit = 2 ** h - 1))
        if tree[root_x_y[1]][root_x_y[0]] == child:
            parents.append(-1)
        else:
            binary_max_heap_search(root_x_y, child)
    return parents

def post_order_traversal(node_coord: list, height: int):
    """Perform a depth-first, post-order traversal of a tree.

    Visit each node of a binary tree in a post-order traversal, labeling
    the nodes with the order wherein they are visited in the traversal.

    Args:
        node_coord: A list of x- and y-coordinates. The y-coordinate is
            an index of a list of lists, wherein each list represents a
            specific level in a binary tree. The y-coordinate is thus
            the level of the tree. The x-coordinate is an index of a
            list in the list for which the y-coordinate is an index, and
            it represents the horizontal position of a node at the level
            specified by the y-coordinate.
        height: A positive integer that represents the height of the
            tree.
    """
    if node_coord[1] + 1 < height:
        left_child_x_y = [node_coord[0] * 2, node_coord[1] + 1]
        right_child_x_y = [node_coord[0] * 2 + 1, node_coord[1] + 1]
        post_order_traversal(left_child_x_y, height)
        post_order_traversal(right_child_x_y, height)
    tree[node_coord[1]][node_coord[0]] = order[0]
    order[0] = order[0] + 1

def binary_max_heap_search(node_coord: list, key: int):
    """Find the parent of a node in a special binary max-heap.

    In a binary max-heap whose last level is complete and whose nodes
    are sorted in each level, retrieve the value of the parent of a node
    whose value is given.

    Args:
        node_coord: A list of x- and y-coordinates. The y-coordinate is
            an index of a list of lists, wherein each list represents a
            specific level in a binary tree. The y-coordinate is thus
            the level of the tree. The x-coordinate is an index of a
            list in the list for which the y-coordinate is an index, and
            it represents the horizontal position of a node at the level
            specified by the y-coordinate.
        key: An integer that represents the value of the node whose
            parent is searched for.
    """
    left_child_x_y = [node_coord[0] * 2, node_coord[1] + 1]
    right_child_x_y = [node_coord[0] * 2 + 1, node_coord[1] + 1]
    if ((tree[left_child_x_y[1]][left_child_x_y[0]] == key) 
            or (tree[right_child_x_y[1]][right_child_x_y[0]] == key)):
        parents.append(tree[node_coord[1]][node_coord[0]])
    else:
        if tree[left_child_x_y[1]][left_child_x_y[0]] < key:
            binary_max_heap_search(right_child_x_y, key)
        else:
            binary_max_heap_search(left_child_x_y, key)
