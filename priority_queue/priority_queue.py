
# -------------------------------------------------------------------------
# [파이썬 기초 문법 가이드 - 이 과제를 위한 필수 요소]
# -------------------------------------------------------------------------
# 1. 변수 선언 (타입 안 써도 됨)
#    - C/Java: int x = 10;
#    - Python: x = 10
#
# 2. 리스트 (배열) 사용법 - self.data 가 리스트입니다.
#    - 길이 확인: len(self.data)
#    - 접근:      self.data[0] (첫 번째), self.data[Index]
#    - 추가:      self.data.append(값) (맨 뒤에 추가)
#    - 제거:      LastWait = self.data.pop() (맨 뒤 요소 꺼내고 리스트에서 제거)
#
# 3. 튜플 (Tuple) - (우선순위, 값) 쌍으로 데이터 저장
#    - 생성: my_tuple = (10, "Apple")
#    - 접근: priority = my_tuple[0]  (10)
#            item = my_tuple[1]      ("Apple")
#    - 비교: (1, "A") < (2, "B") 는 True입니다. (첫 번째 요소끼리 먼저 비교)
#
# 4. 조건문 (If / Else) - 중괄호 {} 대신 들여쓰기(Tab)가 중요합니다!
#    if x < 10:
#        print("작다")
#    elif x == 10:
#        print("같다")
#    else:
#        print("크다")
#
# 5. 반복문 (While)
#    while True:              # 무한 루프
#        if condition:
#            break            # 루프 탈출
#
# 6. 값 서로 바꾸기 (Swap) - 임시 변수 없이 가능!
#    a, b = b, a
#    예) self.data[0], self.data[1] = self.data[1], self.data[0]
#
# 7. 나눗셈 (정수 나눗셈)
#    - 5 / 2  => 2.5 (소수점 포함)
#    - 5 // 2 => 2   (몫만 구함 -> 부모 인덱스 구할 때 필수!)
# -------------------------------------------------------------------------

# In this file, you will develop a Min Heap to use in a priority queue.
# A priority queue is a fundamental data structure for many of the algorithms we will cover in this class,
# so it is important to get the fundamentals right.

# In a normal queue, you insert items, and they are removed in first-in, first-out order (FIFO).
# In a priority queue, you insert an arbitrary object AND a priority value for that item.
# When an item is requested, the item with the lowest priority value is returned (and removed).
# Read more: https://en.wikipedia.org/wiki/Priority_queue

# Fundamental to the Priority Queue is the "Heap" data structure.
# Heaps (especially min-heaps) allow for fast retrieval of the smallest-priority element,
# and efficient re-ordering after inserts/removals.
# Once you have a heap, implementing a Priority Queue is straightforward.

# A min-heap can be thought of as a binary tree where each node has priority <= its children.
# This means the smallest-priority element will always be at index 0.

# The tree is stored in a list. For a node at index i:
# left child index = 2*i + 1
# right child index = 2*i + 2
# parent index = (i - 1) // 2

# When you add an item, append it to the end of the list, then "bubble up"
# by swapping it with its parent while it has a smaller priority than the parent.

# When you pop the minimum item, you remove and return the item at index 0.
# Then move the last element to index 0 and "bubble down" by swapping with the smaller child
# until the heap property is restored.

# Read more: https://en.wikipedia.org/wiki/Heap_(data_structure)

# You can also watch this video, but note it starts indexing at 1 (different math).
# You may implement a 1-indexed heap if you want (leave index 0 unused), or use 0-indexing.
# Either approach works:
# https://www.youtube.com/watch?v=0wPlzMU-k00

# For this assignment, the items added to the priority queue can be any object.
# You will only compute/compare priorities (ints).
# For peek() and pop(), return (priority, item) as a tuple.

class MinHeap:
    def __init__(self):
        # We'll store elements as tuples: (priority, item)
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            return None
        priority, item = self.data[0]
        return (priority, item)

    def add(self, priority, item):
        self.data.append((priority, item))
        self._bubble_up(len(self.data) - 1)

    def pop_min(self):
        if self.is_empty():
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_val = self.data[0]

        last = self.data.pop()
        self.data[0] = last

        self._bubble_down(0)

        return min_val

    def _bubble_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2

            if self.data[idx][0] < self.data[parent_idx][0]:
                self.data[idx], self.data[parent_idx] = self.data[parent_idx], self.data[idx]
                idx = parent_idx
            else:
                break

    def _bubble_down(self, idx):
        while True:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            smallest = idx

            if left_idx < len(self.data):
                if self.data[left_idx][0] < self.data[smallest][0]:
                    smallest = left_idx

            if right_idx < len(self.data):
                if self.data[right_idx][0] < self.data[smallest][0]:
                    smallest = right_idx

            if smallest == idx:
                break

            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            idx = smallest


# Once you have a min heap, the priority queue is pretty straightforward.
# Make sure you understand what it is doing

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def is_empty(self):
        return self.heap.is_empty()

    def add(self, priority, item):
        self.heap.add(priority, item)

    def pop(self):
        return self.heap.pop_min()

    def peek(self):
        return self.heap.peek()

    def __len__(self):
        return len(self.heap)