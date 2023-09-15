box_0 = ['horn', 'coin', 'motorcycle']
box_1 = ['note']
box_2 = ['keyboard', 'elephant', 'truck', 'paint']
box_3 = ['ring', 'toaster']
box_4 = ['scarf', 'spoon', 'necklace', 'flute', 'camera']
box_5 = ['rocket']
box_6 = ['laptop', 'gloves', 'glove', 'coral']
box_7 = []
box_8 = ['glasses']
box_9 = ['boat', 'console', 'shoes']

def swap_items(box1, index1, box2, index2):
    item1 = box1.pop(index1)
    item2 = box2.pop(index2)
    box1.append(item2)
    box2.append(item1)

def remove_items(box, *items):
    for item in items:
        if item in box:
            box.remove(item)

def add_items(box, *items):
    box.extend(items)

swap_items(box_1, 0, box_0, 2)
swap_items(box_8, 0, box_0, 0)
add_items(box_1, 'tie')
remove_items(box_4, 'flute', 'necklace')
remove_items(box_2, 'keyboard', 'elephant', 'truck')
add_items(box_9, 'chair')
swap_items(box_5, 0, box_3, 0)
box_6.remove('coral')
add_items(box_6, 'charger')
add_items(box_2, 'beach')
remove_items(box_3, 'ring', 'toaster')
box_8.remove('note')
swap_items(box_3, 0, box_1, 2)
remove_items(box_1, 'tie', 'rocket')
add_items(box_6, 'coin', 'glasses')
add_items(box_6, 'paint', 'beach')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")