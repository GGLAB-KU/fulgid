# Initial state of boxes
boxes = {
    0: [],
    1: ['cloud', 'button', 'crown', 'ship', 'chair'],
    2: ['sun', 'puzzle'],
    3: ['moon'],
    4: [],
    5: ['tape'],
    6: [],
    7: ['rain', 'card'],
    8: ['cup', 'charger', 'butterfly', 'towel'],
    9: ['bowl', 'pot', 'seaweed', 'brush', 'dolphin'],
    10: []
}

# Put the drum and the razor and the branch into Box 5.
boxes[5].extend(['drum', 'razor', 'branch'])

# Remove the moon from Box 3.
boxes[3].remove('moon')

# Put the crown and the starfish and the mountain into Box 2.
boxes[2].extend(['crown', 'starfish', 'mountain'])

# Replace the rain and the card with the watch and the pot in Box 7.
boxes[7].remove('rain')
boxes[7].remove('card')
boxes[7].extend(['watch', 'pot'])

# Move the button and the ship from Box 1 to Box 2.
items_to_move = ['button', 'ship']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the perfume into Box 10.
boxes[10].append('perfume')

# Remove the tape and the branch and the razor from Box 5.
items_to_remove = ['tape', 'branch', 'razor']
for item in items_to_remove:
    boxes[5].remove(item)

# Put the mixer and the necklace into Box 8.
boxes[8].extend(['mixer', 'necklace'])

# Swap the bowl in Box 9 with the pot in Box 7.
boxes[9].remove('bowl')
boxes[7].remove('pot')
boxes[9].append('pot')
boxes[7].append('bowl')

# Replace the chair and the crown and the cloud with the dice and the rock and the note in Box 1.
boxes[1].remove('chair')
boxes[1].remove('crown')
boxes[1].remove('cloud')
boxes[1].extend(['dice', 'rock', 'note'])

# Swap the ship in Box 2 with the dolphin in Box 9.
boxes[2].remove('ship')
boxes[9].remove('dolphin')
boxes[2].append('dolphin')
boxes[9].append('ship')

# Remove the note and the rock from Box 1.
boxes[1].remove('note')
boxes[1].remove('rock')

# Put the glove and the laptop into Box 6.
boxes[6].extend(['glove', 'laptop'])

# Move the necklace and the cup and the charger from Box 8 to Box 9.
items_to_move = ['necklace', 'cup', 'charger']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[9].append(item)

# Replace the laptop and the glove with the lion and the makeup in Box 6.
boxes[6].remove('laptop')
boxes[6].remove('glove')
boxes[6].extend(['lion', 'makeup'])

# Swap the makeup in Box 6 with the puzzle in Box 2.
boxes[6].remove('makeup')
boxes[2].remove('puzzle')
boxes[6].append('puzzle')
boxes[2].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")