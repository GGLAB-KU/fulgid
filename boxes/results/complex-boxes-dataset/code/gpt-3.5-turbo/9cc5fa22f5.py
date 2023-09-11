# Initial state of boxes
boxes = {
    0: ['toy', 'rain', 'cow', 'pan', 'butterfly'],
    1: ['perfume', 'necklace'],
    2: ['shoes', 'brush', 'drum'],
    3: ['plate'],
    4: [],
    5: ['moon', 'dog', 'boot', 'lion', 'mask'],
    6: [],
    7: ['belt', 'oven', 'coin', 'scissors', 'submarine'],
    8: ['octopus', 'dolphin']
}

# Swap the cow in Box 0 with the drum in Box 2.
boxes[0].remove('cow')
boxes[2].remove('drum')
boxes[0].append('drum')
boxes[2].append('cow')

# Replace the moon and the lion with the doll and the lightning in Box 5.
boxes[5].remove('moon')
boxes[5].remove('lion')
boxes[5].append('doll')
boxes[5].append('lightning')

# Swap the perfume in Box 1 with the dog in Box 5.
boxes[1].remove('perfume')
boxes[5].remove('dog')
boxes[1].append('dog')
boxes[5].append('perfume')

# Swap the brush in Box 2 with the necklace in Box 1.
boxes[2].remove('brush')
boxes[1].remove('necklace')
boxes[2].append('necklace')
boxes[1].append('brush')

# Replace the submarine with the plane in Box 7.
boxes[7].remove('submarine')
boxes[7].append('plane')

# Move the necklace and the shoes from Box 2 to Box 5.
items_to_move = ['necklace', 'shoes']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Empty Box 7.
boxes[7] = []

# Swap the boot in Box 5 with the plate in Box 3.
boxes[5].remove('boot')
boxes[3].remove('plate')
boxes[5].append('plate')
boxes[3].append('boot')

# Move the cow from Box 2 to Box 7.
boxes[2].remove('cow')
boxes[7].append('cow')

# Move the dolphin and the octopus from Box 8 to Box 2.
items_to_move = ['dolphin', 'octopus']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Remove the toy and the drum and the pan from Box 0.
items_to_remove = ['toy', 'drum', 'pan']
for item in items_to_remove:
    boxes[0].remove(item)

# Empty Box 7.
boxes[7] = []

# Move the brush from Box 1 to Box 0.
boxes[1].remove('brush')
boxes[0].append('brush')

# Move the boot from Box 3 to Box 7.
boxes[3].remove('boot')
boxes[7].append('boot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")