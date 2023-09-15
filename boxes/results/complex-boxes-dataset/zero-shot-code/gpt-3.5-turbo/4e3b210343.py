box_0 = ['shark', 'boat', 'watch']
box_1 = ['hat', 'paint', 'swimsuit', 'brush']
box_2 = ['freezer', 'fridge', 'comb', 'tree']
box_3 = ['card', 'key', 'zipper', 'lock', 'oven']
box_4 = ['cloud', 'scarf', 'meteor']
box_5 = ['plate']
box_6 = ['basket', 'ring', 'glasses']
box_7 = ['elephant', 'pillow', 'sculpture', 'pen']
box_8 = ['pants', 'puzzle']

box_7 = []
box_2[2], box_3[0] = box_3[0], box_2[2]
box_6 = []
box_5.extend(['oven', 'dice'])
box_8 = ['watch', 'plane']
box_5 = ['lipstick', 'book']
box_4.remove('meteor')
box_4.extend(['shelf', 'tree', 'glasses'])
box_1[1], box_4[0] = box_4[0], box_1[1]
box_4.remove('scarf')
box_3.append('star')
box_4.remove('shelf')
box_4.remove('glasses')
box_1.extend(['submarine', 'snow'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)