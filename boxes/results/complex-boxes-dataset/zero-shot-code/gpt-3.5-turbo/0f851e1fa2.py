box_0 = ['rocket', 'lion', 'dog']
box_1 = ['submarine', 'thread', 'doll', 'piano', 'hat']
box_2 = ['spoon', 'speaker', 'book']
box_3 = []
box_4 = ['scissors']
box_5 = ['freezer', 'game', 'wig']
box_6 = ['blanket', 'harmonica', 'headphone', 'bird']
box_7 = ['fridge', 'plate', 'vase', 'shorts', 'toaster']
box_8 = ['battery', 'mountain', 'car']

box_4.remove('scissors')
box_4.append('skirt')

box_3.append(box_2.pop(1))

box_6.remove('blanket')

box_2.append('desert')

box_0.remove('rocket')
box_0.remove('dog')
box_0.remove('bird')
box_0.append('horse')
box_0.append('dress')
box_0.append('mirror')

box_3.remove('speaker')
box_3.append('mask')

box_6.remove('harmonica')

box_2[1], box_3[0] = box_3[0], box_2[1]

box_1.clear()

box_5.append('bicycle')
box_5.append('controller')

box_6.append('cup')
box_6.append('moon')

box_2.clear()

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)