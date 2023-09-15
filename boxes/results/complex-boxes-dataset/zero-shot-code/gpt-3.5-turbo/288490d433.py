box_0 = ['branch', 'starfish', 'plane', 'pen', 'jungle']
box_1 = ['usb']
box_2 = ['zipper']
box_3 = ['soap', 'telescope']
box_4 = ['pan', 'paint']
box_5 = ['basket', 'shorts']
box_6 = []
box_7 = ['sock', 'toaster']
box_8 = ['seaweed', 'sun', 'table']
box_9 = []
box_10 = ['meteor', 'microscope']
box_11 = ['train', 'laptop', 'perfume', 'scarf']
box_12 = ['rocket', 'bag', 'lock', 'lightning', 'speaker']

# Swap usb in Box 1 with telescope in Box 3
box_1.remove('usb')
box_3.remove('telescope')
box_1.append('telescope')
box_3.append('usb')

# Put shorts into Box 10
box_10.append('shorts')

# Remove shorts and basket from Box 5
box_5.remove('shorts')
box_5.remove('basket')

# Put rain, ring, and desert into Box 8
box_8.extend(['rain', 'ring', 'desert'])

# Remove bag from Box 12
box_12.remove('bag')

# Move shorts and meteor from Box 10 to Box 5
box_10.remove('shorts')
box_10.remove('meteor')
box_5.append('shorts')
box_5.append('meteor')

# Remove telescope from Box 1
box_1.remove('telescope')

# Put bag, note, and boat into Box 4
box_4.extend(['bag', 'note', 'boat'])

# Put magnet, key, and cat into Box 12
box_12.extend(['magnet', 'key', 'cat'])

# Replace magnet with laptop in Box 12
box_12.remove('magnet')
box_12.append('laptop')

# Replace perfume and scarf with shorts and motorcycle in Box 11
box_11.remove('perfume')
box_11.remove('scarf')
box_11.append('shorts')
box_11.append('motorcycle')

# Put blanket and shorts into Box 4
box_4.extend(['blanket', 'shorts'])

# Replace pen, plane, and jungle with ocean, car, and console in Box 0
box_0.remove('pen')
box_0.remove('plane')
box_0.remove('jungle')
box_0.extend(['ocean', 'car', 'console'])

# Remove sun and rain from Box 8
box_8.remove('sun')
box_8.remove('rain')

# Remove speaker and lock from Box 12
box_12.remove('speaker')
box_12.remove('lock')

# Remove soap and usb from Box 3
box_3.remove('soap')
box_3.remove('usb')

# Empty Box 7
box_7.clear()

# Remove shorts and meteor from Box 5
box_5.remove('shorts')
box_5.remove('meteor')

# Move shorts and motorcycle from Box 11 to Box 0
box_11.remove('shorts')
box_11.remove('motorcycle')
box_0.append('shorts')
box_0.append('motorcycle')

# Print the contents of each box
boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")