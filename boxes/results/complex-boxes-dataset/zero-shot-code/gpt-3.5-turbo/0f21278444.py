box_0 = ['wire', 'forest', 'paint', 'spoon', 'tie']
box_1 = ['cat']
box_2 = ['shark', 'pot', 'perfume', 'motorcycle']
box_3 = ['ring', 'magnet', 'moon']
box_4 = ['sculpture', 'belt', 'lamp']
box_5 = ['candle', 'guitar', 'brush']
box_6 = ['toy', 'microscope']
box_7 = ['toothpaste', 'comet']
box_8 = ['shirt', 'beach', 'chair', 'ocean', 'fish']
box_9 = ['star', 'whistle', 'sun', 'soap', 'dice']
box_10 = ['starfish']
box_11 = ['horse', 'snow', 'headphone', 'violin', 'doll']
box_12 = ['button', 'sandals', 'pan', 'desert']
box_13 = ['clock', 'basket', 'jacket', 'oven', 'speaker']

def swap_items(box1, index1, box2, index2):
    item1 = box1.pop(index1)
    item2 = box2.pop(index2)
    box1.append(item2)
    box2.append(item1)

def remove_item(box, item):
    if item in box:
        box.remove(item)

def move_item(box1, index1, box2):
    item = box1.pop(index1)
    box2.append(item)

def empty_box(box):
    box.clear()

swap_items(box7, 0, box3, 0)
swap_items(box0, 1, box4, 1)
swap_items(box5, 0, box10, 0)
swap_items(box5, 1, box9, 1)
swap_items(box5, 2, box4, 2)
remove_item(box7, 'ring')
remove_item(box7, 'comet')
remove_item(box4, 'makeup')
remove_item(box4, 'sculpture')
remove_item(box12, 'desert')
remove_item(box12, 'sandals')
swap_items(box2, 0, box4, 3)
remove_item(box9, 'dice')
remove_item(box9, 'sun')
remove_item(box12, 'button')
remove_item(box12, 'pan')
move_item(box11, 0, box13)
swap_items(box10, 0, box9, 3)
move_item(box9, 0, box4)
move_item(box9, 0, box4)
move_item(box10, 0, box9)
move_item(box5, 0, box10)
move_item(box5, 0, box10)
move_item(box5, 0, box10)
swap_items(box11, 4, box9, 0)
empty_box(box2)
swap_items(box8, 4, box0, 4)
move_item(box11, 3, box7)
move_item(box7, 0, box0)
box2.extend(['camera', 'starfish'])
box1.extend(['forest', 'fish', 'wire'])

boxes = [box0, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")