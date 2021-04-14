# stack을 통해 reverse 실시하기
# 스택은 후입선출 역순정렬 및 검색에 활용한다.

class Stack(object):
    def __init__(self):
        self.items = [] # 빈 리스트를 기본으로
    def isEmpty(self):
        return not bool(self.items) # self.item이 있으면 No, 아니면 Yes
    def push(self, value):
        self.items.append(value)
    def pop(self): # 반환 후에 제거
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is Empty.")
    def size(self):
        return len(self.items)
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is Empty.")

    def __repr__(self):
        return repr(self.items) # 출력이 가능한 표현

def reverse_string_with_start(str):
    s = Stack()
    revStr = ""

    for c in str:
        s.push(c)

    while not s.isEmpty():
        revStr += s.pop()

    return revStr

str = "버피는 천사다."
print(str)
print(reverse_string_with_start(str))

# 짝 찾아보기 !!
# 즉, (, {, [에 대해서 괄호가 balanced되어 있는지 아닌지의 여부
# 만약 비어있으면 True!
# 아니면, 문자열의 인덱싱 훑다가 (, {, [ 발견되면 stack에 push

possible = {"(" : ")", "{":"}", "[":"]"}

def balanced(string):
    possible = {"(" : ")", "{":"}", "[":"]", "<":">"}
    reverse_possible = dict(map(reversed, possible.items()))
    balance_stack = []
    balance = True

    if len(balance_stack) == 0:
        balance = True

    for i in string:
        if i in possible.keys():
            balance_stack.append(i)
        elif i in possible.values():
            if reverse_possible[i] == balance_stack[-1]:
                balance_stack.pop()

    if len(balance_stack) != 0:
        balance = False

    return balance

print(balanced("<we are the [warriors] and [others] are {enemies}>"))

## 스택에 용량을 제한하고
## 용량 초과시에는 새 스택을 생성한다
## 스택 집합에서 push(), pop() 모두를 사용할 수 있게 하려면?

class Node(object):
    def __init__(self, animalName = None, animalKind = None, pointer = None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0 # 몇번째 동물인가요?

class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.tailCat = None
        self.headDog = None
        self.tailDog = None
        self.animalnumber = 0

    def enqueue(self, animalName, animalKind):
        self.animalnumber += 1
        newAnimal = Node(animalName, animalKind)
        newAnimal.timestamp = self.animalnumber

        if animalKind == "cat": # cat 큐에다가 붙이기
            if not self.headCat: # 아무것도 없으면?
                self.headCat = newAnimal
            if self.tailCat: # 캣 큐의 tail이 존재하면
                self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        if animalKind == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    def dequeueDog(self):
        if self.headDog: # 헤드가 있으면
            newAnimal = self.headDog
            self.headDog = newAnimal.pointer
            return newAnimal.animalName
        else:
            print("개가 없습니다.")

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.pointer
            return newAnimal.animalName
        else:
            print("고양이가 없습니다.")

    def _print(self):
        print("---고양이:---")
        cats = self.headCat
        while cats:
            print(cats.animalName)
            cats = cats.pointer
        print("---개:---")
        dogs = self.headDog
        while dogs:
            print(dogs.animalName)
            dogs = dogs.pointer

if __name__ == "__main__":
    qs = AnimalShelter()
    qs.enqueue("밥", "cat")
    qs.enqueue("미아", "cat")
    qs.enqueue("요다", "dog")
    qs.enqueue("울프", "dog")
    qs._print()
    print("개와 고양이 하나씩 파양")
    qs.dequeueCat()
    qs.dequeueDog()
    qs._print()



