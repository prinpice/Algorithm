class Node:
    # 선언시 val(item포함) + next(비어있음) 를 가진 노드 생성
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    # 선언시 head가
    def __init__(self, item):
        self.head = Node(item)
    # ex) A = LinkedList(3)
    # 링크리스트 A의 head는 node(3)이다.
        # self.head = Node(3)
        # LinkedList.head.val = 3
        # LinkedList.head.next = None


    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
        # LinkedLidst.add(4)
        # cur = Node(3)
        # while Node.next 가 None이 될 때 까지 : 링크의 맨 뒤에
        # Node.next = Node(4)

    def addtoFirst(self,item):
        forenext = self.head
        self.head = Node(item)
        self.head.next = forenext
        # (9)노드를 A의 첫노드(헤드)로 삽입하려고 한다.
        # 기존 헤드를 차기 헤드의 next로 정의한다(:forenext)
        # A.head = Node(9) 로 새로운 노드(9)를 생성하는 동시에 헤드로 정의한다.
        # 바뀐 헤드의 next와 forenext를 연결한다(새 헤드+기존 노드들 연결)

    def addmid(self,pre,item):
        prev = self.head
        while prev.val is not pre:
            prev = prev.next
        if prev.next == None:
            self.add(item)
            print('맨 뒤에 삽입')
        else:
            after_next = prev.next
            prev.next = Node(item)
            prev.next.next = after_next
        # (10)노드를 (6)노드 뒤에 삽입하려고 한다.
        # 만약(6)노드가 맨 뒤라면 그냥 add 함수를 가동하고 print('맨 뒤에 넣음') 이라고 출력
        # 아니라면 노드를 돌면서 (6)노드를 찾아서 pre로 저장한다. 
        # pre 노드의 원래 next인 친구를 차기 next로 저장해놓고 
        # pre 노드를 생성된 (10)노드와 연결,  저장해놓은 차기 next를 pre노드의 다음다음으로 정의하면 끝


    # ex) 아이템기준 3 - 4 - 5 링크 된 상태
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")
        # 헤드인 (3)val인 3  = 지우려는 아이템과 같다면 (:지우려는게 3 헤드라면)
            # 이제부터 헤드는 헤드였던 3의 next (4)가 된다.
        # 아니라면 : (4를 지운다고 가정)
            # cur = node(3)
                # while 링크 끝까지 돌면서
                    # if 지우려는 4를 발견하면
                        # removeitem(4) 함수 실행
                    # 발견할때까지 다음 노드로 (cur = cur.next)

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break
    # 아이템 (4)를 지우려고 한다.
        # cur = 헤드부터 시작
        # while 링크 끝까지 돌면서
            # next의 val이 지우려는 (4)라면
                # cur의 next를 이제 nextnode 로 바꾸겠다


    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
    # 아이템을 뒤집으려고 한다. 3 - 5 - 6 상태
        # prev = None 으로 시작
        # cur = 헤드 (3)부터 시작
        # 노드 끝까지 돌면서
            # next = 현재노드의 next로 정의
            # 현재노드의 next를 prev 로 바꿈 (첫 노드, 즉 헤드의 next가 None으로 바뀌고 둘째 노드의 next가 첫 노드로 바뀜)
            # prev = 다음 순서를 위해 현재노드로 정의해 놓음
            # 다음 노드 처리로 넘어간다


    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
    # LinkedList인 A의 노드들을 출력하려고 한다.
        # cur = 헤드부터
        # 노드 끝까지 돌면서
            # print(현재노드의 val)
            # 다음노드로 이동



A = LinkedList(3)
A.add(4)
A.add(5)
A.remove(4)
A.add(6)
print(A.head.val)
print(A.head.next)
print(A.head)

A.reverse()
print(A.head.val)
print(A.head.next)
print(A.head)
A.printlist()
print('-----맨앞에 9넣기------')
A.addtoFirst(9)
A.printlist()
print('-----6뒤에 10넣기------')
A.addmid(6,10)
A.printlist()
print('-----중간넣기로 11을 맨뒤에 넣어보기(오류실험)------')
A.addmid(3,11)
A.printlist()