# Initial state of boxes
boxes = {
    0: ['dice', 'shoe', 'key', 'cat'],
    1: ['polish', 'bird', 'rocket', 'camera'],
    2: ['watch', 'belt', 'leaf'],
    3: ['chair'],
    4: ['basket', 'thunder'],
    5: ['sun', 'hat'],
    6: ['shoes'],
    7: ['needle'],
    8: [],
    9: ['candle', 'horse', 'thread', 'rock', 'speaker'],
    10: ['bicycle', 'sock', 'seaweed', 'violin'],
    11: [],
    12: ['comet', 'swimsuit', 'perfume']
}

# Swap the thunder in Box 4 with the sock in Box 10.
boxes[4].remove('thunder')
boxes[10].remove('sock')
boxes[4].append('sock')
boxes[10].append('thunder')

# Remove the belt from Box 2.
boxes[2].remove('belt')

# Swap the thunder in Box 10 with the hat in Box 5.
boxes[10].remove('thunder')
boxes[5].remove('hat')
boxes[10].append('hat')
boxes[5].append('thunder')

# Move the dice and the key from Box 0 to Box 5.
items_to_move = ['dice', 'key']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Remove the bicycle and the violin and the seaweed from Box 10.
items_to_remove = ['bicycle', 'violin', 'seaweed']
for item in items_to_remove:
    boxes[10].remove(item)

# Replace the rock and the speaker and the thread with the mask and the planet and the starfish in Box 9.
boxes[9].remove('rock')
boxes[9].remove('speaker')
boxes[9].remove('thread')
boxes[9].append('mask')
boxes[9].append('planet')
boxes[9].append('starfish')

# Replace the thunder and the sun with the skirt and the chair in Box 5.
boxes[5].remove('thunder')
boxes[5].remove('sun')
boxes[5].append('skirt')
boxes[5].append('chair')

# Move the shoes from Box 6 to Box 7.
boxes[6].remove('shoes')
boxes[7].append('shoes')

# Swap the hat in Box 10 with the shoes in Box 7.
boxes[10].remove('hat')
boxes[7].remove('shoes')
boxes[10].append('shoes')
boxes[7].append('hat')

# Put the wallet and the planet and the necklace into Box 3.
items_to_move = ['wallet', 'planet', 'necklace']
for item in items_to_move:
    boxes[3].append(item)

# Move the sock and the basket from Box 4 to Box 6.
boxes[4].remove('sock')
boxes[4].remove('basket')
boxes[6].append('sock')
boxes[6].append('basket')

# Replace the planet and the mask and the horse with the laptop and the glove and the needle in Box 9.
boxes[9].remove('planet')
boxes[9].remove('mask')
boxes[9].remove('horse')
boxes[9].append('laptop')
boxes[9].append('glove')
boxes[9].append('needle')

# Empty Box 5.
boxes[5] = []

# Replace the needle and the hat with the blender and the usb in Box 7.
boxes[7].remove('needle')
boxes[7].remove('hat')
boxes[7].append('blender')
boxes[7].append('usb')

# Replace the candle and the needle and the starfish with the plate and the frame and the river in Box 9.
boxes[9].remove('candle')
boxes[9].remove('needle')
boxes[9].remove('starfish')
boxes[9].append('plate')
boxes[9].append('frame')
boxes[9].append('river')

# Remove the blender and the usb from Box 7.
boxes[7].remove('blender')
boxes[7].remove('usb')

# Move the camera from Box 1 to Box 5.
boxes[1].remove('camera')
boxes[5].append('camera')

# Put the controller and the headphone into Box 6.
items_to_move = ['controller', 'headphone']
for item in items_to_move:
    boxes[6].append(item)

# Replace the camera with the charger in Box 5.
boxes[5].remove('camera')
boxes[5].append('charger')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")