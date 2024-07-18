
class AVLNode:
    def __init__(self, key):
        # Ініціалізація вузла AVL-дерева
        self.key = key  # Значення (ключ) вузла
        self.height = 1  # Висота вузла (початково 1, оскільки це листовий вузол)
        self.left = None  # Ліва дитина
        self.right = None  # Права дитина

    def __str__(self, level=0, prefix="Root: "):
        # Рекурсивна функція для друку дерева
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    # Функція для отримання висоти вузла
    if not node:
        return 0  # Якщо вузол порожній, його висота 0
    return node.height  # Повертаємо висоту вузла

def get_balance(node):
    # Функція для отримання балансу вузла
    if not node:
        return 0  # Якщо вузол порожній, його баланс 0
    return get_height(node.left) - get_height(node.right)  # Різниця висот лівої та правої дитини

def left_rotate(z):
    # Лівий поворот навколо вузла z
    y = z.right  # y - права дитина z
    T2 = y.left  # T2 - ліва дитина y

    # Виконуємо поворот
    y.left = z
    z.right = T2

    # Оновлюємо висоти
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Повертаємо новий корінь піддерева

def right_rotate(y):
    # Правий поворот навколо вузла y
    x = y.left  # x - ліва дитина y
    T3 = x.right  # T3 - права дитина x

    # Виконуємо поворот
    x.right = y
    y.left = T3

    # Оновлюємо висоти
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x  # Повертаємо новий корінь піддерева

def insert(root, key):
    # Вставка нового ключа у дерево
    if not root:
        # Якщо корінь дерева порожній, створюємо новий вузол
        return AVLNode(key)

    if key < root.key:
        # Якщо ключ менший за значення кореня, вставляємо у ліве піддерево
        root.left = insert(root.left, key)
    elif key > root.key:
        # Якщо ключ більший за значення кореня, вставляємо у праве піддерево
        root.right = insert(root.right, key)
    else:
        # Якщо ключ рівний значенню кореня, повертаємо корінь (дублікати не допускаються)
        return root

    # Оновлюємо висоту кореня
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримуємо баланс вузла, щоб перевірити, чи стало дерево незбалансованим
    balance = get_balance(root)

    # Лівий випадок (Left Left Case)
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            # Ліво-правий випадок (Left Right Case)
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Правий випадок (Right Right Case)
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            # Право-лівий випадок (Right Left Case)
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root  # Повертаємо (можливо оновлений) корінь

def get_min_value_node(node):
    # Функція для знаходження вузла з мінімальним значенням у дереві
    current = node
    while current.left is not None:
        # Продовжуємо рухатися до лівої дитини, поки не знайдемо найменше значення
        current = current.left
    return current  # Повертаємо вузол з мінімальним значенням

def get_max_value_node(node):
    # Функція для знаходження вузла з максимального значенням у дереві
    current = node
    while current.right is not None:
        # Продовжуємо рухатися до лівої дитини, поки не знайдемо найменше значення
        current = current.right
    return current  # Повертаємо вузол з мінімальним значенням

def get_sum_nodes_values(node):
    # Функція для обчислення суми всіх значень вузлів у дереві
    if not node:
        return 0  # Якщо вузол порожній, сума значень 0
    return node.key + get_sum_nodes_values(node.left) + get_sum_nodes_values(node.right)  # Сума значень вузлів

def delete_node(root, key):
    # Видалення вузла з деревом
    if not root:
        # Якщо дерево порожнє, повертаємо корінь
        return root

    if key < root.key:
        # Якщо ключ менший за значення кореня, видаляємо у лівому піддереві
        root.left = delete_node(root.left, key)
    elif key > root.key:
        # Якщо ключ більший за значення кореня, видаляємо у правому піддереві
        root.right = delete_node(root.right, key)
    else:
        # Вузол знайдено, видаляємо його
        if root.left is None:
            # Вузол має лише праву дитину або не має дітей
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            # Вузол має лише ліву дитину
            temp = root.left
            root = None
            return temp

        # Вузол має двох дітей, знаходимо мінімальне значення у правому піддереві
        temp = get_min_value_node(root.right)
        root.key = temp.key  # Замінюємо значення вузла на мінімальне значення
        root.right = delete_node(root.right, temp.key)  # Видаляємо мінімальне значення у правому піддереві

    if root is None:
        return root

    # Оновлюємо висоту кореня
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримуємо баланс вузла, щоб перевірити, чи стало дерево незбалансованим
    balance = get_balance(root)

    # Лівий випадок (Left Left Case)
    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            # Ліво-правий випадок (Left Right Case)
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Правий випадок (Right Right Case)
    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            # Право-лівий випадок (Right Left Case)
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root  # Повертаємо (можливо оновлений) корінь

