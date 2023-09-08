# Initial state of boxes
boxes = {
    0: ['tree', 'vase', 'puzzle', 'rocket', 'starfish'],
    1: ['toothpaste', 'lock', 'ship', 'toaster', 'cloud'],
    2: ['shirt', 'bracelet', 'sculpture', 'camera'],
    3: ['bicycle', 'motorcycle', 'clock', 'wire', 'key'],
    4: ['doll', 'dolphin', 'button', 'spoon'],
    5: ['sock', 'game', 'candle', 'tape'],
    6: ['storm', 'needle', 'plane'],
    7: ['headphone', 'blanket', 'perfume', 'thread', 'horse'],
    8: ['shoes', 'violin', 'freezer', 'hat', 'submarine'],
    9: ['branch', 'rock', 'star', 'boot']
}

# Replace the rock and the star with the watch and the fridge in Box 9.
boxes[9].remove('rock')
boxes[9].remove('star')
boxes[9].append('watch')
boxes[9].append('fridge')

# Remove the shoes from Box 8.
boxes[8].remove('shoes')

# Replace the puzzle and the rocket with the magnet and the cow in Box 0.
boxes[0].remove('puzzle')
boxes[0].remove('rocket')
boxes[0].append('magnet')
boxes[0].append('cow')

# Remove the camera from Box 2.
boxes[2].remove('camera')

# Move the ship and the toothpaste and the toaster from Box 1 to Box 7.
items_to_move = ['ship', 'toothpaste', 'toaster']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[7].append(item)

# Move the tape and the candle and the sock from Box 5 to Box 8.
items_to_move = ['tape', 'candle', 'sock']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Remove the button from Box 4.
boxes[4].remove('button')

# Swap the needle in Box 6 with the dolphin in Box 4.
boxes[6].remove('needle')
boxes[4].remove('dolphin')
boxes[6].append('dolphin')
boxes[4].append('needle')

# Remove the sock from Box 8.
boxes[8].remove('sock')

# Replace the hat and the violin and the candle with the comet and the bear and the towel in Box 8.
boxes[8].remove('hat')
boxes[8].remove('violin')
boxes[8].remove('candle')
boxes[8].append('comet')
boxes[8].append('bear')
boxes[8].append('towel')

# Remove the game from Box 5.
boxes[5].remove('game')

# Move the comet and the bear and the freezer from Box 8 to Box 7.
items_to_move = ['comet', 'bear', 'freezer']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Remove the bracelet from Box 2.
boxes[2].remove('bracelet')

# Swap the shirt in Box 2 with the wire in Box 3.
boxes[2].remove('shirt')
boxes[3].remove('wire')
boxes[2].append('wire')
boxes[3].append('shirt')

# Put the pillow and the wig and the usb into Box 8.
items_to_put = ['pillow', 'wig', 'usb']
for item in items_to_put:
    boxes[8].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")