box_0 = []
box_1 = ['chair', 'elephant', 'seaweed']
box_2 = ['swimsuit', 'plate']
box_3 = []
box_4 = ['island', 'tiger', 'grass', 'lamp', 'whistle']

# Replace the tiger and the whistle with the bowl and the bus in Box 4
box_4[1] = 'bowl'
box_4[-1] = 'bus'

# Remove the chair from Box 1
box_1.remove('chair')

# Replace the swimsuit and the plate with the dolphin and the beach in Box 2
box_2[0] = 'dolphin'
box_2[1] = 'beach'

# Replace the seaweed with the pan in Box 1
box_1[2] = 'pan'

# Swap the elephant in Box 1 with the bus in Box 4
box_1[1], box_4[-1] = box_4[-1], box_1[1]

# Replace the grass and the island and the lamp with the bracelet and the comb and the guitar in Box 4
box_4[0] = 'bracelet'
box_4[2] = 'comb'
box_4[3] = 'guitar'

# Swap the bracelet in Box 4 with the bus in Box 1
box_4[0], box_1[2] = box_1[2], box_4[0]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)