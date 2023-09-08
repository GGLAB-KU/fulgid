# Initial state of boxes
boxes = {
    0: ['horn', 'fish'],
    1: ['brush', 'cow', 'guitar', 'coin', 'star'],
    2: ['card', 'grinder', 'basket'],
    3: ['fork', 'soap', 'bicycle', 'storm', 'cup'],
    4: ['wallet', 'plane', 'camera', 'pillow', 'toaster'],
    5: ['microwave'],
    6: ['octopus', 'sock', 'book', 'coat'],
    7: ['belt', 'car', 'violin', 'river'],
    8: ['lightning', 'pan', 'scissors'],
    9: ['meteor'],
    10: ['blender', 'telescope', 'keyboard']
}

# Swap the grinder in Box 2 with the fork in Box 3.
boxes[2].remove('grinder')
boxes[3].remove('fork')
boxes[2].append('fork')
boxes[3].append('grinder')

# Move the coin and the cow from Box 1 to Box 0.
items_to_move = ['coin', 'cow']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Replace the basket and the card and the fork with the polish and the towel and the lamp in Box 2.
boxes[2].remove('basket')
boxes[2].remove('card')
boxes[2].remove('fork')
boxes[2].append('polish')
boxes[2].append('towel')
boxes[2].append('lamp')

# Move the river and the belt and the car from Box 7 to Box 8.
items_to_move = ['river', 'belt', 'car']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[8].append(item)

# Put the apple into Box 6.
boxes[6].append('apple')

# Replace the pan with the sock in Box 8.
boxes[8].remove('pan')
boxes[8].append('sock')

# Put the doll into Box 5.
boxes[5].append('doll')

# Remove the towel from Box 2.
boxes[2].remove('towel')

# Swap the pillow in Box 4 with the keyboard in Box 10.
boxes[4].remove('pillow')
boxes[10].remove('keyboard')
boxes[4].append('keyboard')
boxes[10].append('pillow')

# Put the plane into Box 8.
boxes[8].append('plane')

# Move the cup and the grinder and the soap from Box 3 to Box 2.
items_to_move = ['cup', 'grinder', 'soap']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Replace the star and the guitar with the submarine and the shark in Box 1.
boxes[1].remove('star')
boxes[1].remove('guitar')
boxes[1].append('submarine')
boxes[1].append('shark')

# Move the coat and the apple and the book from Box 6 to Box 2.
items_to_move = ['coat', 'apple', 'book']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Remove the violin from Box 7.
boxes[7].remove('violin')

# Put the ship and the butterfly into Box 7.
boxes[7].append('ship')
boxes[7].append('butterfly')

# Move the cup and the grinder from Box 2 to Box 0.
items_to_move = ['cup', 'grinder']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")