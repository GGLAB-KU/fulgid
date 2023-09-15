box_0 = ['puzzle', 'cup', 'train']
box_1 = ['fish', 'submarine']
box_2 = ['spoon', 'coin', 'boat']
box_3 = ['forest', 'bird', 'cat', 'star']
box_4 = ['pan', 'bear', 'tree']
box_5 = ['tie', 'shorts', 'scissors', 'mountain', 'microwave']
box_6 = ['skirt', 'elephant', 'umbrella', 'button', 'cow']
box_7 = ['wire', 'polish', 'oven', 'game', 'thread']
box_8 = []
box_9 = ['grinder', 'swimsuit', 'plane', 'drum']
box_10 = ['plate', 'usb', 'dress', 'comb']
box_11 = []
box_12 = ['note', 'phone', 'basket']

def move_items():
    box_3.extend([box_6.pop(3), box_6.pop(3), box_6.pop(3)])
    box_9.remove('swimsuit')
    box_9.remove('drum')
    box_9.remove('grinder')
    box_7[4], box_9[2] = box_9[2], box_7[4]
    box_9[2], box_4[0] = box_4[0], box_9[2]
    box_1.clear()
    box_10[0], box_9[2] = box_9[2], box_10[0]
    box_6[1], box_10[0] = box_10[0], box_6[1]
    box_0[0], box_7[2] = box_7[2], box_0[0]
    box_12.remove('note')
    box_7.append(box_10.pop(3))
    box_10.append('swimsuit')
    box_12.extend([box_6.pop(1), box_10.pop(1)])
    box_3.append('rocket')
    box_5.remove('mountain')
    box_5.remove('tie')
    box_5.remove('shorts')
    box_9[0] = 'storm'
    box_4[1], box_5[2] = box_5[2], box_4[1]
    box_1.append('thunder')
    box_1.remove('thunder')
    box_5.remove('microwave')

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

move_items()
print_boxes()