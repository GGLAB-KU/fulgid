box_0 = ['console', 'thread', 'tree']
box_1 = []
box_2 = []
box_3 = []
box_4 = ['sock']
box_5 = ['razor', 'drum', 'sculpture', 'earring']
box_6 = ['polish', 'doll', 'card', 'bag']
box_7 = ['sandals', 'swimsuit', 'blanket', 'boot']

box_4.remove('sock')
box_0[1], box_7[3] = box_7[3], box_0[1]
box_5[0], box_5[1], box_5[2] = 'tie', 'forest', 'speaker'
box_7[1] = 'controller'
box_5[2], box_5[0] = 'car', 'gloves'
box_6.extend(['dress', 'razor', 'brush'])
box_0[1], box_7[0] = box_7[0], box_0[1]
box_0.extend(['cow', 'crown', 'seaweed'])
box_0[0], box_6[2] = box_6[2], box_0[0]
box_5.append(box_6.pop(0))
box_4.append(box_7.pop(1))
box_6.remove('razor')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")