box_0 = ['bear', 'boat']
box_1 = []
box_2 = ['truck', 'sculpture', 'umbrella', 'laptop', 'violin']
box_3 = []
box_4 = ['shark', 'magnet', 'train']
box_5 = ['fork', 'guitar', 'scarf', 'doll', 'bicycle']
box_6 = ['island', 'makeup']
box_7 = []

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)

def move_item(source_box, item, destination_box):
    source_box.remove(item)
    destination_box.append(item)

def replace_item(box, old_item, new_item):
    box.remove(old_item)
    box.append(new_item)

def remove_item(box, item):
    box.remove(item)

def empty_box(box):
    box.clear()

# Move the fork from Box 5 to Box 2
move_item(box_5, 'fork', box_2)

# Move the island and the makeup from Box 6 to Box 5
move_item(box_6, 'island', box_5)
move_item(box_6, 'makeup', box_5)

# Replace the magnet with the grass in Box 4
replace_item(box_4, 'magnet', 'grass')

# Remove the grass and the shark from Box 4
remove_item(box_4, 'grass')
remove_item(box_4, 'shark')

# Replace the bear and the boat with the truck and the makeup in Box 0
replace_item(box_0, 'bear', 'truck')
replace_item(box_0, 'boat', 'makeup')

# Move the fork and the umbrella from Box 2 to Box 5
move_item(box_2, 'fork', box_5)
move_item(box_2, 'umbrella', box_5)

# Remove the train from Box 4
remove_item(box_4, 'train')

# Move the truck and the makeup from Box 0 to Box 7
move_item(box_0, 'truck', box_7)
move_item(box_0, 'makeup', box_7)

# Empty Box 2
empty_box(box_2)

# Move the makeup from Box 5 to Box 1
move_item(box_5, 'makeup', box_1)

# Swap the truck in Box 7 with the makeup in Box 1
replace_item(box_7, 'truck', 'makeup')
replace_item(box_1, 'makeup', 'truck')

# Replace the makeup and the makeup with the starfish and the battery in Box 7
replace_item(box_7, 'makeup', 'starfish')
replace_item(box_7, 'makeup', 'battery')

# Print the final state of the boxes
print_boxes()