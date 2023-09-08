# Initial state of boxes
boxes = {
    0: ['lightning', 'lipstick', 'harmonica', 'cup'],
    1: ['submarine', 'jungle', 'train', 'comet', 'microwave'],
    2: ['shorts', 'doll'],
    3: ['gloves', 'tie', 'sun'],
    4: ['toothbrush', 'vase', 'sculpture'],
    5: ['laptop', 'crown', 'moon', 'bell'],
    6: ['watch', 'book', 'snow', 'cat', 'storm'],
    7: ['blender'],
    8: ['starfish', 'basket', 'skirt', 'camera'],
    9: ['button', 'fork', 'bear', 'horn', 'tape'],
    10: ['paint', 'cow', 'river', 'battery']
}

# Remove the gloves and the tie and the sun from Box 3.
boxes[3].remove('gloves')
boxes[3].remove('tie')
boxes[3].remove('sun')

# Put the oven and the island into Box 2.
boxes[2].append('oven')
boxes[2].append('island')

# Replace the lightning with the train in Box 0.
boxes[0].remove('lightning')
boxes[0].append('train')

# Move the river and the paint and the cow from Box 10 to Box 8.
items_to_move = ['river', 'paint', 'cow']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Remove the blender from Box 7.
boxes[7].remove('blender')

# Swap the cup in Box 0 with the paint in Box 8.
boxes[0].remove('cup')
boxes[8].remove('paint')
boxes[0].append('paint')
boxes[8].append('cup')

# Swap the horn in Box 9 with the paint in Box 0.
boxes[9].remove('horn')
boxes[0].remove('paint')
boxes[9].append('paint')
boxes[0].append('horn')

# Put the telescope into Box 0.
boxes[0].append('telescope')

# Put the doll into Box 9.
boxes[2].remove('doll')
boxes[9].append('doll')

# Put the boot and the butterfly into Box 0.
boxes[0].append('boot')
boxes[0].append('butterfly')

# Put the toaster into Box 0.
boxes[0].append('toaster')

# Put the chair and the comb into Box 8.
boxes[8].append('chair')
boxes[8].append('comb')

# Put the leaf and the bowl into Box 9.
boxes[9].append('leaf')
boxes[9].append('bowl')

# Replace the bell and the crown and the laptop with the thread and the razor and the train in Box 5.
boxes[5].remove('bell')
boxes[5].remove('crown')
boxes[5].remove('laptop')
boxes[5].append('thread')
boxes[5].append('razor')
boxes[5].append('train')

# Swap the doll in Box 2 with the toothbrush in Box 4.
boxes[2].remove('doll')
boxes[4].remove('toothbrush')
boxes[2].append('toothbrush')
boxes[4].append('doll')

# Move the watch and the book from Box 6 to Box 3.
boxes[6].remove('watch')
boxes[6].remove('book')
boxes[3].append('watch')
boxes[3].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")