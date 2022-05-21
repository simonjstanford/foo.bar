def solution(h, q):
    total_nodes = (2 ** h) - 1
    root_node = create_tree(total_nodes)
    post_order = {}
    assign_post_order_traversal(root_node, post_order, 0)
    return calculate_answer(q, post_order)

def calculate_answer(q, post_order):
    answer = []
    for n in q:
        node = post_order[n]

        if node.parent:
            parent_pos = node.parent.post_order_index
            answer.append(parent_pos)
        else:
            answer.append(-1)
    
    return answer

def create_tree(total_nodes):
    root_node = Node(None, 1)
    nodes_to_process = [root_node]
    nodes = [root_node]

    for i in range(1, total_nodes):
        parent_node = nodes_to_process[0]
        node = Node(parent_node, i + 1)
        nodes_to_process.append(node)
        nodes.append(node)

        if parent_node.right is None:
            parent_node.right = node
        elif parent_node.left is None:
            parent_node.left = node
            nodes_to_process.remove(parent_node)

    return root_node

def assign_post_order_traversal(node, post_order, index):
    if node == None:
        return

    assign_post_order_traversal(node.left, post_order, index)
    assign_post_order_traversal(node.right, post_order, index)
    index = len(post_order) + 1
    post_order[index] = node
    node.post_order_index = index
    

class Node():
    left = None
    right = None
    parent = None
    index = None
    post_order_index = None

    def __init__(self, parent, index):
        self.parent = parent
        self.index = index


if __name__ == '__main__':
    print(solution(3, [1, 4, 7]))
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))