from exercises import Node, inorder, is_unival_tree

def test_inorder():
    t = Node(1,
            Node(2, Node(4), Node(5)),
            Node(3, Node(6), Node(7)))
    
    assert inorder(t) == [4, 2, 5, 1, 6, 3, 7]

def test_is_unival_tree():
    t1 = Node(1,
            Node(2, Node(4), Node(5)),
            Node(3, Node(6), Node(7)))
    
    t2 = Node(1,
            Node(1, Node(1), Node(1)),
            Node(1, Node(1), Node(1)))
    
    assert not is_unival_tree(t1)
    assert is_unival_tree(t2) 

