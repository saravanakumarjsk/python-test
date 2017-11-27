this expalains about you the file concept
>>> f = open('new.txt','w')
>>> f.write('hello saravana')
14
>>> f.close()
>>> f = open('new.txt')
>>> f.readline()
'hello saravana'
>>> f = open('new.txt','w')
>>> f.write('hello sravana')
13
>>> f.write('hello kumar')
11
>>> f.write('hello subash')
12
>>> f.close()
>>> f = open('new.txt')
>>> k = (open('new.txt').read())
>>> print(k)
hello sravanahello kumarhello subash
>>> 
