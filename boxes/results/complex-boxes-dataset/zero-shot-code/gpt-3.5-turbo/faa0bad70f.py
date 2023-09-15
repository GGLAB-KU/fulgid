box_0 = ['river', 'meteor', 'scissors']
box_1 = ['coat', 'tree', 'truck', 'magnet', 'boat']
box_2 = []
box_3 = ['ocean', 'toaster', 'storm']
box_4 = ['rain', 'cup', 'shorts']
box_5 = ['grinder', 'controller', 'snow', 'mirror']
box_6 = ['towel', 'sandals']
box_7 = ['coin']
box_8 = []
box_9 = ['ship', 'shark', 'horn', 'oven']
box_10 = ['shoes', 'paint', 'shelf', 'bowl', 'motorcycle']
box_11 = ['card', 'spoon', 'fork', 'telescope']
box_12 = ['pot', 'plate', 'train']

# Remove the shelf and the motorcycle from Box 10
box_10.remove('shelf')
box_10.remove('motorcycle')

# Put the shirt and the starfish and the jungle into Box 7
box_7.extend(['shirt', 'starfish', 'jungle'])

# Move the rain and the shorts and the cup from Box 4 to Box 9
box_9.extend(box_4[0:3])
box_4 = []

# Move the controller and the snow and the mirror from Box 5 to Box 7
box_7.extend(box_5[1:4])
box_5 = ['grinder']

# Swap the train in Box 12 with the towel in Box 6
box_12[2], box_6[0] = box_6[0], box_12[2]

# Remove the paint from Box 10
box_10.remove('paint')

# Remove the grinder from Box 5
box_5 = []

# Replace the truck and the magnet with the bear and the mirror in Box 1
box_1[2:4] = ['bear', 'mirror']

# Remove the shoes from Box 10
box_10.remove('shoes')

# Put the watch and the pen and the microscope into Box 5
box_5.extend(['watch', 'pen', 'microscope'])

# Swap the ocean in Box 3 with the coin in Box 7
box_3[0], box_7[0] = box_7[0], box_3[0]

# Swap the ship in Box 9 with the train in Box 6
box_9[0], box_6[0] = box_6[0], box_9[0]

# Swap the pen in Box 5 with the toaster in Box 3
box_5[1], box_3[1] = box_3[1], box_5[1]

# Move the bowl from Box 10 to Box 3
box_3.append(box_10.pop(3))

# Move the boat from Box 1 to Box 2
box_2.append(box_1.pop(4))

# Replace the controller and the snow and the starfish with the doll and the wire and the tiger in Box 7
box_7[1:4] = ['doll', 'wire', 'tiger']

# Replace the spoon with the dress in Box 11
box_11[1] = 'dress'

# Remove the river and the meteor from Box 0
box_0 = []

# Put the book and the bowl into Box 0
box_0.extend(['book', 'bowl'])

# Remove the towel and the plate from Box 12
box_12 = box_12[0:2]

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")