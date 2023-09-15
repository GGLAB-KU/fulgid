box_0 = ['thread', 'bicycle']
box_1 = ['pillow']
box_2 = ['seaweed', 'blanket', 'rain', 'meteor']
box_3 = ['train', 'rock', 'boat']
box_4 = ['swimsuit', 'perfume', 'charger']
box_5 = ['key', 'camera']
box_6 = []
box_7 = ['toy', 'earring', 'gloves', 'tree']
box_8 = ['scissors']
box_9 = ['pen', 'butterfly', 'chair']

box_0.remove('thread')
box_0.append('comb')

box_5.remove('camera')
box_5.append('violin')

box_4.extend(box_9.pop(0))
box_4.extend(box_9.pop(0))

box_8.append(box_0.pop(0))

box_4[0], box_5[0] = box_5[0], box_4[0]

box_3 = ['bus', 'harmonica', 'tree']

box_7 = []

box_6.extend(['truck', 'pan'])

box_9.append('thunder')

box_0.append(box_1.pop(0))

box_6.append(box_2.pop(0))

box_8.extend(box_2.pop(0))
box_8.extend(box_2.pop(0))

box_9.extend(['wallet', 'skirt', 'storm'])

box_3 = ['jacket', 'dice']

box_9[0], box_8[2] = box_8[2], box_9[0]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)