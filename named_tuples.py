from collections import namedtuple

# color = (55,155,255)

Color = namedtuple('Color',['red','green','blue'])
color = Color(55,75,78)
print(color)
print(color.red)
print(color.green)
print(color.blue)

