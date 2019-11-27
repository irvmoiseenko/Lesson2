def fun(a, b):
    if not type(a) == str or not type(b) == str:
        return 0
    if len(a) == len(b):
        return 1
    if len(a) > len(b):
        return 2
    if len(a) != len(b) and b == 'learn':
        return 3

print(fun('ghj', 4))
print(fun('as', 'hj'))
print(fun('asss', 'hj'))
print(fun('asss', 'learn'))