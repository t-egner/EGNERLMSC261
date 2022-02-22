Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> three = 3
>>> print(f"{three} Blind Mice")
3 Blind Mice
>>>  a="******"
    for i in range(0,3):
  
    print("\t"*(i+1),a)
    
SyntaxError: unexpected indent
>>> a + "******"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a + "******"
NameError: name 'a' is not defined
>>> a = "******"
>>> for i in range(0,3):
	print("\t"*(i + 1),a)

	
	 ******
		 ******
			 ******
>>> a = "3BlindMice"
>>> for i in range(0,3):
	print("\t"*(i + 1),a)

	
	 3BlindMice
		 3BlindMice
			 3BlindMice
>>> a = 3
>>> b = Blind
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b = Blind
NameError: name 'Blind' is not defined
>>> a = 3
>>> b = "Blind"
>>> c = "Mice"
>>> for i in range(0,3):
	print("\t"*(i + 1),a)
	print("\t"*(i + 1),b)
	print("\t"*(i + 1),c)

	
	 3
	 Blind
	 Mice
		 3
		 Blind
		 Mice
			 3
			 Blind
			 Mice
>>> a = 3
>>> b = "Blind"
>>> c = "Mice"
>>> for i in range(0,3):
	print"\t"*(i + 1),a)
	
SyntaxError: invalid syntax
>>> a = 3
>>> b = "Blind"
>>> c = "Mice"
>>> for i in range(0,3):
	
SyntaxError: multiple statements found while compiling a single statement
>>> a = 3
>>> b = "Blind"
>>> c = "Mice"
>>> for i in range(0,3):
	print("\t"*(i + 1),a)
	print("\t"*(i + 2),b)
	print("\t"*(i + 3),c)

	
	 3
		 Blind
			 Mice
		 3
			 Blind
				 Mice
			 3
				 Blind
					 Mice
>>> 