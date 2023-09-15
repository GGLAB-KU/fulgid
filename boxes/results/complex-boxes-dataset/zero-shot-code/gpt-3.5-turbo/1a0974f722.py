box_0 = ['glasses', 'comet', 'vase']
box_1 = ['tape', 'phone', 'gloves', 'speaker']
box_2 = ['scissors', 'bag', 'button', 'blender', 'battery']
box_3 = ['apple', 'rain', 'frame', 'seaweed', 'telescope']
box_4 = ['wig', 'basket', 'horn', 'magnet']
box_5 = ['thread', 'helmet']
box_6 = []
box_7 = ['whistle', 'toy', 'toaster', 'toothpaste']
box_8 = ['jacket', 'shelf']
box_9 = ['submarine']
box_10 = ['console', 'piano', 'freezer']
box_11 = ['bicycle']
box_12 = []

# Replace the submarine with the tree in Box 9
box_9.remove('submarine')
box_9.append('tree')

# Remove the console and the piano and the freezer from Box 10
box_10.remove('console')
box_10.remove('piano')
box_10.remove('freezer')

# Put the table and the shoes and the cup into Box 0
box_0.extend(['table', 'shoes', 'cup'])

# Replace the thread and the helmet with the watch and the glasses in Box 5
box_5.remove('thread')
box_5.remove('helmet')
box_5.extend(['watch', 'glasses'])

# Swap the speaker in Box 1 with the horn in Box 4
box_1.remove('speaker')
box_4.remove('horn')
box_1.append('horn')
box_4.append('speaker')

# Swap the telescope in Box 3 with the horn in Box 1
box_3.remove('telescope')
box_1.remove('horn')
box_3.append('horn')
box_1.append('telescope')

# Remove the watch and the glasses from Box 5
box_5.remove('watch')
box_5.remove('glasses')

# Move the tree from Box 9 to Box 2
box_9.remove('tree')
box_2.append('tree')

# Move the bicycle from Box 11 to Box 9
box_11.remove('bicycle')
box_9.append('bicycle')

# Replace the bicycle with the tiger in Box 9
box_9.remove('bicycle')
box_9.append('tiger')

# Swap the whistle in Box 7 with the battery in Box 2
box_7.remove('whistle')
box_2.remove('battery')
box_7.append('battery')
box_2.append('whistle')

# Move the shelf from Box 8 to Box 1
box_8.remove('shelf')
box_1.append('shelf')

# Swap the battery in Box 7 with the tiger in Box 9
box_7.remove('battery')
box_9.remove('tiger')
box_7.append('tiger')
box_9.append('battery')

# Replace the battery with the fork in Box 9
box_9.remove('battery')
box_9.append('fork')

# Replace the tiger and the toy and the toothpaste with the mixer and the plate and the sandals in Box 7
box_7.remove('tiger')
box_7.remove('toy')
box_7.remove('toothpaste')
box_7.extend(['mixer', 'plate', 'sandals'])

# Move the glasses and the table and the vase from Box 0 to Box 5
box_0.remove('glasses')
box_0.remove('table')
box_0.remove('vase')
box_5.extend(['glasses', 'table', 'vase'])

# Swap the magnet in Box 4 with the table in Box 5
box_4.remove('magnet')
box_5.remove('table')
box_4.append('table')
box_5.append('magnet')

# Replace the glasses and the vase with the microscope and the chair in Box 5
box_5.remove('glasses')
box_5.remove('vase')
box_5.extend(['microscope', 'chair'])

# Replace the jacket with the boat in Box 8
box_8.remove('jacket')
box_8.append('boat')

# Replace the gloves and the tape with the shirt and the dog in Box 1
box_1.remove('gloves')
box_1.remove('tape')
box_1.extend(['shirt', 'dog'])

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")