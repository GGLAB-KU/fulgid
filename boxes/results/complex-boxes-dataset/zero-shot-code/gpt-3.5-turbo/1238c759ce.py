box = {
    0: ['plate', 'gloves', 'telescope', 'dolphin'],
    1: [],
    2: ['crown'],
    3: ['blender'],
    4: ['frame', 'paint', 'battery'],
    5: ['cat', 'pot', 'basket'],
    6: ['lion'],
    7: ['shelf', 'star', 'wire', 'swimsuit'],
    8: ['bag', 'mountain'],
    9: ['needle', 'shampoo', 'thunder', 'coat'],
    10: ['glove', 'cow', 'horse'],
    11: ['brush', 'butterfly'],
    12: []
}

def move_item(from_box, to_box, item):
    box[from_box].remove(item)
    box[to_box].append(item)

def remove_item(from_box, item):
    box[from_box].remove(item)

def add_item(to_box, item):
    box[to_box].append(item)

# Move the brush and the butterfly from Box 11 to Box 12
move_item(11, 12, 'brush')
move_item(11, 12, 'butterfly')

# Move the frame and the battery from Box 4 to Box 2
move_item(4, 2, 'frame')
move_item(4, 2, 'battery')

# Put the cow into Box 11
add_item(11, 'cow')

# Remove the mountain and the bag from Box 8
remove_item(8, 'mountain')
remove_item(8, 'bag')

# Swap the gloves in Box 0 with the brush in Box 12
move_item(0, 12, 'gloves')
move_item(12, 0, 'brush')

# Swap the lion in Box 6 with the frame in Box 2
move_item(6, 2, 'lion')
move_item(2, 6, 'frame')

# Remove the shampoo and the coat and the thunder from Box 9
remove_item(9, 'shampoo')
remove_item(9, 'coat')
remove_item(9, 'thunder')

# Put the swimsuit into Box 9
add_item(9, 'swimsuit')

# Move the basket from Box 5 to Box 7
move_item(5, 7, 'basket')

# Put the lion into Box 12
add_item(12, 'lion')

# Remove the pot from Box 5
remove_item(5, 'pot')

# Move the cow from Box 11 to Box 2
move_item(11, 2, 'cow')

# Move the frame from Box 6 to Box 12
move_item(6, 12, 'frame')

# Swap the cat in Box 5 with the star in Box 7
move_item(5, 7, 'cat')
move_item(7, 5, 'star')

# Move the paint from Box 4 to Box 9
move_item(4, 9, 'paint')

# Swap the horse in Box 10 with the cat in Box 7
move_item(10, 7, 'horse')
move_item(7, 10, 'cat')

# Replace the needle and the paint with the cup and the chair in Box 9
remove_item(9, 'needle')
remove_item(9, 'paint')
add_item(9, 'cup')
add_item(9, 'chair')

# Remove the lion from Box 12
remove_item(12, 'lion')

# Swap the star in Box 5 with the crown in Box 2
move_item(5, 2, 'star')
move_item(2, 5, 'crown')

# Replace the battery and the lion with the snow and the pillow in Box 2
remove_item(2, 'battery')
remove_item(2, 'lion')
add_item(2, 'snow')
add_item(2, 'pillow')

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")