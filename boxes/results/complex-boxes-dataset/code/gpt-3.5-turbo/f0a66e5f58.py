# Initial state of boxes
boxes = {
    0: ['octopus', 'paint', 'lipstick'],
    1: ['sun', 'charger', 'console', 'boat', 'basket'],
    2: ['drum', 'zipper'],
    3: ['tie', 'shoe', 'mixer', 'jungle'],
    4: ['snow', 'telescope', 'car', 'bowl', 'comet'],
    5: ['horse', 'necklace', 'puzzle', 'cat'],
    6: ['desert', 'glove'],
    7: ['swimsuit'],
    8: []
}

# Remove the basket and the sun and the console from Box 1.
items_to_remove = ['basket', 'sun', 'console']
for item in items_to_remove:
    boxes[1].remove(item)

# Put the polish and the tape into Box 0.
boxes[0].append('polish')
boxes[0].append('tape')

# Remove the swimsuit from Box 7.
boxes[7].remove('swimsuit')

# Remove the glove from Box 6.
boxes[6].remove('glove')

# Remove the charger and the boat from Box 1.
boxes[1].remove('charger')
boxes[1].remove('boat')

# Replace the comet and the bowl with the rain and the shark in Box 4.
boxes[4].remove('comet')
boxes[4].remove('bowl')
boxes[4].append('rain')
boxes[4].append('shark')

# Remove the drum from Box 2.
boxes[2].remove('drum')

# Swap the desert in Box 6 with the cat in Box 5.
boxes[6], boxes[5] = boxes[5], boxes[6]

# Empty Box 2.
boxes[2] = []

# Put the truck into Box 5.
boxes[5].append('truck')

# Put the lightning and the controller into Box 1.
boxes[1].append('lightning')
boxes[1].append('controller')

# Remove the desert from Box 6.
boxes[6].remove('desert')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")