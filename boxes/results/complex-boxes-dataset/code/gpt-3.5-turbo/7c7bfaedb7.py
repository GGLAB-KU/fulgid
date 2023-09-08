# Initial state of boxes
boxes = {
    0: ['brush', 'bicycle', 'starfish'],
    1: ['crown', 'shark', 'mirror', 'button'],
    2: [],
    3: ['zipper', 'plane'],
    4: ['needle', 'shoes', 'cow', 'octopus'],
    5: ['ring', 'comb', 'gloves', 'spoon'],
    6: ['polish', 'pants', 'laptop'],
    7: ['scissors', 'flute', 'watch', 'drum'],
    8: [],
    9: ['vase', 'necklace', 'microscope']
}

# Remove the bicycle from Box 0.
boxes[0].remove('bicycle')

# Move the comb and the gloves and the spoon from Box 5 to Box 7.
items_to_move = ['comb', 'gloves', 'spoon']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Move the laptop and the pants and the polish from Box 6 to Box 3.
items_to_move = ['laptop', 'pants', 'polish']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Swap the pants in Box 3 with the comb in Box 7.
boxes[3].remove('pants')
boxes[7].remove('comb')
boxes[3].append('comb')
boxes[7].append('pants')

# Put the towel and the harmonica into Box 8.
boxes[8].append('towel')
boxes[8].append('harmonica')

# Move the harmonica from Box 8 to Box 4.
boxes[8].remove('harmonica')
boxes[4].append('harmonica')

# Put the train into Box 4.
boxes[4].append('train')

# Move the starfish and the brush from Box 0 to Box 4.
items_to_move = ['starfish', 'brush']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the soap into Box 6.
boxes[6].append('soap')

# Move the polish and the zipper from Box 3 to Box 6.
boxes[3].remove('polish')
boxes[3].remove('zipper')
boxes[6].append('polish')
boxes[6].append('zipper')

# Remove the comb and the laptop and the plane from Box 3.
items_to_remove = ['comb', 'laptop', 'plane']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the crown in Box 1 with the vase in Box 9.
boxes[1].remove('crown')
boxes[9].remove('vase')
boxes[1].append('vase')
boxes[9].append('crown')

# Replace the microscope and the crown and the necklace with the rocket and the bear and the boot in Box 9.
boxes[9].remove('microscope')
boxes[9].remove('crown')
boxes[9].remove('necklace')
boxes[9].append('rocket')
boxes[9].append('bear')
boxes[9].append('boot')

# Move the ring from Box 5 to Box 4.
boxes[5].remove('ring')
boxes[4].append('ring')

# Remove the vase from Box 1.
boxes[1].remove('vase')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")