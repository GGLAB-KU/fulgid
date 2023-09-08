# Initial state of boxes
boxes = {
    0: ['mirror'],
    1: [],
    2: ['forest', 'meteor', 'bracelet', 'boot', 'telescope'],
    3: [],
    4: ['game', 'ring'],
    5: ['cup', 'camera', 'chair', 'shoes', 'book'],
    6: ['wire', 'towel', 'boat'],
    7: ['tape'],
    8: ['necklace'],
    9: ['thread', 'keyboard'],
    10: ['beach']
}

# Replace the tape with the button in Box 7.
boxes[7].remove('tape')
boxes[7].append('button')

# Put the cow and the tiger and the tie into Box 9.
boxes[9].extend(['cow', 'tiger', 'tie'])

# Swap the beach in Box 10 with the towel in Box 6.
boxes[10].remove('beach')
boxes[6].remove('towel')
boxes[10].append('towel')
boxes[6].append('beach')

# Swap the mirror in Box 0 with the necklace in Box 8.
boxes[0].remove('mirror')
boxes[8].remove('necklace')
boxes[0].append('necklace')
boxes[8].append('mirror')

# Replace the wire and the beach with the car and the coat in Box 6.
boxes[6].remove('wire')
boxes[6].remove('beach')
boxes[6].append('car')
boxes[6].append('coat')

# Empty Box 9.
boxes[9] = []

# Move the coat and the car and the boat from Box 6 to Box 3.
items_to_move = ['coat', 'car', 'boat']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Move the towel from Box 10 to Box 3.
boxes[10].remove('towel')
boxes[3].append('towel')

# Replace the coat and the car with the truck and the hat in Box 3.
boxes[3].remove('coat')
boxes[3].remove('car')
boxes[3].append('truck')
boxes[3].append('hat')

# Replace the boat and the truck and the towel with the needle and the lock and the ship in Box 3.
boxes[3].remove('boat')
boxes[3].remove('truck')
boxes[3].remove('towel')
boxes[3].append('needle')
boxes[3].append('lock')
boxes[3].append('ship')

# Move the cup from Box 5 to Box 10.
boxes[5].remove('cup')
boxes[10].append('cup')

# Move the necklace from Box 0 to Box 5.
boxes[0].remove('necklace')
boxes[5].append('necklace')

# Remove the game from Box 4.
boxes[4].remove('game')

# Replace the bracelet with the scissors in Box 2.
boxes[2].remove('bracelet')
boxes[2].append('scissors')

# Remove the scissors and the boot from Box 2.
boxes[2].remove('scissors')
boxes[2].remove('boot')

# Replace the button with the cup in Box 7.
boxes[7].remove('button')
boxes[7].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")