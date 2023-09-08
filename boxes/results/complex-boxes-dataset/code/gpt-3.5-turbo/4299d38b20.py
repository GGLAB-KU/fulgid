# Initial state of boxes
boxes = {
    0: ['perfume', 'wallet', 'blender'],
    1: [],
    2: ['horse', 'mountain', 'ring'],
    3: ['skirt', 'pants', 'toothpaste', 'brush'],
    4: ['rock', 'bag', 'coin', 'game'],
    5: [],
    6: ['soap', 'gloves', 'guitar'],
    7: ['apple', 'toy'],
    8: ['ship', 'grass', 'pen', 'storm', 'rocket'],
    9: ['bicycle', 'makeup', 'console', 'sandals'],
    10: ['lion', 'frame'],
    11: []
}

# Move the apple and the toy from Box 7 to Box 0.
boxes[7].remove('apple')
boxes[7].remove('toy')
boxes[0].append('apple')
boxes[0].append('toy')

# Remove the ship and the pen from Box 8.
boxes[8].remove('ship')
boxes[8].remove('pen')

# Move the brush and the skirt and the pants from Box 3 to Box 0.
items_to_move = ['brush', 'skirt', 'pants']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Swap the soap in Box 6 with the frame in Box 10.
boxes[6].remove('soap')
boxes[10].remove('frame')
boxes[6].append('frame')
boxes[10].append('soap')

# Remove the gloves from Box 6.
boxes[6].remove('gloves')

# Put the zipper and the tiger into Box 11.
boxes[11].append('zipper')
boxes[11].append('tiger')

# Put the shoe and the table into Box 9.
boxes[9].append('shoe')
boxes[9].append('table')

# Remove the lion from Box 10.
boxes[10].remove('lion')

# Move the rocket and the grass from Box 8 to Box 10.
boxes[8].remove('rocket')
boxes[8].remove('grass')
boxes[10].append('rocket')
boxes[10].append('grass')

# Replace the horse and the ring with the sandals and the plane in Box 2.
boxes[2].remove('horse')
boxes[2].remove('ring')
boxes[2].append('sandals')
boxes[2].append('plane')

# Move the wallet and the apple from Box 0 to Box 5.
boxes[0].remove('wallet')
boxes[0].remove('apple')
boxes[5].append('wallet')
boxes[5].append('apple')

# Swap the storm in Box 8 with the apple in Box 5.
boxes[8].remove('storm')
boxes[5].remove('apple')
boxes[8].append('apple')
boxes[5].append('storm')

# Replace the guitar and the frame with the magnet and the tree in Box 6.
boxes[6].remove('guitar')
boxes[6].remove('frame')
boxes[6].append('magnet')
boxes[6].append('tree')

# Replace the grass and the soap with the pillow and the comet in Box 10.
boxes[10].remove('grass')
boxes[10].remove('soap')
boxes[10].append('pillow')
boxes[10].append('comet')

# Swap the apple in Box 8 with the console in Box 9.
boxes[8].remove('apple')
boxes[9].remove('console')
boxes[8].append('console')
boxes[9].append('apple')

# Put the towel and the lamp and the train into Box 2.
boxes[2].append('towel')
boxes[2].append('lamp')
boxes[2].append('train')

# Remove the pants from Box 0.
boxes[0].remove('pants')

# Put the sandals and the gloves into Box 5.
boxes[5].append('sandals')
boxes[5].append('gloves')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")