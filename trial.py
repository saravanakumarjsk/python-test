s = 'spam'
for i in range(len(s)):
    s = s[1:] + s[:1]
    print(s)
    
