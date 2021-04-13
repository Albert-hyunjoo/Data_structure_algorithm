class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newpointer):
        self.pointer = newpointer

class LinkedListFIFO(object):
    # fifo 연결 리스트의 경우에는 tail이 존재
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end = " ")
            node = node.pointer

    def _addfirst(self, value):
        self.length = 1
        node = Node(value) # 추가
        self.head = node # head로 인정
        self.tail = node # 이거 하나 밖에 없는 경우

    def _deletefirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")

    # 새 노드를 추가한다!
    # 테일이 있다면, 테일의 다음 노드는 새 노드
    # 테일은 새 노드를 가리킨다
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    # 새노드를 추가한다
    def addNode(self, value):
        if not self.head:
            self._addfirst(value)
        else:
            self._add(value)

    # 인덱스로 노드 찾기
    def _find(self, index):
        prev = None
        node = self.head # head에서 시작
        i = 0
        while node and i < index: # node를 순회
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deletefirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("No Value")

    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer:
            self._deletefirst()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("No node")

class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)

    def _print(self):
        for i in range(self.size):
            print("슬롯 (slot) {0}:".format(i))
            self.slots[i]._printList()
def test_hash_tables():
    H1 = HashTableLL(3) # slot 3개 생성
    for i in range(0, 20):
        H1._add(i)
    H1._print()
    print("\n항목 0, 1, 7를 삭제합니다.")
    H1._delete(0)
    H1._delete(1)
    H1._delete(7)
    H1._print()

if __name__ == "__main__":
    test_hash_tables()