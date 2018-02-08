#stack是个LIFO(last in first out先进后出结构)，可以用list模拟
#pop推出栈顶元素，peek获取栈顶元素但不删除，push推入栈顶元素，isEmpty检查栈是否空，size获取栈长
#----进栈出栈，复杂度都是O(1)----
#典型应用 十进制转二进制、递归
class stack():
    #初始化栈为空列表
    def __init__(self):
        self.items = []
    #如果没这个函数，那么print(stackA())将是打印栈的内存地址
    def __str__(self):
        return '%s' % self.items 
    __repr__ = __str__
    #isEmpty检测栈是否为空栈
    def isEmpty(self):
        return self.items == []
    #push将元素推入栈顶
    def push(self, item):
        self.items.append(item)
    #size获取栈长
    def size(self):
        return len(self.items)
    #clear清空栈，del是列表内置操作，[:]表示遍历整个列表
    def clear(self):
        del self.items[:]
    #peek获取栈顶元素，并不删除
    def peek(self):
        if self.isEmpty():
            print('The stack is empty.')
            return None
        else:
            return self.items[len(self.items)-1] #len是list内置方法
    #pop推出栈顶元素
    def pop(self):
        if self.isEmpty():
            print('The stack is empty.')
            return None
        else:
            self.items.pop() #这是list的内置方法，获得list最后一位，之后list会减少最后一位

if __name__ == '__main__':
    print('测试代码：')
    print('初始化一个栈stackA')
    stackA = stack()
    print(stackA)
    print('数字1进栈')
    stackA.push(1)
    print(stackA)
    print('字符串jack进栈')
    stackA.push('jack')
    print(stackA)
    print('布尔型True进栈')
    stackA.push(True)
    print(stackA)
    print('查看栈顶元素')
    print(stackA.peek())
    print('栈顶元素出栈')
    str(stackA.pop())
    print('获取栈长')
    print(stackA.size())
    print('是否为空')
    if stackA.isEmpty():
        print('为空')
    else:
        print('非空')
