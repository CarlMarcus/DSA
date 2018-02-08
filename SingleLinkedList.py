#初编辑 @ 2018.02.06
__author__ = 'CarlMarcus'
#单链表的查找和读取，最坏情况为O(n)，顺序表O(1)，
#知道元素位置的情况下，插入删除复杂度为O(n)，若知道则为O(1),顺序表一直是O(n)
#对于插入或删除数据越频繁的操作，单链表的效率优势就越是明显。顺序存储需要预分配空间，单链表按需增减

#定义节点类
class SListNode(): #支持存储数据和后继节点指针的获取和修改

    __slots__ =  ['elem', 'next'] #限定SListNode的实例属性只能是数据元素elem和后继节点next

    def __init__(self, elm, pnext = None): #elm是要存储的数据元素，pnext保存下一个节点
        self.elem = elm
        self.next = pnext

    def __str__(self): #无论是直接调用Slistnode实例还是打印Slistnode实例，都有直观的输出（可有可无）
        return str(self.elem)
    __repr__ = __str__

    def getItem(self):  #获取节点存储的数据
        return self.elem

    def getNext(self): #获取指针域存的下一个节点地址
        return self.next

    def setItem(self, newElm): #修改存储数据
        self.elem = newElm

    def setNext(self, newNext): #修改指针域地址以改变下一个节点指向
        self.next = newNext

#定义链表类
#类方法：isEmpty判断是否为空，length获取链表长度，addStart头插法，addEnd尾插法
#search检查链表是否还有某元素，index获取某元素在链表内的索引，delete删除某元素，insert在某处插入元素
class SingleLinkedList():

    def __init__(self):  #初始化的链表为空表
        self._head = None

    def isEmpty(self): #检测链表是否为空
        return self._head == None

    def length(self):
        count = 0
        current = self._head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def addStart(self, item): #在链表头部添加节点存放数据
        temp = SListNode(item)
        temp.setNext(self._head)
        self._head = temp

    def traverse(self):
        current = self._head
        print('[', end=' ') #end=''意思是以空一格结尾，默认是换行
        while current != None:
            print(current.elem, end=' ')
            current= current.getNext()
        print(']')

    def addEnd(self, item): #在链表尾部添加节点存放数据
        temp = SListNode(item)
        if self.isEmpty(): #说明当前链表是空表
            self._head = temp #直接把要添加的节点作为链表
        else:
            current = self._head
            while current.getNext() != None: #遍历整个链表，直到current指向表尾
                current = current.getNext()
            current.setNext(temp)

    def search(self, item): #检索数据元素是否在链表中
        current = self._head #从表头开始起
        foundItem = False
        while current != None and not foundItem:  #当链表还没检索完且尚未找到该数据元素时
            if current.getItem() == item:
                return True #找到了该数据元素就把标志设为true，while循环将终止
            else:
                current = current.getNext() #不断指向后继节点
        return False

    def index(self, item): #查找item数据在链表中的索引
        current = self._head #从表头开始
        count = 0 #位置计数器
        foundItem = False
        while current != None and not foundItem: #当链表没遍历完而且没找到该数据时
            if current.getItem() == item: #如果找到了该数据，便将标志设为true
                foundItem = True
                return count
            else:
                current = current.getNext() #否则，继续向后遍历
            count += 1
        raise ValueError("%s is not in linkedlist" % item)  #否则，抛出错误，数据不在链表内

    def delete(self, item): #删除链表的某个节点存放数据
        current = self._head #从表头开始
        pre = None
        while current != None: #当链表还没遍历完
            if current.getItem() != item: #如果没找到item数据的节点
                pre = current
                current = current.getNext()  #不断将current指向节点后移，并用pre指代前一节点
            else: #否则若找到了
                if not pre:  #说明该item数据的节点在表头
                    self._head = current.getNext() #只需将表头指向这个节点的后继节点就行
                else:
                    pre.setNext(current.getNext())  #否则说明该item数据的节点在链表中间，将前驱节点的后继设置成item的后继节点即可
                break #删除了即可中止循环

    def insert(self, position, item): #插入某节点，position插入位置，item要插入的数据
        if position < 0 or position > (self.length()-1):
            raise ValueError("index %s is out of linked-list" % position)
        elif position == 0:
            self.addStart(item)  #作为头节点
        elif position == (self.length()-1):
            self.addEnd(item) #作为尾节点
        else: #在中间插入
            temp = SListNode(item)
            count = 0
            pre = None
            current = self._head #从表头开始
            while count < position: #即将current和pre定位到要插入的位置，pre在pos-1处，current在pos处
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp) #pre的后继节点设为temp
            temp.setNext(current)  #temp的后继节点设为current，即完成插入


if __name__ == "__main__":
    print('----------test----------')
    sll = SingleLinkedList()
    print('------判断是否为空-------')
    if sll.isEmpty():
        print('True')
    else:
        print('False')
    print('------插入一些数据-------')
    sll.addStart(11)
    sll.addEnd(12)
    sll.addEnd(13)
    sll.addEnd(14)
    sll.addEnd(15)
    print('--------获取长度--------')
    print(sll.length())
    print('--------输出链表--------')
    sll.traverse()
    print('---判断13是否在链表内---')
    if sll.search(13):
        print('True')
    else:
        print('False')
    print('----获取13的链表索引----')
    print(sll.index(13))
    print('-------删除元素14-------')
    sll.delete(14)
    sll.traverse()
    print('---在原14的位置上插入2---')
    sll.insert(3, 2)
    sll.traverse()
    print('----------end----------')
