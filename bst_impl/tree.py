class TreeNode:
    """Узел бинарного дерева поиска."""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Бинарное дерево поиска."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        """Вставка элемента в дерево."""
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node, key, value):
        """Рекурсивная вставка элемента."""
        if node is None:
            return TreeNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Если ключ уже существует, обновляем значение
            node.value = value
        
        return node
    
    def search(self, key):
        """Поиск элемента по ключу. Возвращает значение или None."""
        node = self._search(self.root, key)
        return node.value if node else None
    
    def _search(self, node, key):
        """Рекурсивный поиск узла по ключу."""
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def delete(self, key):
        """Удаление элемента по ключу."""
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        """Рекурсивное удаление узла."""
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел найден, нужно его удалить
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # У узла есть оба потомка
                # Находим минимальный элемент в правом поддереве
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.key)
        
        return node
    
    def _find_min(self, node):
        """Находит узел с минимальным ключом в поддереве."""
        while node.left is not None:
            node = node.left
        return node
    
    def height(self):
        """Вычисление высоты дерева."""
        return self._height(self.root)
    
    def _height(self, node):
        """Рекурсивное вычисление высоты поддерева."""
        if node is None:
            return -1
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_balanced(self):
        """Проверка сбалансированности дерева."""
        return self._is_balanced(self.root) != -1
    
    def _is_balanced(self, node):
        """Проверка сбалансированности поддерева.
        
        Возвращает высоту поддерева, если оно сбалансировано,
        или -1, если не сбалансировано.
        """
        if node is None:
            return 0
        
        left_height = self._is_balanced(node.left)
        if left_height == -1:
            return -1
        
        right_height = self._is_balanced(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
