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

s = set([1,1,2,3])#重复元素会过滤
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
