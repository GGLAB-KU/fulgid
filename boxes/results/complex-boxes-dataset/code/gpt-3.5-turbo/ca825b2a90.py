# Initial state of boxes
boxes = {
    0: ['doll', 'swimsuit', 'shoes', 'lion', 'tie'],
    1: ['microwave', 'pillow'],
    2: ['mountain', 'card', 'lamp'],
    3: ['bracelet', 'puzzle'],
    4: ['dress'],
    5: ['phone'],
    6: ['river', 'whistle', 'drum', 'seaweed', 'apple'],
    7: ['polish', 'pan']
}

# Swap the phone in Box 5 with the lion in Box 0.
boxes[0].remove('lion')
boxes[5].remove('phone')
boxes[0].append('phone')
boxes[5].append('lion')

# Move the phone and the doll and the shoes from Box 0 to Box 5.
items_to_move = ['phone', 'doll', 'shoes']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Remove the shoes and the lion and the phone from Box 5.
items_to_remove = ['shoes', 'lion', 'phone']
for item in items_to_remove:
    boxes[5].remove(item)

# Put the car and the shoe and the forest into Box 7.
items_to_add = ['car', 'shoe', 'forest']
for item in items_to_add:
    boxes[7].append(item)

# Replace the microwave and the pillow with the ship and the mixer in Box 1.
boxes[1].remove('microwave')
boxes[1].remove('pillow')
boxes[1].append('ship')
boxes[1].append('mixer')

# Move the mountain and the lamp and the card from Box 2 to Box 0.
items_to_move = ['mountain', 'lamp', 'card']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Swap the mountain in Box 0 with the mixer in Box 1.
boxes[0].remove('mountain')
boxes[1].remove('mixer')
boxes[0].append('mixer')
boxes[1].append('mountain')

# Swap the pan in Box 7 with the drum in Box 6.
boxes[7].remove('pan')
boxes[6].remove('drum')
boxes[7].append('drum')
boxes[6].append('pan')

# Put the skirt and the harmonica into Box 4.
items_to_add = ['skirt', 'harmonica']
for item in items_to_add:
    boxes[4].append(item)

# Put the sun into Box 4.
boxes[4].append('sun')

# Swap the dress in Box 4 with the doll in Box 5.
boxes[4].remove('dress')
boxes[5].remove('doll')
boxes[4].append('doll')
boxes[5].append('dress')

# Remove the ship and the mountain from Box 1.
items_to_remove = ['ship', 'mountain']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")