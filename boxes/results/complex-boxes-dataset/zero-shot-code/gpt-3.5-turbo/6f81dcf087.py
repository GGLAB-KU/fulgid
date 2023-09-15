box_0 = ['wire', 'freezer', 'belt', 'piano']
box_1 = []
box_2 = ['plate', 'mask', 'lock', 'dress']
box_3 = []
box_4 = ['thread', 'sculpture', 'wallet', 'needle']
box_5 = ['sock', 'pants', 'rain', 'lamp']
box_6 = ['bag', 'tiger', 'chair']
box_7 = ['necklace', 'ocean', 'rocket', 'lion', 'charger']
box_8 = ['toy', 'leaf', 'rock']
box_9 = []

# Swap the rock in Box 8 with the sock in Box 5
box_8.remove('rock')
box_5.remove('sock')
box_8.append('sock')
box_5.append('rock')

# Swap the thread in Box 4 with the wire in Box 0
box_4.remove('thread')
box_0.remove('wire')
box_4.append('wire')
box_0.append('thread')

# Move the belt from Box 0 to Box 5
box_0.remove('belt')
box_5.append('belt')

# Remove the chair and the tiger from Box 6
box_6.remove('chair')
box_6.remove('tiger')

# Remove the plate and the dress from Box 2
box_2.remove('plate')
box_2.remove('dress')

# Replace the thread and the piano with the bird and the glove in Box 0
box_0.remove('thread')
box_0.remove('piano')
box_0.append('bird')
box_0.append('glove')

# Put the apple and the dog and the watch into Box 6
box_6.append('apple')
box_6.append('dog')
box_6.append('watch')

# Swap the watch in Box 6 with the glove in Box 0
box_6.remove('watch')
box_0.remove('glove')
box_6.append('glove')
box_0.append('watch')

# Put the elephant and the book and the razor into Box 0
box_0.append('elephant')
box_0.append('book')
box_0.append('razor')

# Move the leaf from Box 8 to Box 2
box_8.remove('leaf')
box_2.append('leaf')

# Remove the lamp and the rock from Box 5
box_5.remove('lamp')
box_5.remove('rock')

# Replace the wire and the sculpture with the horn and the comb in Box 4
box_4.remove('wire')
box_4.remove('sculpture')
box_4.append('horn')
box_4.append('comb')

# Remove the sock from Box 8
box_8.remove('sock')

# Remove the belt and the pants and the rain from Box 5
box_5.remove('belt')
box_5.remove('pants')
box_5.remove('rain')

# Put the hat and the flower and the tie into Box 9
box_9.append('hat')
box_9.append('flower')
box_9.append('tie')

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