Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3,'python',[1,2],23]
>>> a[-2]
[1, 2]
>>> a[4]
[1, 2]
>>> a[-2][1]
2
>>> a[4][0]
1
>>> a=[1,2,3,4,5,6,7,8,[-4,-1000],1]
>>> a[-2]
[-4, -1000]
>>> a[-2][2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[-2][2]
IndexError: list index out of range
>>> a[-2][-1]
-1000
>>> a[-2][-0]
-4
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> a.pop()
10
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.insert(9,10)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.pop(0)
1
>>> a
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.insert(0,1)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.pop(4)
5
>>> a
[1, 2, 3, 4, 6, 7, 8, 9, 10]
>>> a.append(11)
>>> a
[1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
>>> a.append(12)
>>> a
[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
>>> a=[1,2,3,4,[23,-23],'python']
>>> a[4]
[23, -23]
>>> type([a])
<class 'list'>
>>> type([a[4]])
<class 'list'>
>>> a[-2:-1]
[[23, -23]]
>>> a[-2][-1]
-23
>>> a[-2][0]
23
>>> a=[1,2,3,4,5,67]
>>> a.pop(-1)
67
>>> a
[1, 2, 3, 4, 5]
>>> a.del()
SyntaxError: invalid syntax
>>> 
>>> a.del(-2)
SyntaxError: invalid syntax
>>> a=[1,2,3,4,5,6,7,8]
>>> del a(-2)
SyntaxError: cannot delete function call
>>> del(-2)
SyntaxError: cannot delete operator
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> del a(-1)
SyntaxError: cannot delete function call
>>> del b(-1)
SyntaxError: cannot delete function call
>>> del a[-1]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.append(10)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del a[2:-2)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> del a[2:-2]
>>> a
[1, 2, 9, 10]
>>> a.insert(2,3)
>>> a
[1, 2, 3, 9, 10]
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> del a[10)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> del a[10]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    del a[10]
IndexError: list assignment index out of range
>>> del a[-1]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del a
>>> 
a
>>> a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a.clear()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.clear()
NameError: name 'a' is not defined
>>> a=[1,2,3,4,5]
>>> a.clear()
>>> a
[]
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> a.remove(5)
>>> a
[1, 2, 3, 4, 6, 7, 8, 9, 10]
>>> a=[1,2,3,4,5,6,7,8,9,10)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> b=[1,2,3,4,5,6,7,8,9,10]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> b=[11,12,13,14,15,16,17,18,19,20]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> a*b
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> a.remove(6:17)
SyntaxError: invalid syntax
>>> a.remove(14)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.remove(14)
ValueError: list.remove(x): x not in list
>>> a=[1,2,3,4,5,,6,7,8]
SyntaxError: invalid syntax
>>> a=[1,2,3,4,5,6,7]
>>> a.remove(4)
>>> a
[1, 2, 3, 5, 6, 7]
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> a.clear()
>>> a
[]
>>> a.append(1)
>>> a
[1]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a[1,2,3,4,5,6,7,8,9,10]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a[1,2,3,4,5,6,7,8,9,10]
NameError: name 'a' is not defined
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> b=11,12,13,14,15,16,17,18,19,20]
SyntaxError: unmatched ']'
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> b=[11,12,13,14,15,16,17,18,19,20]
>>> a*2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a*b*2
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a*b*2
TypeError: can't multiply sequence by non-int of type 'list'
>>> a=[1,2,3,4,5,6,7]
>>> b=a
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> b
[1, 2, 3, 4, 5, 6, 7]
>>> b.pop()
7
>>> b
[1, 2, 3, 4, 5, 6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3,4,5,6,7]
>>> c=a.copy()
>>> c
[1, 2, 3, 4, 5, 6, 7]
>>> b
[1, 2, 3, 4, 5, 6]
>>> c
[1, 2, 3, 4, 5, 6, 7]
>>> 