Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 02:47:15) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup=4,5,6
>>> tup
(4, 5, 6)
>>> tuple([4,0,2])
(4, 0, 2)
>>> tup=tup('string')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup=tup('string')
TypeError: 'tuple' object is not callable
>>> 
>>> tup=tuple('string')
>>> tup
('s', 't', 'r', 'i', 'n', 'g')
>>> tup[0]
's'
>>> tup=tuple(['foo', [1,2],True])
>>> tup[2]
True
>>> tup[2]=False
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tup[2]=False
TypeError: 'tuple' object does not support item assignment
>>> tup[1].append(3)
>>> tup
('foo', [1, 2, 3], True)
>>> (4,None,'foo')+(6,0)+('bar',)
(4, None, 'foo', 6, 0, 'bar')
>>> tup=(4,5,6)
>>> a,b,c=tup
>>> b
5
>>> a
4
>>> c
6
>>> 
