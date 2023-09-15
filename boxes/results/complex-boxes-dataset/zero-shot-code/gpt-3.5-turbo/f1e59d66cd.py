box_0 = ['car', 'tie', 'lipstick', 'horse', 'rocket']
box_1 = ['butterfly', 'camera', 'piano', 'coat']
box_2 = ['lion', 'starfish', 'lightning', 'leaf', 'shelf']
box_3 = ['comet', 'wire']
box_4 = ['shark', 'tree', 'mountain']
box_5 = ['cup', 'oven']
box_6 = ['helmet', 'game', 'cat', 'console']

box_5.extend(['bag', 'book', 'note'])
box_1[0], box_5[2] = box_5[2], box_1[0]
box_2.remove('lion')
box_2.remove('shelf')
box_2.remove('lightning')
box_2.append('star')
box_4[1] = 'oven'
box_2[1], box_6[0] = box_6[0], box_2[1]
box_2[1], box_6[1] = box_6[1], box_2[1]
box_5[0] = 'blender'
box_2.remove('helmet')
box_2.remove('game')
box_5.remove('oven')
box_5.remove('butterfly')
box_5.remove('book')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")