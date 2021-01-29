def solution(numbers, target):
    tree = [0]
    for num in numbers:
        node = []
        for tree_num in tree:
            node.append(tree_num + num)
            node.append(tree_num - num)
        tree=node
    answer = tree.count(target)
    return answer
