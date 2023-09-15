box = {
    0: ['coral', 'toy', 'pants', 'guitar'],
    1: ['vase', 'blender', 'pillow', 'mountain'],
    2: ['makeup', 'microscope', 'apple'],
    3: ['ocean', 'drum'],
    4: [],
    5: ['lightning'],
    6: ['shorts', 'sculpture', 'dice'],
    7: [],
    8: ['harmonica', 'shirt'],
    9: ['elephant', 'plane'],
    10: ['wire'],
    11: [],
    12: ['crown', 'piano', 'thunder']
}

def move_item(from_box, to_box, item):
    if item in box[from_box]:
        box[from_box].remove(item)
        box[to_box].append(item)

def replace_items(box_num, items):
    box[box_num] = items

def remove_items(box_num, items):
    for item in items:
        if item in box[box_num]:
            box[box_num].remove(item)

def swap_items(box_num1, box_num2, item1, item2):
    if item1 in box[box_num1] and item2 in box[box_num2]:
        box[box_num1].remove(item1)
        box[box_num2].remove(item2)
        box[box_num1].append(item2)
        box[box_num2].append(item1)

# Move the plane from Box 9 to Box 10
move_item(9, 10, 'plane')

# Move the shirt and the harmonica from Box 8 to Box 4
move_item(8, 4, 'shirt')
move_item(8, 4, 'harmonica')

# Replace the ocean and the drum with the boot and the shoe in Box 3
replace_items(3, ['boot', 'shoe'])

# Move the elephant from Box 9 to Box 0
move_item(9, 0, 'elephant')

# Move the pants and the elephant and the coral from Box 0 to Box 12
move_item(0, 12, 'pants')
move_item(0, 12, 'elephant')
move_item(0, 12, 'coral')

# Move the boot from Box 3 to Box 5
move_item(3, 5, 'boot')

# Swap the plane in Box 10 with the coral in Box 12
swap_items(10, 12, 'plane', 'coral')

# Remove the vase and the mountain from Box 1
remove_items(1, ['vase', 'mountain'])

# Move the harmonica from Box 4 to Box 10
move_item(4, 10, 'harmonica')

# Remove the dice from Box 6
remove_items(6, ['dice'])

# Move the blender from Box 1 to Box 0
move_item(1, 0, 'blender')

# Swap the shirt in Box 4 with the sculpture in Box 6
swap_items(4, 6, 'shirt', 'sculpture')

# Replace the microscope and the apple and the makeup with the snow and the freezer and the bag in Box 2
replace_items(2, ['snow', 'freezer', 'bag'])

# Put the pillow and the storm into Box 10
box[10].extend(['pillow', 'storm'])

# Swap the elephant in Box 12 with the pillow in Box 1
swap_items(12, 1, 'elephant', 'pillow')

# Remove the plane and the pillow and the piano from Box 12
remove_items(12, ['plane', 'pillow', 'piano'])

# Swap the storm in Box 10 with the sculpture in Box 4
swap_items(10, 4, 'storm', 'sculpture')

# Move the shirt and the shorts from Box 6 to Box 2
move_item(6, 2, 'shirt')
move_item(6, 2, 'shorts')

# Swap the thunder in Box 12 with the sculpture in Box 10
swap_items(12, 10, 'thunder', 'sculpture')

# Print the contents of each box
for box_num, items in box.items():
    print(f"Box {box_num}: {items}")