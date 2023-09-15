box_0 = ['towel']
box_1 = ['candle', 'fork']
box_2 = ['makeup', 'whistle']
box_3 = ['card', 'grinder']
box_4 = ['comb']
box_5 = ['mask', 'coat', 'bus']
box_6 = []
box_7 = ['magnet', 'mountain', 'mixer', 'zipper', 'tape']
box_8 = ['razor']

# Replace the grinder with the sculpture in Box 3
box_3 = ['card', 'sculpture']

# Remove the towel from Box 0
box_0 = []

# Empty Box 3
box_3 = []

# Move the mountain and the magnet from Box 7 to Box 8
box_8.extend(['mountain', 'magnet'])
box_7.remove('mountain')
box_7.remove('magnet')

# Put the chair and the jungle and the fridge into Box 4
box_4.extend(['chair', 'jungle', 'fridge'])

# Swap the comb in Box 4 with the coat in Box 5
box_4, box_5 = box_5, box_4

# Remove the comb and the mask and the bus from Box 5
box_5 = []

# Swap the candle in Box 1 with the whistle in Box 2
box_1, box_2 = box_2, box_1

# Empty Box 8
box_8 = []

# Replace the mixer and the tape and the zipper with the dolphin and the towel and the island in Box 7
box_7 = ['magnet', 'dolphin', 'island']

# Replace the towel with the jacket in Box 7
box_7.remove('towel')
box_7.append('jacket')

# Move the makeup from Box 2 to Box 8
box_8.append('makeup')
box_2.remove('makeup')

# Remove the candle from Box 2
box_2.remove('candle')

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