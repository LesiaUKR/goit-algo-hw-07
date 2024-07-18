from tasks_1_3 import get_max_value_node, get_min_value_node, get_sum_nodes_values, insert


if __name__ == '__main__':
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    print("Вставка ключів у AVL-дерево:")
    for key in keys:
        root = insert(root, key)
   
    print("AVL-Дерево:")
    print(root)

    print("Мінімальне значення у дереві:", get_min_value_node(root).key)

    print("Максимальне значення у дереві:", get_max_value_node(root).key)

    print("Сума всіх значень у дереві:", get_sum_nodes_values(root))

