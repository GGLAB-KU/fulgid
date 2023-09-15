box_0 = ['plane']
box_1 = []
box_2 = ['key', 'grinder', 'phone']
box_3 = ['oven', 'doll']

box_3 = []

box_2.extend(['book', 'helmet', 'thunder'])
box_0, box_2 = box_2, box_0

box_0.remove('phone')

box_2.remove('key')
box_2.remove('thunder')

box_2.remove('book')
box_0.remove('plane')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)