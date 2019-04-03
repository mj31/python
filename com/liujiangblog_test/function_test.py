def add(x,n=2):
    return x*n
print(add(2))

def func(a=[]):
    a.append("A")
    return a

print(func())
print(func())
print(func())

try:
    1/0
except Exception as e:
    print(e)
finally:
    print("结束")
print(12)
