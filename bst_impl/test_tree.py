from tree import BinarySearchTree


def test_basic_operations():
    """Тест 1: Проверка базовых операций BST."""
    bst = BinarySearchTree()
    
    # Проверка пустого дерева
    assert bst.height() == -1, "Высота пустого дерева должна быть -1"
    assert bst.is_balanced() is True, "Пустое дерево должно быть сбалансировано"
    assert bst.search(5) is None, "Поиск в пустом дереве должен вернуть None"
    
    # Вставка элементов
    bst.insert(50, "root")
    bst.insert(30, "left")
    bst.insert(70, "right")
    bst.insert(20, "left-left")
    bst.insert(40, "left-right")
    bst.insert(60, "right-left")
    bst.insert(80, "right-right")
    
    # Проверка поиска
    assert bst.search(50) == "root", "Должен найти корневой элемент"
    assert bst.search(30) == "left", "Должен найти левый элемент"
    assert bst.search(70) == "right", "Должен найти правый элемент"
    assert bst.search(20) == "left-left", "Должен найти элемент в левом поддереве"
    assert bst.search(100) is None, "Поиск несуществующего элемента должен вернуть None"
    
    # Проверка высоты
    assert bst.height() == 2, "Высота дерева должна быть 2"
    
    # Проверка сбалансированности
    assert bst.is_balanced() is True, "Сбалансированное дерево должно быть сбалансировано"
    
    # Проверка обновления значения
    bst.insert(50, "updated-root")
    assert bst.search(50) == "updated-root", "Значение должно обновиться"
    
    # Удаление листа
    bst.delete(20)
    assert bst.search(20) is None, "Удаленный элемент не должен находиться"
    assert bst.search(30) == "left", "Родительский элемент должен остаться"
    
    # Удаление узла с одним потомком
    bst.delete(30)
    assert bst.search(30) is None, "Удаленный элемент не должен находиться"
    assert bst.search(40) == "left-right", "Потомок должен остаться"
    
    # Удаление узла с двумя потомками
    bst.delete(70)
    assert bst.search(70) is None, "Удаленный элемент не должен находиться"
    assert bst.search(80) == "right-right", "Правый потомок должен остаться"
    assert bst.search(60) == "right-left", "Левый потомок должен остаться"
    
    # Проверка высоты после удалений
    assert bst.height() >= 0, "Высота не должна быть отрицательной"
    
    print("Тест 1 пройден: все базовые операции работают корректно")


def test_complex_scenarios():
    """Тест 2: Проверка сложных сценариев и граничных случаев."""
    bst = BinarySearchTree()
    
    # Создание несбалансированного дерева (вырожденное дерево)
    bst.insert(10, "a")
    bst.insert(20, "b")
    bst.insert(30, "c")
    bst.insert(40, "d")
    bst.insert(50, "e")
    
    # Проверка высоты несбалансированного дерева
    assert bst.height() == 4, "Высота вырожденного дерева должна быть 4"
    assert bst.is_balanced() is False, "Вырожденное дерево не должно быть сбалансировано"
    
    # Проверка всех элементов
    assert bst.search(10) == "a"
    assert bst.search(20) == "b"
    assert bst.search(30) == "c"
    assert bst.search(40) == "d"
    assert bst.search(50) == "e"
    
    # Создание сбалансированного дерева
    bst2 = BinarySearchTree()
    bst2.insert(25, "root")
    bst2.insert(15, "left")
    bst2.insert(35, "right")
    bst2.insert(10, "left-left")
    bst2.insert(20, "left-right")
    bst2.insert(30, "right-left")
    bst2.insert(40, "right-right")
    
    assert bst2.height() == 2, "Высота сбалансированного дерева должна быть 2"
    assert bst2.is_balanced() is True, "Дерево должно быть сбалансировано"
    
    # Удаление корня с двумя потомками
    bst2.delete(25)
    assert bst2.search(25) is None, "Корень должен быть удален"
    assert bst2.search(30) == "right-left", "Элементы должны остаться"
    assert bst2.is_balanced() is True, "Дерево должно остаться сбалансированным"
    
    # Удаление всех элементов
    bst2.delete(15)
    bst2.delete(35)
    bst2.delete(10)
    bst2.delete(20)
    bst2.delete(30)
    bst2.delete(40)
    
    assert bst2.height() == -1, "Высота пустого дерева должна быть -1"
    assert bst2.is_balanced() is True, "Пустое дерево должно быть сбалансировано"
    assert bst2.search(25) is None, "Поиск в пустом дереве должен вернуть None"
    
    # Проверка удаления несуществующего элемента
    bst2.delete(999)  # Не должно вызвать ошибку
    assert bst2.height() == -1, "Высота не должна измениться"
    
    # Проверка работы с одним элементом
    bst3 = BinarySearchTree()
    bst3.insert(42, "single")
    assert bst3.height() == 0, "Высота дерева с одним элементом должна быть 0"
    assert bst3.is_balanced() is True, "Дерево с одним элементом должно быть сбалансировано"
    assert bst3.search(42) == "single", "Должен найти единственный элемент"
    
    bst3.delete(42)
    assert bst3.height() == -1, "После удаления дерево должно стать пустым"
    assert bst3.is_balanced() is True, "Пустое дерево должно быть сбалансировано"
    
    print("Тест 2 пройден: все сложные сценарии работают корректно")


if __name__ == "__main__":
    test_basic_operations()
    test_complex_scenarios()
    print("\nВсе тесты успешно пройдены!")

