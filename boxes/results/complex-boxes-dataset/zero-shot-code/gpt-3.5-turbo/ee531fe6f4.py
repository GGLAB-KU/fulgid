box_0 = ['ocean', 'piano', 'key']
box_1 = ['battery', 'coral', 'phone']
box_2 = ['jacket', 'telescope', 'train']
box_3 = ['clock', 'forest']
box_4 = ['glove', 'flute', 'shorts', 'blender']
box_5 = []
box_6 = ['paint', 'comet', 'sock', 'coat']
box_7 = ['scissors', 'octopus', 'basket']
box_8 = ['harmonica', 'star', 'dolphin', 'perfume', 'sculpture']
box_9 = ['dog', 'magnet', 'plate', 'wire', 'lipstick']
box_10 = ['makeup', 'river']
box_11 = ['tie', 'plane', 'shark', 'razor']
box_12 = ['freezer', 'guitar', 'cat', 'sun']
box_13 = ['mirror', 'microwave', 'card', 'toy', 'soap']
box_14 = ['camera', 'violin', 'cow', 'ring', 'fork']

# Swap the key in Box 0 with the paint in Box 6
box_0[2], box_6[0] = box_6[0], box_0[2]

# Move the scissors and the octopus and the basket from Box 7 to Box 10
box_10.extend([box_7.pop(0), box_7.pop(0), box_7.pop(0)])

# Replace the freezer with the microwave in Box 12
box_12[0] = 'microwave'

# Put the makeup and the speaker into Box 2
box_2.extend(['makeup', 'speaker'])

# Remove the cow from Box 14
box_14.remove('cow')

# Remove the sock from Box 6
box_6.remove('sock')

# Put the makeup into Box 14
box_14.append('makeup')

# Move the ring and the makeup from Box 14 to Box 0
box_0.extend([box_14.pop(box_14.index('ring')), box_14.pop(box_14.index('makeup'))])

# Swap the perfume in Box 8 with the clock in Box 3
box_8[3], box_3[0] = box_3[0], box_8[3]

# Empty Box 14
box_14.clear()

# Replace the key and the comet with the lamp and the needle in Box 6
box_6[2], box_6[1] = 'lamp', 'needle'

# Replace the card with the island in Box 13
box_13[2] = 'island'

# Swap the dolphin in Box 8 with the speaker in Box 2
box_8[2], box_2[3] = box_2[3], box_8[2]

# Put the starfish into Box 3
box_3.append('starfish')

# Replace the wire and the plate with the cat and the keyboard in Box 9
box_9[3], box_9[2] = 'cat', 'keyboard'

# Swap the ring in Box 0 with the plane in Box 11
box_0[2], box_11[1] = box_11[1], box_0[2]

# Put the grinder and the dice into Box 4
box_4.extend(['grinder', 'dice'])

# Replace the tie with the phone in Box 11
box_11[0] = 'phone'

# Put the jacket and the soap into Box 11
box_11.extend(['jacket', 'soap'])

# Remove the battery and the coral and the phone from Box 1
box_1.clear()

# Replace the jacket with the book in Box 2
box_2[0] = 'book'

# Move the grinder and the blender and the flute from Box 4 to Box 8
box_8.extend([box_4.pop(box_4.index('grinder')), box_4.pop(box_4.index('blender')), box_4.pop(box_4.index('flute'))])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")