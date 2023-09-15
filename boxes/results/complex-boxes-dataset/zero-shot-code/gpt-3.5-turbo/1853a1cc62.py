box = {
    0: ['sock', 'boot', 'lock', 'gloves'],
    1: [],
    2: ['bell', 'shoes', 'microscope'],
    3: ['needle'],
    4: ['lipstick', 'earring'],
    5: ['skirt', 'mask', 'bracelet', 'plate', 'grass'],
    6: ['shirt'],
    7: ['storm', 'book', 'pants', 'flute'],
    8: ['phone'],
    9: [],
    10: ['dress', 'frame', 'crown', 'moon'],
    11: ['bird', 'bowl', 'mirror', 'horse', 'console'],
    12: ['branch', 'rock', 'spoon', 'harmonica', 'sculpture'],
    13: ['cow', 'freezer', 'violin'],
    14: ['tape', 'cup', 'glove', 'lamp', 'dice']
}

def move_item(from_box, to_box, item):
    box[from_box].remove(item)
    box[to_box].append(item)

def remove_item(from_box, item):
    box[from_box].remove(item)

def add_item(to_box, item):
    box[to_box].append(item)

# Move the phone from Box 8 to Box 4
move_item(8, 4, 'phone')

# Replace the needle with the pot in Box 3
remove_item(3, 'needle')
add_item(3, 'pot')

# Remove the skirt and the grass and the plate from Box 5
remove_item(5, 'skirt')
remove_item(5, 'grass')
remove_item(5, 'plate')

# Move the pot from Box 3 to Box 9
move_item(3, 9, 'pot')

# Swap the shirt in Box 6 with the dress in Box 10
move_item(6, 10, 'dress')
move_item(10, 6, 'shirt')

# Move the dress from Box 6 to Box 5
move_item(6, 5, 'dress')

# Put the submarine into Box 2
add_item(2, 'submarine')

# Swap the shoes in Box 2 with the book in Box 7
move_item(2, 7, 'book')
move_item(7, 2, 'shoes')

# Remove the mask and the bracelet and the dress from Box 5
remove_item(5, 'mask')
remove_item(5, 'bracelet')
remove_item(5, 'dress')

# Remove the dice and the lamp from Box 14
remove_item(14, 'dice')
remove_item(14, 'lamp')

# Move the submarine and the book from Box 2 to Box 10
move_item(2, 10, 'submarine')
move_item(2, 10, 'book')

# Replace the bowl with the boat in Box 11
remove_item(11, 'bowl')
add_item(11, 'boat')

# Put the toothbrush into Box 13
add_item(13, 'toothbrush')

# Replace the pot with the motorcycle in Box 9
remove_item(9, 'pot')
add_item(9, 'motorcycle')

# Move the microscope from Box 2 to Box 9
move_item(2, 9, 'microscope')

# Remove the cow and the freezer and the toothbrush from Box 13
remove_item(13, 'cow')
remove_item(13, 'freezer')
remove_item(13, 'toothbrush')

# Put the bracelet and the branch into Box 7
add_item(7, 'bracelet')
add_item(7, 'branch')

# Replace the cup with the train in Box 14
remove_item(14, 'cup')
add_item(14, 'train')

# Swap the bell in Box 2 with the train in Box 14
move_item(2, 14, 'bell')
move_item(14, 2, 'train')

# Put the battery into Box 4
add_item(4, 'battery')

# Put the frame and the dolphin and the coral into Box 13
add_item(13, 'frame')
add_item(13, 'dolphin')
add_item(13, 'coral')

# Move the train from Box 2 to Box 5
move_item(2, 5, 'train')

# Print the contents of each box
for i in range(15):
    print(f"Box {i}: {box[i]}")