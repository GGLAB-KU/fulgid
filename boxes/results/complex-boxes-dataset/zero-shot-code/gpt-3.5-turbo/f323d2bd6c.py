box_0 = ['pan', 'shark']
box_1 = []
box_2 = ['lamp', 'horn', 'earring', 'necklace']
box_3 = ['cup', 'sculpture']
box_4 = ['button', 'ocean', 'razor']
box_5 = ['microwave', 'pen', 'beach']
box_6 = ['butterfly', 'mirror', 'telescope', 'pants']
box_7 = []
box_8 = []
box_9 = ['flute', 'headphone', 'paint', 'freezer', 'toothbrush']
box_10 = ['apple', 'charger', 'table', 'branch']
box_11 = ['coat', 'mountain', 'rock', 'vase', 'shoe']
box_12 = ['river', 'toaster', 'desert', 'umbrella', 'swimsuit']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Put the microscope into Box 4
box_4.append('microscope')

# Put the violin and the scissors and the paint into Box 3
box_3.extend(['violin', 'scissors', 'paint'])

# Swap the telescope in Box 6 with the paint in Box 9
box_6.remove('telescope')
box_9.remove('paint')
box_6.append('paint')
box_9.append('telescope')

# Move the microwave from Box 5 to Box 12
box_5.remove('microwave')
box_12.append('microwave')

# Move the telescope and the freezer and the flute from Box 9 to Box 5
box_9.remove('telescope')
box_9.remove('freezer')
box_9.remove('flute')
box_5.extend(['telescope', 'freezer', 'flute'])

# Swap the paint in Box 3 with the toothbrush in Box 9
box_3.remove('paint')
box_9.remove('toothbrush')
box_3.append('toothbrush')
box_9.append('paint')

# Swap the headphone in Box 9 with the pants in Box 6
box_9.remove('headphone')
box_6.remove('pants')
box_9.append('pants')
box_6.append('headphone')

# Remove the shark and the pan from Box 0
box_0.remove('shark')
box_0.remove('pan')

# Replace the pants and the paint with the shirt and the shelf in Box 9
box_9.remove('pants')
box_9.remove('paint')
box_9.extend(['shirt', 'shelf'])

# Remove the butterfly and the headphone and the mirror from Box 6
box_6.remove('butterfly')
box_6.remove('mirror')
box_6.remove('headphone')

# Put the scarf into Box 11
box_11.append('scarf')

# Put the grinder into Box 3
box_3.append('grinder')

# Put the speaker and the moon into Box 3
box_3.extend(['speaker', 'moon'])

# Empty Box 6
box_6.clear()

# Remove the horn from Box 2
box_2.remove('horn')

# Remove the button from Box 4
box_4.remove('button')

# Swap the shelf in Box 9 with the earring in Box 2
box_9.remove('shelf')
box_2.remove('earring')
box_9.append('earring')
box_2.append('shelf')

# Move the pen from Box 5 to Box 0
box_5.remove('pen')
box_0.append('pen')

# Replace the telescope with the pan in Box 5
box_5.remove('telescope')
box_5.append('pan')

# Print the contents of each box
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)