box_0 = ['ocean', 'clock', 'pen', 'umbrella']
box_1 = ['fish', 'game', 'rain', 'beach']
box_2 = ['sun', 'bowl']
box_3 = ['fridge', 'lamp', 'mixer', 'glove']
box_4 = ['bell', 'headphone', 'whistle', 'microwave', 'pan']
box_5 = ['watch', 'dolphin', 'usb']
box_6 = ['needle', 'paint', 'mask']
box_7 = ['basket', 'bird', 'speaker', 'blender', 'book']
box_8 = ['wig', 'toothbrush', 'coat', 'plate', 'polish']
box_9 = []
box_10 = []
box_11 = ['leaf', 'magnet', 'key']
box_12 = ['harmonica', 'grass', 'makeup']
box_13 = ['table', 'moon', 'brush', 'starfish']
box_14 = []

# Remove bird and speaker from Box 7
box_7.remove('bird')
box_7.remove('speaker')

# Move leaf, key, and magnet from Box 11 to Box 8
box_8.extend(box_11)
box_11.clear()

# Move paint, needle, and mask from Box 6 to Box 12
box_12.extend(box_6)
box_6.clear()

# Swap watch in Box 5 with blender in Box 7
box_5[0], box_7[3] = box_7[3], box_5[0]

# Replace pan, microwave, and whistle with bell, toy, and paint in Box 4
box_4.remove('pan')
box_4.remove('microwave')
box_4.remove('whistle')
box_4.extend(['bell', 'toy', 'paint'])

# Swap usb in Box 5 with mixer in Box 3
box_5[2], box_3[2] = box_3[2], box_5[2]

# Replace headphone, bell, and toy with bicycle, charger, and table in Box 4
box_4.remove('headphone')
box_4.remove('bell')
box_4.remove('toy')
box_4.extend(['bicycle', 'charger', 'table'])

# Move umbrella and ocean from Box 0 to Box 6
box_6.extend(box_0[:2])
box_0.remove('ocean')
box_0.remove('umbrella')

# Swap fridge in Box 3 with table in Box 13
box_3[0], box_13[0] = box_13[0], box_3[0]

# Put swimsuit, shelf, and pot into Box 8
box_8.extend(['swimsuit', 'shelf', 'pot'])

# Remove book, watch, and basket from Box 7
box_7.remove('book')
box_7.remove('watch')
box_7.remove('basket')

# Put motorcycle into Box 4
box_4.append('motorcycle')

# Replace bell, charger, and bicycle with apple, fish, and cloud in Box 4
box_4.remove('bell')
box_4.remove('charger')
box_4.remove('bicycle')
box_4.extend(['apple', 'fish', 'cloud'])

# Remove sun and bowl from Box 2
box_2.clear()

# Remove blender from Box 5
box_5.remove('blender')

# Put mixer into Box 1
box_1.append('mixer')

# Put fridge into Box 13
box_13.append('fridge')

# Swap apple in Box 4 with rain in Box 1
box_4[0], box_1[2] = box_1[2], box_4[0]

# Remove brush, moon, and starfish from Box 13
box_13.remove('brush')
box_13.remove('moon')
box_13.remove('starfish')

# Move needle from Box 12 to Box 11
box_11.append(box_12.pop(0))

# Remove ocean from Box 6
box_6.remove('ocean')

# Remove dolphin from Box 5
box_5.remove('dolphin')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")