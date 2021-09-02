Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> True* False
0
>>> True & False
False
>>> True and True
True
>>> ((6>3) and (7<4) or (18 ==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> s1 = “Nice to have it”
s2 = “here”
SyntaxError: invalid character in identifier
>>> s1 = "nice to have it"
>>> s2 = "here"
>>> print(s1+s2)
nice to have ithere
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> print (a[3][1][2])
['hello']
>>> #5
>>> a.insert(0,s1)
>>> a.insert(8,s2)
>>> print(a)
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> ##6
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
>>> for x in numbers
SyntaxError: invalid syntax
>>> for x i numbers:
	
SyntaxError: invalid syntax
>>> for x in numbers:
	if x == 237:
		print(x)
		break;
	elif x%2 ==0:
		print(x)

		
386
462
418
344
236
566
978
328
162
758
918
237
>>> color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
SyntaxError: multiple statements found while compiling a single statement
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1 - color_list_2
{'White', 'Black'}
>>> n = int(input("enter an integer:"))
enter an integer:5
>>> t = str(n)
>>> n1 = t+t
>>> n2 = t+t+t
>>> print(n+int(n1)+int(n2))
615
>>> 
>>> sen = input("enter words:)
	    
SyntaxError: EOL while scanning string literal
>>> 	
