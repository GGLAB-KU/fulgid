box_0 = []
box_1 = ['spoon']
box_2 = ['train', 'whistle', 'belt', 'button']
box_3 = ['doll', 'pen']
box_4 = ['jungle']

box_2.remove('train')
box_2.remove('whistle')
box_3.remove('doll')
box_3.append('camera')
box_1.remove('spoon')
box_3.extend(['razor', 'oven'])
box_4.remove('jungle')
box_3.clear()
box_2.remove('belt')
box_2.remove('button')
box_2.extend(['dolphin', 'seaweed'])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)