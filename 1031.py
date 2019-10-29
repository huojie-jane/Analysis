# 1,	打印由‘*’组成的实心菱形图案
# s = '*'
# for i in range(1, 8, 2):
#     print((s * i).center(7))
# for i in reversed(range(1, 6, 2)):
#     print((s * i).center(7))

# 2,定义一个函数，以两种方式传入姓名，年龄和地点，直接在屏幕上打印出自我介绍‘你好，我的名字是name,今年age,现在居住在addr’


# def self(name,age,addr):
#     print('你好，我的名字是%s,今年%s,现在居住在%s'%(name,age,addr))
# self('sam',18,'上海')
# self(name='jack',age=19,addr='北京')
# 3，将一个英文语句以单词为单位逆序排放，左右单词之间用一个空格隔开
# 除了英文字母外，不含其它字符，输入描述：将一个英文语句以单词为单位逆序排放。- 输出描述:得到逆序的句子
# s = input('s:')
# a = s.split()
# a.reverse()
# print(' '.join(a))
# print(" ".join(s.split()[::-1]))
# 4,猜字母游戏，自己定义一个喜欢的字母给答题者去猜，若猜的不是26个小写字母就重新让用户输入，若猜的字母不是你设置的字母就给出正确提示（之前或者之后），若打错5次，则答题失败并退出游戏
# letter_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
# letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# letter = 'h'
# count = 0
# while True:
#     letter_input = input('请输入26个小写英文字母中的任意一个：')
#     count +=1
#     if letter_input not in letter_list:
#         print('请重新输入字母：')
#     elif count >= 5:
#         print('您已答错5次，答题失败')
#         break
#     elif letter_input == letter:
#         print('恭喜您，答对了，总共猜了{}次'.format(count))
#         break
#     elif letter_input > letter:
#         print('你输入的字母排在该字母之前')
#     elif letter_input < letter:
#         print('你输入的字母排在该字母之后')
#     else:
#         print('未知错误')
"""
5,编写一个名为collatz()的函数,它有一个名为number的参数。
如果参数是偶数,那么collatz()就打印出number//2,并返回
该值。如果number是奇数,collatz()就打印并返回3*number+1。
然后编写一个程序,让用户输入一个整数,并不断对这个数
调用collatz(),直到函数返回值1(令人惊奇的是,这个序列
对于任何整数都有效,利用这个序列,你迟早会得到1!既使数学
家也不能确定为什么。你的程序在研究所谓的“Collatz序列”,
它有时候被称为“最简单的、不可能的数学问题”)。
"""


# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     else:
#         return 3 * number + 1
#
#
# def main():
#     num = int(input('Num:'))
#     while True:
#         if collatz(num) == 1: # collatz(3) 3, 10, 2
#             print(1)
#             break
#         else:
#             num = collatz(num)
#             print(num)
# main()

# def printinfo():
#     print('-'*20)
# printinfo()
# c=5
# d=8
# def two_sum(a, b):
#     global c,d
#     c=3
#     print(a+b-c)
# two_sum(4,9)
# print(c)


# def li(a,b,*args,c=6,d=8,**kwargs):
#     print(*args)
#     print(args)
#     print(c,d)
#     print(kwargs)
#     return a,b
# li(1,2,3,4,5,4,9,c=3,d=0,k=5)

# a=4
# b=3
# a,b=b,a
# print(a)
# print(b)

# a,b,c,d=(1,2,3,4)
# q,w,e,r=[5,6,7,8]
# print(a)
# print(e)
#
# student = {'name':'qqq','age':18}
# a,b = student
# print(student[a])
# print(b)
# def info(*args,b=1,**kwargs):
#     s = 0
#     for i in args:
#         s+=i
#     s+=b
#     for j in kwargs.values():
#         s+=j

# print(lambda a,b:a+b)
# li = [1,2,3,4]
# print(li.sort())


# li = ['姓名','性别','age']
# li2 = ['sam','man',18]
# dic = {}
# for i, j in zip(li, li2):
#     dic[i] = j
# print(dic)
# dic = {i:j for i,j in zip(li,li2)}
# print(dic)
# print(len(dic))
# print(len(li))

# res =[i for i in range(15) if i>3]
# print(res)

# dic = {'name':'sam','age':18}
# dic['sex'] = 'man'

li3 = [98,86,90]
li4 = [90,95,96]
for i,j in zip(li3,li4):
    if i>j:
        print('张三成绩高')
    else:
        print('李四成绩高')
# res =[print('张三成绩高') for i,j in zip(li3,li4) if i>j ]


