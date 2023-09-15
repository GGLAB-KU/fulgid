box_0 = ['headphone', 'clock', 'ring', 'horse', 'cup']
box_1 = ['brush']
box_2 = ['fork']
box_3 = ['shoe']
box_4 = ['doll', 'branch', 'bell']

# Replace the shoe with the towel in Box 3
box_3 = ['towel']

# Empty Box 0
box_0 = []

# Replace the brush with the car in Box 1
box_1 = ['car']

# Swap the doll in Box 4 with the fork in Box 2
box_2, box_4 = box_4, box_2

# Replace the car with the mirror in Box 1
box_1 = ['mirror']

# Replace the towel with the puzzle in Box 3
box_3 = ['puzzle']

# Move the puzzle from Box 3 to Box 1
box_1 = box_1 + box_3
box_3 = []

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)