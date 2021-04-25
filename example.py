
class Height(object):
    def __init__(self):
        self.height = 0

class NodeBT(object):
    def __init__(self, value = None, level = 1):
        self.value = value
        self.level = level
        self.left = None # 왜 default로?
        self.right = None # left, right는 있을 수도 없을수도

    def __repr__(self):
        return "{}".format(self.value)

    def _add_next_node(self, value, level_here = 2):
        new_node = NodeBT(value, level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            # 노드가 왼쪽, 오른쪽이 둘 다 있으면
            # 노드를 왼족에 추가한다
            self.left = self.left._add_next_node(value, level_here+1)
        return self # add_next_node 이후에는 트리를 반환

    def _search_for_node(self, value):
        # 전위 순회로 (pre-order) 값을 찾는다.
        # value 값을 받으면 그 값이 있는지 없는지 체크
        if self.value == value:
            return self # 그 부분을 return한다
        else:
            found = None
            if self.left:
                found = self.left._search_for_node(value)
            if self.right:
                found = found or self.right._search_for_node(value)
        return found

    def _is_leaf(self):
        # 왼쪽, 오른쪽 자식이 있나요?
        return not self.right and not self.left

    def _get_max_height(self):
        heightr, lengthl = 0, 0
        if self.right: # 만약 self.right가 있으면
            heightr = self.right._get_max_height() + 1
        if self.left:
            lengthl = self.left._get_max_height() + 1
        return max(heightr, lengthl)

    def _is_balanced(self, height = Height()): # 기본이 0
        lh = Height() #높이
        rh = Height() #높이

        if self.value is None: # self.value가 없으면
            return True

        l, r = True, True
        if self.left: # 만약 left가 존재하면
            l = self.left._is_balanced(lh)
        if self.right:
            r = self.right._is_balanced(rh)
        # Height()의 height는 두 개 중애서 한 개 max 길이를 return한다
        height.height = max(lh.height, rh.height) + 1

        if abs(lh.height - hr.height) <= 1:
            return l and r

        return False

    def _is_bst(self, left = None, right = None):
        # 이진 탐색 트리인지 확인한다 -- O(n)
        if self.value: # 만약 value가 있으면
            if left and self.value < left:
                return False
            if right and self.value > right:
                return False

            l, r = True, True
            if self.left:
                # 왼쪽은 왼쪽대로
                # 순회하면서 self.left가 먹히면, self.value 역할은 self.left로
                # 이렇게 되면 계속해서 비교한다. 언제까지? left, right가 없어질때까지
                # 중간에 한번이라도 안맞으면 나가리
                l = self.left._is_bst(left, self.value)
            if self.right:
                r = self.right._is_best(self.value, right)
            return l and r
        else:
            return True

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root: # root가 없으면
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)

    def is_leaf(self, value):
        node = self.root._search_for_node(value) # 원하는 value에 leaf?
        if node: # 있으면
            return node._is_leaf() # _is_leaf 메서드 자동 생성
        else:
            return False

    def get_node_level(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node.level
        else:
            return False

    def is_root(self, value):
        return self.root.value == value # 이 value가 root인가여?

    def get_height(self):
        return self.root._get_max_height()

    def is_balanced(self):
        return self.root._is_balanced()

    def is_bst(self):
        return self.root._is_best()

if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(1, 10):
        bt.add_node(i)

print(bt.is_root(1))