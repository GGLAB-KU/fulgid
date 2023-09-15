box_0 = ['boot', 'branch', 'pillow', 'wallet']
box_1 = ['wig']
box_2 = ['river', 'usb', 'drum', 'scarf']
box_3 = ['submarine', 'mirror']
box_4 = ['speaker']
box_5 = ['card', 'lipstick']
box_6 = ['moon', 'console', 'microwave', 'meteor', 'bear']
box_7 = ['phone', 'shoe', 'charger']
box_8 = []
box_9 = ['keyboard', 'swimsuit', 'bowl', 'rain', 'magnet']
box_10 = []
box_11 = ['microscope', 'glasses', 'tape', 'thunder']
box_12 = ['crown', 'mountain', 'toothpaste']

# Swap the wig in Box 1 with the speaker in Box 4
box_1[0], box_4[0] = box_4[0], box_1[0]

# Move the boot and the pillow from Box 0 to Box 4
box_4.extend([box_0.pop(0), box_0.pop(0)])

# Put the pen into Box 12
box_12.append('pen')

# Remove the bear from Box 6
box_6.remove('bear')

# Move the wallet from Box 0 to Box 1
box_1.append(box_0.pop(2))

# Remove the lipstick and the card from Box 5
box_5.remove('lipstick')
box_5.remove('card')

# Remove the wig and the boot from Box 4
box_4.remove('wig')
box_4.remove('boot')

# Replace the crown and the toothpaste and the mountain with the keyboard and the train and the game in Box 12
box_12.extend(['keyboard', 'train', 'game'])
box_12.remove('crown')
box_12.remove('toothpaste')
box_12.remove('mountain')

# Move the meteor from Box 6 to Box 12
box_12.append(box_6.pop(3))

# Remove the glasses and the microscope and the thunder from Box 11
box_11.remove('glasses')
box_11.remove('microscope')
box_11.remove('thunder')

# Remove the branch from Box 0
box_0.remove('branch')

# Put the perfume and the thread into Box 11
box_11.extend(['perfume', 'thread'])

# Swap the scarf in Box 2 with the tape in Box 11
box_2[2], box_11[2] = box_11[2], box_2[2]

# Move the shoe and the charger and the phone from Box 7 to Box 9
box_9.extend([box_7.pop(1), box_7.pop(1), box_7.pop(0)])

# Remove the mirror and the submarine from Box 3
box_3.remove('mirror')
box_3.remove('submarine')

# Put the butterfly and the bicycle into Box 10
box_10.extend(['butterfly', 'bicycle'])

# Replace the scarf and the thread and the perfume with the violin and the ocean and the bracelet in Box 11
box_11.extend(['violin', 'ocean', 'bracelet'])
box_11.remove('scarf')
box_11.remove('thread')
box_11.remove('perfume')

# Move the usb and the tape from Box 2 to Box 12
box_12.extend([box_2.pop(1), box_2.pop(1)])

# Replace the pillow with the needle in Box 4
box_4.remove('pillow')
box_4.append('needle')

# Move the speaker from Box 1 to Box 5
box_5.append(box_1.pop(0))

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")