box_0 = ['thunder', 'shark', 'needle', 'pen', 'truck']
box_1 = ['scissors', 'earring', 'lamp']
box_2 = ['lion', 'frame']
box_3 = ['pan', 'forest', 'watch', 'flute']
box_4 = ['helmet', 'car']
box_5 = ['comb', 'gloves', 'telescope', 'ring', 'horn']
box_6 = ['tiger', 'battery']
box_7 = []
box_8 = ['storm', 'plane', 'coat']
box_9 = ['starfish', 'jacket', 'motorcycle']
box_10 = ['elephant', 'cat', 'thread']
box_11 = []
box_12 = ['lightning', 'octopus', 'flower', 'mountain', 'apple']
box_13 = ['piano', 'clock', 'mirror', 'seaweed']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Put the book and the drum and the mixer into Box 3
box_3.extend(['book', 'drum', 'mixer'])
print_box(3, box_3)

# Put the polish and the ring into Box 10
box_10.extend(['polish', 'ring'])
print_box(10, box_10)

# Remove the scissors from Box 1
box_1.remove('scissors')
print_box(1, box_1)

# Remove the apple from Box 12
box_12.remove('apple')
print_box(12, box_12)

# Remove the frame from Box 2
box_2.remove('frame')
print_box(2, box_2)

# Swap the car in Box 4 with the octopus in Box 12
box_4.remove('car')
box_12.remove('octopus')
box_4.append('octopus')
box_12.append('car')
print_box(4, box_4)
print_box(12, box_12)

# Remove the coat and the storm from Box 8
box_8.remove('coat')
box_8.remove('storm')
print_box(8, box_8)

# Put the ocean and the bus and the necklace into Box 9
box_9.extend(['ocean', 'bus', 'necklace'])
print_box(9, box_9)

# Remove the lamp and the earring from Box 1
box_1.remove('lamp')
box_1.remove('earring')
print_box(1, box_1)

# Put the octopus and the motorcycle into Box 10
box_10.extend(['octopus', 'motorcycle'])
print_box(10, box_10)

# Replace the plane with the cloud in Box 8
box_8.remove('plane')
box_8.append('cloud')
print_box(8, box_8)

# Put the brush into Box 3
box_3.append('brush')
print_box(3, box_3)

# Move the gloves and the horn from Box 5 to Box 2
box_5.remove('gloves')
box_5.remove('horn')
box_2.extend(['gloves', 'horn'])
print_box(5, box_5)
print_box(2, box_2)

# Swap the lion in Box 2 with the tiger in Box 6
box_2.remove('lion')
box_6.remove('tiger')
box_2.append('tiger')
box_6.append('lion')
print_box(2, box_2)
print_box(6, box_6)

# Move the ring from Box 10 to Box 1
box_10.remove('ring')
box_1.append('ring')
print_box(10, box_10)
print_box(1, box_1)

# Remove the ring from Box 1
box_1.remove('ring')
print_box(1, box_1)

# Replace the mountain with the pot in Box 12
box_12.remove('mountain')
box_12.append('pot')
print_box(12, box_12)

# Remove the lightning and the flower from Box 12
box_12.remove('lightning')
box_12.remove('flower')
print_box(12, box_12)

# Move the flute and the brush from Box 3 to Box 4
box_3.remove('flute')
box_3.remove('brush')
box_4.extend(['flute', 'brush'])
print_box(3, box_3)
print_box(4, box_4)

# Remove the mixer and the watch and the book from Box 3
box_3.remove('mixer')
box_3.remove('watch')
box_3.remove('book')
print_box(3, box_3)

# Put the butterfly and the microwave into Box 9
box_9.extend(['butterfly', 'microwave'])
print_box(9, box_9)