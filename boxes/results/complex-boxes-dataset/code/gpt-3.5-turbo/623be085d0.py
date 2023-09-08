# Initial state of boxes
boxes = {
    0: ['zipper'],
    1: ['toaster', 'starfish', 'needle', 'shoes', 'boat'],
    2: [],
    3: ['whistle', 'key', 'helmet', 'basket'],
    4: ['razor', 'mask', 'comet'],
    5: [],
    6: [],
    7: ['earring', 'thunder', 'necklace', 'sock'],
    8: ['brush', 'moon'],
    9: ['grinder', 'microwave', 'magnet', 'river', 'perfume']
}

# Remove the magnet and the perfume from Box 9.
boxes[9].remove('magnet')
boxes[9].remove('perfume')

# Remove the zipper from Box 0.
boxes[0].remove('zipper')

# Put the skirt and the magnet and the pillow into Box 7.
boxes[7].append('skirt')
boxes[7].append('magnet')
boxes[7].append('pillow')

# Replace the starfish and the needle and the toaster with the phone and the tree and the vase in Box 1.
boxes[1].remove('starfish')
boxes[1].remove('needle')
boxes[1].remove('toaster')
boxes[1].append('phone')
boxes[1].append('tree')
boxes[1].append('vase')

# Swap the brush in Box 8 with the razor in Box 4.
boxes[8].remove('brush')
boxes[4].remove('razor')
boxes[8].append('razor')
boxes[4].append('brush')

# Move the comet and the brush from Box 4 to Box 6.
boxes[4].remove('comet')
boxes[4].remove('brush')
boxes[6].append('comet')
boxes[6].append('brush')

# Put the bicycle and the plane into Box 8.
boxes[8].append('bicycle')
boxes[8].append('plane')

# Move the comet and the brush from Box 6 to Box 8.
boxes[6].remove('comet')
boxes[6].remove('brush')
boxes[8].append('comet')
boxes[8].append('brush')

# Swap the skirt in Box 7 with the brush in Box 8.
boxes[7].remove('skirt')
boxes[8].remove('brush')
boxes[7].append('brush')
boxes[8].append('skirt')

# Swap the mask in Box 4 with the tree in Box 1.
boxes[4].remove('mask')
boxes[1].remove('tree')
boxes[4].append('tree')
boxes[1].append('mask')

# Move the river and the grinder and the microwave from Box 9 to Box 2.
items_to_move = ['river', 'grinder', 'microwave']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[2].append(item)

# Replace the key and the whistle with the plane and the blender in Box 3.
boxes[3].remove('key')
boxes[3].remove('whistle')
boxes[3].append('plane')
boxes[3].append('blender')

# Swap the skirt in Box 8 with the helmet in Box 3.
boxes[8].remove('skirt')
boxes[3].remove('helmet')
boxes[8].append('helmet')
boxes[3].append('skirt')

# Swap the sock in Box 7 with the grinder in Box 2.
boxes[7].remove('sock')
boxes[2].remove('grinder')
boxes[7].append('grinder')
boxes[2].append('sock')

# Replace the tree with the makeup in Box 4.
boxes[4].remove('tree')
boxes[4].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")