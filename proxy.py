
class A:
    def f_one(self, x):
        print("here is f_one")
        print("x=",x)
        print("-"*100)
 
    def f_two(self):
        print("here is f_two")
        print("-"*100)
 
class B(A):
    def __init__(self):
        self._a = A()
 
    def f_three(self):
        print('this is f3')
 
    def __getattr__(self, name):#相当于重写了__getattr__,利用__getattr_来实现委托的效果（其实委托就是甩锅的意思啦，B搞不定，甩锅给A）
        return getattr(self._a, name)
if __name__ == '__main__':
    b_test=B()
    x=6
    b_test.f_one(x)
    b_test.f_two()
    b_test.f_three()