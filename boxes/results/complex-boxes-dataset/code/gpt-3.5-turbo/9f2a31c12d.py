# Initial state of boxes
boxes = {
    0: ['doll'],
    1: ['tree', 'sun', 'flute', 'moon'],
    2: ['keyboard', 'blender', 'zipper'],
    3: ['toy', 'bear'],
    4: ['laptop', 'fish', 'horse', 'shoe', 'boat'],
    5: ['bag', 'dolphin', 'spoon', 'pan'],
    6: ['blanket'],
    7: ['speaker', 'basket', 'jungle', 'scarf'],
    8: ['phone', 'mask']
}

# Remove the blender and the keyboard and the zipper from Box 2.
items_to_remove = ['blender', 'keyboard', 'zipper']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the bag and the spoon and the dolphin from Box 5.
items_to_remove = ['bag', 'spoon', 'dolphin']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the pan from Box 5.
boxes[5].remove('pan')

# Replace the fish and the shoe and the boat with the bicycle and the grinder and the polish in Box 4.
boxes[4].remove('fish')
boxes[4].remove('shoe')
boxes[4].remove('boat')
boxes[4].append('bicycle')
boxes[4].append('grinder')
boxes[4].append('polish')

# Replace the mask with the chair in Box 8.
boxes[8].remove('mask')
boxes[8].append('chair')

# Swap the basket in Box 7 with the chair in Box 8.
boxes[7].remove('basket')
boxes[8].remove('chair')
boxes[7].append('chair')
boxes[8].append('basket')

# Put the rock and the comet and the butterfly into Box 1.
items_to_add = ['rock', 'comet', 'butterfly']
for item in items_to_add:
    boxes[1].append(item)

# Empty Box 4.
boxes[4] = []

# Replace the moon with the mirror in Box 1.
boxes[1].remove('moon')
boxes[1].append('mirror')

# Empty Box 6.
boxes[6] = []

# Replace the tree with the wig in Box 1.
boxes[1].remove('tree')
boxes[1].append('wig')

# Put the jungle and the microwave into Box 3.
boxes[3].append('jungle')
boxes[3].append('microwave')

# Replace the butterfly and the mirror with the comb and the toothbrush in Box 1.
boxes[1].remove('butterfly')
boxes[1].remove('mirror')
boxes[1].append('comb')
boxes[1].append('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")