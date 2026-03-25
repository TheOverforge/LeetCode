# Фреймворк Two Pointers

## 1. Где это находится в общей картине

LeetCode удобно изучать не как набор случайных задач, а как систему:

- **11 фреймворков**
- **30 основных паттернов**
- первый фреймворк: **Two Pointers**

Главная идея: не зубрить отдельные решения, а учиться **распознавать форму задачи** и быстро выбирать подходящий метод.

---

## 2. Что такое Two Pointers

**Two Pointers** — это подход, где используются **два указателя / два индекса**, которые двигаются по:

- одному массиву;
- одной строке;
- связанному списку;
- двум разным последовательностям.

Цель подхода:

- убрать лишние вложенные циклы;
- сократить сложность;
- решить задачу за **O(n)** или **O(n + m)** вместо **O(n²)**.

---

## 3. Когда этот фреймворк обычно встречается

Two Pointers часто появляется, когда:

- есть **одна или две последовательности**;
- нужно искать пары, пересечения, совпадения;
- нужно делать **in-place modification**;
- надо двигаться **с двух концов**;
- массив уже **отсортирован**, либо сортировка помогает.

---

## 4. Главная схема распознавания

    Two Pointers
    │
    ├── Есть больше одной последовательности?
    │   └── Да → один указатель на каждую
    │
    └── Последовательность одна
        ├── Нужно менять её in-place?
        │   └── Да → fast & slow
        │
        └── Иначе → left & right

### Вопросы, которые надо задавать себе

1. У меня **две последовательности**?
2. У меня **одна последовательность**, и её надо менять **на месте**?
3. У меня **одна последовательность**, и ответ ищется **с двух концов**?

---

## 5. Основные виды Two Pointers

### 5.1. One pointer for each sequence

#### Идея

Если есть **две последовательности**, часто ставится **по одному указателю на каждую**.

#### Когда использовать

- пересечение двух отсортированных массивов;
- слияние двух отсортированных массивов;
- сравнение двух строк;
- синхронный проход по двум структурам.

#### Общая логика

- если левый элемент меньше — двигаем левый указатель;
- если правый элемент меньше — двигаем правый указатель;
- если равны — обрабатываем совпадение и двигаем оба.

#### Пример

    from typing import List

    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = 0
        p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1

        return result

#### Сложность

- **Time:** `O(n + m)`
- **Memory:** `O(k)` для результата

#### Green flags

- две последовательности;
- данные отсортированы или могут быть отсортированы;
- нужно найти `intersection`, `merge`, `common elements`.

---

### 5.2. Fast and Slow

#### Идея

Если последовательность **одна**, и её нужно **менять in-place**, часто используется пара:

- `fast` — читает все элементы;
- `slow` — показывает, куда ставить следующий нужный элемент.

#### Когда использовать

- Move Zeroes
- Remove Duplicates from Sorted Array
- Remove Element
- фильтрация массива без нового массива

#### Интуиция

`fast` сканирует массив.  
Когда найден полезный элемент, он переносится в позицию `slow`, после чего `slow` двигается дальше.

#### Пример

    from typing import List

    def move_zeroes(nums: List[int]) -> List[int]:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return nums

#### Сложность

- **Time:** `O(n)`
- **Memory:** `O(1)`

#### Green flags

- в условии есть `in-place`;
- нельзя использовать дополнительный массив;
- нужно удалить, сгруппировать или перенести элементы;
- нужно сохранить относительный порядок.

---

### 5.3. Left / Right pointers

#### Идея

Если последовательность **одна**, можно поставить:

- `left` слева,
- `right` справа,

и постепенно **сужать диапазон**.

#### Когда использовать

- Two Sum II
- Valid Palindrome
- Container With Most Water
- поиск пары в отсортированном массиве

#### Общая логика

- если текущая пара подходит — ответ найден;
- если сумма слишком маленькая — двигаем `left`;
- если сумма слишком большая — двигаем `right`.

#### Пример

    from typing import List

    def two_sum(nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left, right]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]

#### Сложность

- **Time:** `O(n)`
- **Memory:** `O(1)`

#### Green flags

- массив отсортирован;
- нужен ответ по паре элементов;
- диапазон можно сужать с двух концов;
- задача связана с палиндромом или крайними элементами.

---

## 6. Arrays vs Linked Lists

Two Pointers используется не только в массивах и строках, но и в **linked lists**.

### В массивах и строках

Удобно работать, потому что:

- есть индексы;
- легко делать `left`, `right`, `fast`, `slow`;
- можно быстро сравнивать значения.

### В linked lists

Two Pointers часто нужен для:

- поиска середины списка;
- поиска цикла;
- поиска `k`-го элемента с конца;
- разбиения списка.

---

## 7. Что нужно знать до изучения Two Pointers

Полезная база:

- arrays
- linked lists
- selection sort

### Почему это важно

**Arrays**
- индексация;
- swap;
- границы массива;
- проход по элементам.

**Linked Lists**
- ссылки `next`;
- движение по узлам;
- понимание, как не потерять связи.

**Selection Sort**
- работа с индексами;
- поиск минимума;
- понимание движения границ.

---

## 8. Признаки, что перед тобой задача на Two Pointers

### Частые слова в условии

- `sorted array`
- `in-place`
- `remove duplicates`
- `move zeroes`
- `find pair`
- `palindrome`
- `intersection`
- `merge`

### На что реагировать

- `without extra space`
- `preserve relative order`
- `two arrays`
- `two strings`
- `leftmost / rightmost`

---

## 9. Частые ошибки

1. Неправильные границы цикла  
   Например, `left <= right` вместо `left < right`.

2. Двигается не тот указатель  
   Сравнение сделано правильно, а pointer сдвинут неправильно.

3. Потеря порядка элементов  
   Особенно в задачах вроде Move Zeroes.

4. Игнорирование sorted property  
   Некоторые решения работают только на отсортированных данных.

5. Путаница между `fast/slow` и `left/right`  
   Это разные подпаттерны.

---

## 10. Быстрые шаблоны

### Один указатель на каждую последовательность

    p1 = 0
    p2 = 0

    while p1 < len(a) and p2 < len(b):
        if a[p1] < b[p2]:
            p1 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            # обработка совпадения
            p1 += 1
            p2 += 1

### Fast and Slow

    slow = 0

    for fast in range(len(nums)):
        if condition(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1

### Left / Right

    left = 0
    right = len(nums) - 1

    while left < right:
        if condition_met:
            return answer
        elif need_move_left:
            left += 1
        else:
            right -= 1

---

## 11. Итог

### Two Pointers — это семейство подходов

1. **One pointer for each sequence**
   - две последовательности
   - merge / intersection / compare

2. **Fast and Slow**
   - одна последовательность
   - in-place modification

3. **Left / Right**
   - одна последовательность
   - движение с двух концов

### Главная мысль

Надо распознавать не название задачи, а её **структуру**:

- две последовательности → pointer for each
- одна последовательность + in-place → fast & slow
- одна последовательность + два края → left & right

---

## 12. Что решать для закрепления

### Fast and Slow

- Move Zeroes
- Remove Duplicates from Sorted Array
- Remove Element

### One pointer for each

- Intersection of Two Sorted Arrays
- Merge Sorted Array
- Compare Strings with Backspaces

### Left / Right

- Two Sum II
- Valid Palindrome
- Container With Most Water