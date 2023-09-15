box_0 = ['camera', 'tree', 'rock', 'bag', 'pants']
box_1 = ['branch', 'glove', 'thread', 'basket', 'toothbrush']
box_2 = ['candle', 'brush', 'puzzle']
box_3 = ['belt']
box_4 = ['microscope', 'bear', 'thunder', 'perfume', 'snow']
box_5 = ['storm', 'helmet']
box_6 = ['pot', 'doll', 'bicycle']
box_7 = ['elephant', 'phone']
box_8 = ['car', 'table', 'fork']
box_9 = []
box_10 = ['boat', 'cloud', 'glasses']
box_11 = ['comet', 'mask', 'apple', 'jacket']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

def swap_items(box1, index1, box2, index2):
    item1 = box1.pop(index1)
    item2 = box2.pop(index2)
    box1.append(item2)
    box2.append(item1)

def move_item(source_box, source_index, destination_box):
    item = source_box.pop(source_index)
    destination_box.append(item)

def remove_item(box, index):
    box.pop(index)

def replace_items(box, index, items):
    box.pop(index)
    box.extend(items)

# Swap the glove in Box 1 with the jacket in Box 11
swap_items(box_1, 1, box_11, 3)

# Empty Box 6
box_6.clear()

# Remove the comet from Box 11
remove_item(box_11, 0)

# Move the apple from Box 11 to Box 8
move_item(box_11, 1, box_8)

# Put the belt and the bicycle and the rocket into Box 10
move_item(box_3, 0, box_10)
move_item(box_6, 2, box_10)
move_item(box_10, 0, box_10)

# Swap the brush in Box 2 with the jacket in Box 1
swap_items(box_2, 1, box_1, 0)

# Swap the thread in Box 1 with the belt in Box 3
swap_items(box_1, 1, box_3, 0)

# Move the elephant from Box 7 to Box 4
move_item(box_7, 0, box_4)

# Move the perfume and the thunder and the bear from Box 4 to Box 11
move_item(box_4, 3, box_11)
move_item(box_4, 2, box_11)
move_item(box_4, 1, box_11)

# Remove the jacket and the candle from Box 2
remove_item(box_2, 1)
remove_item(box_2, 0)

# Move the boat and the belt from Box 10 to Box 2
move_item(box_10, 0, box_2)
move_item(box_10, 0, box_2)

# Remove the helmet and the storm from Box 5
remove_item(box_5, 1)
remove_item(box_5, 0)

# Move the phone from Box 7 to Box 11
move_item(box_7, 1, box_11)

# Put the sock and the razor into Box 6
box_6.extend(['sock', 'razor'])

# Remove the puzzle and the belt and the boat from Box 2
remove_item(box_2, 1)
remove_item(box_2, 0)
remove_item(box_2, 0)

# Replace the rocket and the cloud and the glasses with the island and the puzzle and the perfume in Box 10
replace_items(box_10, 0, ['island'])
replace_items(box_10, 0, ['puzzle'])
replace_items(box_10, 0, ['perfume'])

# Replace the bicycle with the shorts in Box 10
replace_items(box_10, 0, ['shorts'])

# Move the apple from Box 8 to Box 1
move_item(box_8, 0, box_1)

# Print the final state of the boxes
print_boxes()