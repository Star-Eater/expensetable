

_list = [('Income', 123), ('Food', 25)]

d = dict()
for x,y in _list:
    d[x] = d.get(x, 0) + y;
print(d)
