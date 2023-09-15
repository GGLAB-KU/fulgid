box_0 = ['bird']
box_1 = ['flower', 'shoe', 'moon']
box_2 = ['oven', 'flute', 'leaf', 'earring']
box_3 = ['necklace', 'pot', 'sock']
box_4 = ['book']
box_5 = ['needle', 'blender', 'dress', 'spoon', 'helmet']
box_6 = []
box_7 = ['umbrella', 'charger', 'zipper', 'mixer', 'comet']
box_8 = ['game', 'harmonica', 'glove', 'horn']
box_9 = []
box_10 = []
box_11 = ['fork', 'lion', 'shirt']

def print_box(box_name, box):
    print(f"Box {box_name}: {box}")

# Move the blender and the helmet and the dress from Box 5 to Box 9
box_9.extend([box_5.pop(box_5.index('blender')), box_5.pop(box_5.index('helmet')), box_5.pop(box_5.index('dress'))])

# Replace the earring and the leaf and the oven with the starfish and the shorts and the flower in Box 2
box_2[box_2.index('earring')] = 'starfish'
box_2[box_2.index('leaf')] = 'shorts'
box_2[box_2.index('oven')] = 'flower'

# Put the horn and the star into Box 7
box_7.append(box_8.pop(box_8.index('horn')))
box_7.append('star')

# Remove the umbrella and the horn from Box 7
box_7.remove('umbrella')
box_7.remove('horn')

# Swap the charger in Box 7 with the book in Box 4
box_7[box_7.index('charger')] = box_4.pop(box_4.index('book'))

# Remove the flower and the moon and the shoe from Box 1
box_1.remove('flower')
box_1.remove('moon')
box_1.remove('shoe')

# Replace the needle with the pan in Box 5
box_5[box_5.index('needle')] = 'pan'

# Swap the starfish in Box 2 with the charger in Box 4
box_2[box_2.index('starfish')] = box_4.pop(box_4.index('charger'))

# Replace the game and the glove with the tiger and the bracelet in Box 8
box_8[box_8.index('game')] = 'tiger'
box_8[box_8.index('glove')] = 'bracelet'

# Swap the spoon in Box 5 with the dress in Box 9
box_5[box_5.index('spoon')] = box_9.pop(box_9.index('dress'))

# Put the thunder into Box 11
box_11.append('thunder')

# Replace the starfish with the vase in Box 4
box_4[box_4.index('starfish')] = 'vase'

# Move the bracelet from Box 8 to Box 11
box_11.append(box_8.pop(box_8.index('bracelet')))

# Move the horn from Box 8 to Box 2
box_2.append(box_8.pop(box_8.index('horn')))

# Put the glove and the freezer and the lock into Box 10
box_10.extend(['glove', 'freezer', 'lock'])

# Remove the harmonica from Box 8
box_8.remove('harmonica')

# Swap the dress in Box 5 with the bird in Box 0
box_0.append(box_5.pop(box_5.index('dress')))

# Replace the book with the dolphin in Box 7
box_7[box_7.index('book')] = 'dolphin'

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