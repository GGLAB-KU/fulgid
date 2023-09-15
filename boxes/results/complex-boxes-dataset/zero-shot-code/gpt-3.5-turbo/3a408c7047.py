box_0 = ['lightning', 'butterfly', 'pot', 'camera']
box_1 = ['comb', 'bus', 'grinder', 'shorts']
box_2 = ['shelf', 'clock', 'mountain', 'lipstick', 'fork']
box_3 = ['pen', 'cup', 'submarine']
box_4 = ['dice', 'frame', 'tie', 'river']
box_5 = ['flower', 'horn', 'makeup', 'magnet', 'apple']
box_6 = ['shirt', 'shampoo']
box_7 = ['puzzle', 'polish', 'freezer', 'violin', 'chair']
box_8 = ['key', 'microwave', 'fish', 'gloves']
box_9 = ['jacket']

# Replace the pot and the camera and the lightning with the toaster and the pillow and the comb in Box 0
box_0 = ['toaster', 'pillow', 'comb']

# Remove the mountain from Box 2
box_2.remove('mountain')

# Move the violin and the polish and the chair from Box 7 to Box 9
box_9.extend(['violin', 'polish', 'chair'])
box_7.remove('violin')
box_7.remove('polish')
box_7.remove('chair')

# Replace the tie with the speaker in Box 4
box_4[2] = 'speaker'

# Replace the toaster with the glasses in Box 0
box_0[0] = 'glasses'

# Replace the fork and the lipstick and the shelf with the plane and the book and the guitar in Box 2
box_2[2:5] = ['plane', 'book', 'guitar']

# Remove the glasses and the butterfly from Box 0
box_0.remove('glasses')
box_0.remove('butterfly')

# Put the leaf into Box 4
box_4.append('leaf')

# Move the polish and the violin and the jacket from Box 9 to Box 1
box_1.extend(['polish', 'violin', 'jacket'])
box_9.remove('polish')
box_9.remove('violin')
box_9.remove('jacket')

# Move the makeup from Box 5 to Box 8
box_8.append('makeup')
box_5.remove('makeup')

# Swap the pillow in Box 0 with the guitar in Box 2
box_0[1], box_2[4] = box_2[4], box_0[1]

# Move the chair from Box 9 to Box 2
box_2.append(box_9.pop())

# Move the leaf and the river and the speaker from Box 4 to Box 0
box_0.extend([box_4.pop(3), box_4.pop(2), box_4.pop()])

# Remove the comb and the bus from Box 1
box_1.remove('comb')
box_1.remove('bus')

# Put the towel and the coat into Box 2
box_2.extend(['towel', 'coat'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)