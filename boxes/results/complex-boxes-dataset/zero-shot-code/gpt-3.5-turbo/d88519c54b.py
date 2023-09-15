box_0 = ['perfume', 'jacket', 'hat', 'polish', 'plate']
box_1 = []
box_2 = ['desert', 'plane', 'headphone']
box_3 = ['flute', 'thread', 'pillow', 'bag', 'card']
box_4 = ['crown', 'coin', 'chair', 'razor', 'laptop']
box_5 = []
box_6 = ['pot', 'brush', 'helmet', 'shirt']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)

# Put the magnet into Box 4
box_4.append('magnet')

# Put the tie into Box 2
box_2.append('tie')

# Swap the laptop in Box 4 with the polish in Box 0
box_0.remove('polish')
box_4.remove('laptop')
box_0.append('laptop')
box_4.append('polish')

# Put the key and the moon and the piano into Box 0
box_0.extend(['key', 'moon', 'piano'])

# Remove the helmet and the shirt from Box 6
box_6.remove('helmet')
box_6.remove('shirt')

# Swap the pot in Box 6 with the bag in Box 3
box_3.remove('bag')
box_6.remove('pot')
box_3.append('pot')
box_6.append('bag')

# Move the desert and the plane and the tie from Box 2 to Box 1
box_2.remove('desert')
box_2.remove('plane')
box_2.remove('tie')
box_1.extend(['desert', 'plane', 'tie'])

# Replace the chair and the magnet with the cup and the telescope in Box 4
box_4.remove('chair')
box_4.remove('magnet')
box_4.append('cup')
box_4.append('telescope')

# Move the polish from Box 4 to Box 1
box_4.remove('polish')
box_1.append('polish')

# Move the flute from Box 3 to Box 2
box_3.remove('flute')
box_2.append('flute')

# Replace the telescope with the mixer in Box 4
box_4.remove('telescope')
box_4.append('mixer')

# Print the final state of the boxes
print_boxes()