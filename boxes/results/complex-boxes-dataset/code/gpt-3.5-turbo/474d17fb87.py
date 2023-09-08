# Initial state of boxes
boxes = {
    0: ['sock', 'lipstick', 'speaker', 'shoes'],
    1: ['pan', 'basket', 'violin', 'rock'],
    2: ['umbrella', 'microscope', 'jacket'],
    3: ['telescope', 'usb', 'pot', 'harmonica'],
    4: ['phone', 'makeup', 'sandals', 'oven', 'bracelet'],
    5: ['comet'],
    6: ['butterfly', 'cup', 'starfish', 'dice', 'skirt'],
    7: ['seaweed', 'desert', 'island', 'laptop'],
    8: ['moon', 'wallet', 'truck', 'tree', 'rain'],
    9: ['submarine', 'drum', 'boat'],
    10: ['shampoo', 'plane', 'brush', 'game', 'perfume'],
    11: ['lock', 'coin', 'storm'],
    12: [],
    13: ['helmet', 'comb', 'apple', 'elephant'],
    14: ['thread', 'polish', 'bag']
}

# Remove the starfish and the cup from Box 6.
boxes[6].remove('starfish')
boxes[6].remove('cup')

# Remove the harmonica and the telescope from Box 3.
boxes[3].remove('harmonica')
boxes[3].remove('telescope')

# Remove the apple and the comb from Box 13.
boxes[13].remove('apple')
boxes[13].remove('comb')

# Remove the shampoo and the perfume and the plane from Box 10.
boxes[10].remove('shampoo')
boxes[10].remove('perfume')
boxes[10].remove('plane')

# Swap the polish in Box 14 with the umbrella in Box 2.
boxes[14].remove('polish')
boxes[2].remove('umbrella')
boxes[14].append('umbrella')
boxes[2].append('polish')

# Move the usb from Box 3 to Box 2.
boxes[3].remove('usb')
boxes[2].append('usb')

# Swap the shoes in Box 0 with the desert in Box 7.
boxes[0].remove('shoes')
boxes[7].remove('desert')
boxes[0].append('desert')
boxes[7].append('shoes')

# Remove the butterfly and the skirt and the dice from Box 6.
boxes[6].remove('butterfly')
boxes[6].remove('skirt')
boxes[6].remove('dice')

# Swap the drum in Box 9 with the microscope in Box 2.
boxes[9].remove('drum')
boxes[2].remove('microscope')
boxes[9].append('microscope')
boxes[2].append('drum')

# Replace the pot with the scarf in Box 3.
boxes[3].remove('pot')
boxes[3].append('scarf')

# Put the boot and the blender and the bowl into Box 5.
items_to_put = ['boot', 'blender', 'bowl']
for item in items_to_put:
    boxes[5].append(item)

# Remove the basket and the rock from Box 1.
boxes[1].remove('basket')
boxes[1].remove('rock')

# Replace the lipstick with the glasses in Box 0.
boxes[0].remove('lipstick')
boxes[0].append('glasses')

# Swap the thread in Box 14 with the tree in Box 8.
boxes[14].remove('thread')
boxes[8].remove('tree')
boxes[14].append('tree')
boxes[8].append('thread')

# Move the drum and the jacket and the polish from Box 2 to Box 1.
items_to_move = ['drum', 'jacket', 'polish']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Remove the bag and the umbrella and the tree from Box 14.
boxes[14].remove('bag')
boxes[14].remove('umbrella')
boxes[14].remove('tree')

# Move the scarf from Box 3 to Box 5.
boxes[3].remove('scarf')
boxes[5].append('scarf')

# Put the ocean and the glove and the necklace into Box 1.
items_to_put = ['ocean', 'glove', 'necklace']
for item in items_to_put:
    boxes[1].append(item)

# Remove the game and the brush from Box 10.
boxes[10].remove('game')
boxes[10].remove('brush')

# Replace the submarine with the lipstick in Box 9.
boxes[9].remove('submarine')
boxes[9].append('lipstick')

# Put the charger into Box 6.
boxes[6].append('charger')

# Put the bag and the bird and the moon into Box 14.
items_to_put = ['bag', 'bird', 'moon']
for item in items_to_put:
    boxes[14].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")