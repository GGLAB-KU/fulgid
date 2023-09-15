box_0 = ['flute']
box_1 = ['controller', 'shirt']
box_2 = ['dice', 'polish', 'soap']
box_3 = ['jacket', 'apple', 'phone', 'speaker']
box_4 = ['coral', 'river', 'swimsuit']

# Put the rocket, rock, and dolphin into Box 1
box_1.extend(['rocket', 'rock', 'dolphin'])

# Put the swimsuit into Box 0
box_0.append('swimsuit')

# Move the swimsuit and flute from Box 0 to Box 1
box_1.extend(box_0)
box_0 = []

# Remove the soap from Box 2
box_2.remove('soap')

# Move the jacket, speaker, and phone from Box 3 to Box 1
box_1.extend(box_3[:3])
box_3 = box_3[3:]

# Swap the apple in Box 3 with the coral in Box 4
box_3[1], box_4[0] = box_4[0], box_3[1]

# Swap the controller in Box 1 with the polish in Box 2
box_1[0], box_2[1] = box_2[1], box_1[0]

# Put the bracelet into Box 2
box_2.append('bracelet')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)