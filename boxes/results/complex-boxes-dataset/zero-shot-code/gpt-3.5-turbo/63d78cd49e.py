box_0 = ['shoe', 'snow', 'lamp', 'violin']
box_1 = ['perfume', 'laptop', 'boat', 'scarf', 'gloves']
box_2 = ['tiger']
box_3 = ['tape', 'soap', 'fridge', 'thunder', 'headphone']
box_4 = ['razor']
box_5 = ['phone', 'note']
box_6 = []
box_7 = ['guitar', 'elephant']
box_8 = ['harmonica', 'tree', 'glove', 'submarine', 'jungle']
box_9 = ['island']
box_10 = ['makeup', 'wire', 'cup']
box_11 = ['starfish', 'chair', 'dice']
box_12 = ['octopus', 'rock', 'spoon', 'blender', 'rain']

box_9.remove('island')
box_5.extend(['cup', 'makeup'])
box_11.append(box_4.pop())
box_3.remove('soap')
box_3.remove('thunder')
box_3.remove('tape')
box_10.remove('wire')
box_8.extend(['laptop', 'scarf', 'gloves'])
box_9.extend(['star', 'speaker'])
box_11.clear()
box_3.remove('fridge')
box_7[0] = 'drum'
box_5.remove('phone')
box_2, box_12 = box_12, box_2
box_0, box_9 = box_9, box_0
box_1.clear()
box_7[0] = 'bowl'
box_8[3], box_8[0] = box_8[0], box_8[3]
box_0[1], box_9[0] = box_9[0], box_0[1]
box_10.extend(['forest', 'lamp'])
box_3.extend(['forest', 'lamp'])

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")