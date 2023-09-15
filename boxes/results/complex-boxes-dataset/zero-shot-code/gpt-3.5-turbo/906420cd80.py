box_0 = []
box_1 = ['grinder', 'cloud', 'lamp']
box_2 = ['puzzle']
box_3 = ['skirt', 'fork']
box_4 = ['toothpaste', 'crown', 'rocket']
box_5 = ['ocean']
box_6 = ['game']
box_7 = []

# Replace the skirt and the fork with the gloves and the snow in Box 3
box_3.remove('skirt')
box_3.remove('fork')
box_3.extend(['gloves', 'snow'])

# Swap the fish in Box 1 with the ocean in Box 5
box_1.remove('fish')
box_5.remove('ocean')
box_1.append('ocean')
box_5.append('fish')

# Put the makeup and the submarine into Box 4
box_4.extend(['makeup', 'submarine'])

# Move the puzzle from Box 2 to Box 3
box_2.remove('puzzle')
box_3.append('puzzle')

# Replace the submarine with the lion in Box 4
box_4.remove('submarine')
box_4.append('lion')

# Put the swimsuit and the tape into Box 7
box_7.extend(['swimsuit', 'tape'])

# Replace the snow and the gloves and the puzzle with the frame and the watch and the wallet in Box 3
box_3.remove('snow')
box_3.remove('gloves')
box_3.remove('puzzle')
box_3.extend(['frame', 'watch', 'wallet'])

# Remove the tape from Box 7
box_7.remove('tape')

# Put the elephant into Box 3
box_3.append('elephant')

# Put the mask into Box 0
box_0.append('mask')

# Move the frame from Box 3 to Box 7
box_3.remove('frame')
box_7.append('frame')

# Move the watch and the elephant and the glove from Box 3 to Box 7
box_3.remove('watch')
box_3.remove('elephant')
box_3.remove('glove')
box_7.extend(['watch', 'elephant', 'glove'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)