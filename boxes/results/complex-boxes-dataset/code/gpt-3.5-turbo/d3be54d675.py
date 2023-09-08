# Initial state of boxes
boxes = {
    0: ['razor', 'river', 'sun', 'scarf'],
    1: ['sock', 'pants', 'grass', 'leaf'],
    2: ['candle', 'shampoo', 'cup', 'blanket'],
    3: [],
    4: ['scissors', 'paint', 'guitar', 'soap'],
    5: ['train', 'boat', 'tape', 'controller', 'flower'],
    6: [],
    7: ['freezer', 'planet'],
    8: ['toaster', 'dog', 'truck', 'butterfly'],
    9: [],
    10: [],
    11: ['lock'],
    12: [],
    13: ['car', 'glove', 'thunder', 'skirt']
}

# Move the butterfly from Box 8 to Box 0.
boxes[8].remove('butterfly')
boxes[0].append('butterfly')

# Swap the toaster in Box 8 with the thunder in Box 13.
boxes[8].remove('toaster')
boxes[13].remove('thunder')
boxes[8].append('thunder')
boxes[13].append('toaster')

# Replace the tape and the boat and the flower with the scissors and the card and the belt in Box 5.
boxes[5].remove('tape')
boxes[5].remove('boat')
boxes[5].remove('flower')
boxes[5].append('scissors')
boxes[5].append('card')
boxes[5].append('belt')

# Put the makeup and the microscope and the shark into Box 11.
items_to_move = ['makeup', 'microscope', 'shark']
for item in items_to_move:
    boxes[11].append(item)

# Replace the guitar and the soap and the scissors with the plate and the vase and the sock in Box 4.
boxes[4].remove('guitar')
boxes[4].remove('soap')
boxes[4].remove('scissors')
boxes[4].append('plate')
boxes[4].append('vase')
boxes[4].append('sock')

# Replace the controller with the book in Box 5.
boxes[5].remove('controller')
boxes[5].append('book')

# Remove the toaster and the skirt from Box 13.
boxes[13].remove('toaster')
boxes[13].remove('skirt')

# Replace the glove with the note in Box 13.
boxes[13].remove('glove')
boxes[13].append('note')

# Remove the shark and the microscope from Box 11.
boxes[11].remove('shark')
boxes[11].remove('microscope')

# Swap the planet in Box 7 with the shampoo in Box 2.
boxes[7].remove('planet')
boxes[2].remove('shampoo')
boxes[7].append('shampoo')
boxes[2].append('planet')

# Put the swimsuit and the meteor and the toy into Box 9.
items_to_move = ['swimsuit', 'meteor', 'toy']
for item in items_to_move:
    boxes[9].append(item)

# Put the belt and the thread into Box 11.
items_to_move = ['belt', 'thread']
for item in items_to_move:
    boxes[11].append(item)

# Put the fridge and the mixer and the button into Box 1.
items_to_move = ['fridge', 'mixer', 'button']
for item in items_to_move:
    boxes[1].append(item)

# Move the pants and the sock from Box 1 to Box 11.
items_to_move = ['pants', 'sock']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[11].append(item)

# Remove the shampoo from Box 7.
boxes[7].remove('shampoo')

# Replace the belt and the card and the train with the keyboard and the oven and the brush in Box 5.
boxes[5].remove('belt')
boxes[5].remove('card')
boxes[5].remove('train')
boxes[5].append('keyboard')
boxes[5].append('oven')
boxes[5].append('brush')

# Put the rocket into Box 4.
boxes[4].append('rocket')

# Move the freezer from Box 7 to Box 0.
boxes[7].remove('freezer')
boxes[0].append('freezer')

# Swap the blanket in Box 2 with the thunder in Box 8.
boxes[2].remove('blanket')
boxes[8].remove('thunder')
boxes[2].append('thunder')
boxes[8].append('blanket')

# Move the cup and the candle from Box 2 to Box 5.
items_to_move = ['cup', 'candle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Remove the planet and the thunder from Box 2.
boxes[2].remove('planet')
boxes[2].remove('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")