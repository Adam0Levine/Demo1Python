#names = ["Leo","Ma","Hu"]
#for name in names:
#    print(name)
#简单的一个循环


# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)
#1-100的和

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)
# 1-100的奇数之和

# d={'Mike':100,'Jack':88,'Sia':97}
# print(d['Mike'])
# d.pop('Jack')
# print(d)
# print('Mike' in d)#检查元素是否在dict里
# print(d.get('Mike'))#检查元素是否在dict里
# print(d.get('Jack'))#如果没有则返回None
# print(d.get('Jack',-1))#如果没有返回自己定义的值
# 和list比较，dict有以下几个特点：
#
#     查找和插入的速度极快，不会随着key的增加而变慢；
#     需要占用大量的内存，内存浪费多。
#
# 而list相反：
#
#     查找和插入的时间随着元素的增加而增加；
#     占用空间小，浪费内存很少。

# s = set([1,1,2,3])#重复元素会过滤
# print(s)
# s.add(4)
# print(s)
# s.remove(4)
# print(s)
# s2 = set([1,2,4])
# print(s&s2)
# print(s|s2)


# print(max(1,3,5,6))
#
# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))  #十六进制
#
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# n = int(input())
#
# print(my_abs(n))#自己定义的一个绝对值

# def power(x,n=2):
#     s = 1
#     while n>0:
#         n = n - 1
#         s = s * x;
#     return s
# print(power(3,3))#x的n次方
#默认参数必须指向不变对象！

# def calc(*numbers):
#     s = 0
#     for n in numbers:
#         s = s + n * n
#     return s
# # print(calc(1,2,3))
# num = [1,2,3,4]
# print(calc(*num))#参数数量是可变的

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# person('Jack',23)
# person('Mike',33,addr='China')
# extra ={'city':'Beijing','job':'engineer'}
# person('Jack',24,**extra)

#
# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n-1)
# print(fac(5))#阶乘

# L = ['Mike','Jack','Tony','Bob','Sia']
# print(L[0:3]) #从0开始到3但不包括3
# print(L[:3])  #从0开始还可以省略
# print(L[-2:])

# L = list(range(100))
# print(L[::2])#每两位取值
# print(L[:]) #整个list集合

# 'ABCDEFGHI'[1:3] #直接截取两位

# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))#是否可以迭代

# [x*x for x in range(100)]
# [x*x for x in range(10) if x%2==0]

# import os
# [d for d in os.listdir('.')]

# g = (x*x for x in range(10))
# for n in g:
#     print(n)


# def fib(n):
#     s = 0
#     t = 1
#     w = 1
#     while n>0:
#         w = s+t
#         s = t
#         t =  w
#     return w
# print(fib(3))