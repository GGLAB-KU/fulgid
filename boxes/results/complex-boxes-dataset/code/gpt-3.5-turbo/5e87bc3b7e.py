# Initial state of boxes
boxes = {
    0: ['cow', 'desert', 'book', 'storm', 'razor'],
    1: ['mountain', 'earring', 'pot', 'lamp', 'mixer'],
    2: ['moon', 'plane', 'puzzle', 'toy', 'phone'],
    3: ['camera', 'river', 'horse', 'doll', 'bicycle'],
    4: ['pants', 'whistle', 'bracelet', 'harmonica', 'shoes'],
    5: ['card', 'cloud', 'comb', 'jacket', 'bus'],
    6: ['microwave', 'shirt'],
    7: ['bear', 'basket', 'lightning', 'chair'],
    8: ['truck', 'keyboard'],
    9: [],
    10: [],
    11: ['blanket', 'spoon'],
    12: ['scarf', 'submarine', 'soap', 'pan', 'lipstick']
}

# Replace the pants and the harmonica and the shoes with the pen and the fish and the motorcycle in Box 4.
boxes[4].remove('pants')
boxes[4].remove('harmonica')
boxes[4].remove('shoes')
boxes[4].append('pen')
boxes[4].append('fish')
boxes[4].append('motorcycle')

# Swap the submarine in Box 12 with the spoon in Box 11.
boxes[12].remove('submarine')
boxes[11].remove('spoon')
boxes[12].append('spoon')
boxes[11].append('submarine')

# Replace the book and the cow with the umbrella and the coat in Box 0.
boxes[0].remove('book')
boxes[0].remove('cow')
boxes[0].append('umbrella')
boxes[0].append('coat')

# Remove the horse and the river from Box 3.
boxes[3].remove('horse')
boxes[3].remove('river')

# Replace the pen with the tiger in Box 4.
boxes[4].remove('pen')
boxes[4].append('tiger')

# Put the telescope and the sculpture into Box 6.
boxes[6].append('telescope')
boxes[6].append('sculpture')

# Remove the truck and the keyboard from Box 8.
boxes[8].remove('truck')
boxes[8].remove('keyboard')

# Replace the mountain and the earring with the camera and the polish in Box 1.
boxes[1].remove('mountain')
boxes[1].remove('earring')
boxes[1].append('camera')
boxes[1].append('polish')

# Move the shirt and the microwave and the sculpture from Box 6 to Box 9.
items_to_move = ['shirt', 'microwave', 'sculpture']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[9].append(item)

# Move the jacket and the cloud and the card from Box 5 to Box 2.
items_to_move = ['jacket', 'cloud', 'card']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Put the tape into Box 1.
boxes[1].append('tape')

# Remove the lightning from Box 7.
boxes[7].remove('lightning')

# Move the telescope from Box 6 to Box 5.
boxes[6].remove('telescope')
boxes[5].append('telescope')

# Remove the bicycle from Box 3.
boxes[3].remove('bicycle')

# Move the fish from Box 4 to Box 5.
boxes[4].remove('fish')
boxes[5].append('fish')

# Put the boot and the game into Box 7.
boxes[7].append('boot')
boxes[7].append('game')

# Remove the fish and the bus and the telescope from Box 5.
items_to_remove = ['fish', 'bus', 'telescope']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the camera from Box 3 to Box 6.
boxes[3].remove('camera')
boxes[6].append('camera')

# Put the telescope and the planet into Box 0.
boxes[0].append('telescope')
boxes[0].append('planet')

# Put the game into Box 5.
boxes[5].append('game')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")