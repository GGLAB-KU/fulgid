box_0 = ['frame', 'mixer']
box_1 = []
box_2 = ['makeup', 'lightning', 'cloud', 'cup']
box_3 = ['microscope', 'wire']
box_4 = []
box_5 = ['plate', 'island', 'ring', 'forest']
box_6 = ['fish', 'mask']
box_7 = ['pillow', 'shoes']
box_8 = ['wallet']
box_9 = ['controller', 'card']
box_10 = ['dice']

box_0 = []
box_4 = []
box_3.remove('magnet')
box_0 = ['jacket', 'storm']
box_0 = ['thread', 'apple']
box_0 = []
box_8.append('wallet')
box_9.remove('spoon')
box_7[box_7.index('pillow')] = 'ring'
box_10.append('dice')
box_2[box_2.index('makeup')] = 'wire'
box_10[box_10.index('dice')] = 'plate'
box_3.remove('horn')
box_6.extend(['fish', 'mask'])
box_9.extend(['controller', 'card'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")