box_0 = ['drum', 'skirt', 'toy', 'snow']
box_1 = ['earring', 'vase', 'table']
box_2 = ['telescope']
box_3 = ['branch', 'horn', 'leaf', 'glasses']
box_4 = []
box_5 = ['flute', 'scarf', 'toaster']
box_6 = ['headphone']
box_7 = ['console', 'bracelet']
box_8 = ['dog']

box_4.extend(['key', 'flower'])
box_5.remove('toaster')
box_6.remove('headphone')
box_2.clear()
box_8[0] = 'butterfly'
box_3[1], box_7[1] = box_7[1], box_3[1]
box_7.remove('horn')
box_4[0], box_4[1] = box_3[0], box_3[1]
box_8.clear()
box_3.extend(['key', 'crown'])
box_3.extend(box_4[0:2])
box_1.extend(box_0[0:2])
box_6.extend(box_3[2:])
box_7[0] = 'whistle'

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)