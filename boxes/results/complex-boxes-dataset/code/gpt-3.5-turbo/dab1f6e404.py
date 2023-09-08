# Initial state of boxes
boxes = {
    0: ['lion', 'frame', 'chair'],
    1: ['brush', 'usb'],
    2: [],
    3: ['toothbrush', 'planet', 'puzzle', 'belt', 'grinder'],
    4: ['cup', 'coin', 'crown', 'button'],
    5: ['dice', 'game'],
    6: [],
    7: ['phone', 'thunder', 'mountain'],
    8: [],
    9: ['shirt', 'blanket', 'shelf', 'comb', 'rain'],
    10: ['butterfly', 'storm', 'doll', 'controller'],
    11: ['grass', 'piano', 'rock']
}

# Move the butterfly and the storm and the doll from Box 10 to Box 6.
items_to_move = ['butterfly', 'storm', 'doll']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[6].append(item)

# Move the shirt and the comb from Box 9 to Box 6.
items_to_move = ['shirt', 'comb']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[6].append(item)

# Remove the grinder from Box 3.
boxes[3].remove('grinder')

# Put the meteor into Box 9.
boxes[9].append('meteor')

# Move the piano from Box 11 to Box 10.
boxes[11].remove('piano')
boxes[10].append('piano')

# Put the earring and the thread into Box 9.
boxes[9].append('earring')
boxes[9].append('thread')

# Remove the piano from Box 10.
boxes[10].remove('piano')

# Move the button and the cup and the coin from Box 4 to Box 2.
items_to_move = ['button', 'cup', 'coin']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the controller from Box 10 to Box 8.
boxes[10].remove('controller')
boxes[8].append('controller')

# Swap the game in Box 5 with the rock in Box 11.
boxes[5].remove('game')
boxes[11].remove('rock')
boxes[5].append('rock')
boxes[11].append('game')

# Remove the grass from Box 11.
boxes[11].remove('grass')

# Move the button from Box 2 to Box 10.
boxes[2].remove('button')
boxes[10].append('button')

# Replace the usb and the brush with the needle and the shampoo in Box 1.
boxes[1].remove('usb')
boxes[1].remove('brush')
boxes[1].append('needle')
boxes[1].append('shampoo')

# Remove the frame and the chair from Box 0.
boxes[0].remove('frame')
boxes[0].remove('chair')

# Swap the button in Box 10 with the shirt in Box 6.
boxes[10].remove('button')
boxes[6].remove('shirt')
boxes[10].append('shirt')
boxes[6].append('button')

# Move the rain and the blanket and the meteor from Box 9 to Box 1.
items_to_move = ['rain', 'blanket', 'meteor']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Put the mirror into Box 2.
boxes[2].append('mirror')

# Move the game from Box 11 to Box 2.
boxes[11].remove('game')
boxes[2].append('game')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")