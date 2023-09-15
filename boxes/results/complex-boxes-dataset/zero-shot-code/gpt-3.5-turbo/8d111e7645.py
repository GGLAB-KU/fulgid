box_0 = ['razor', 'needle', 'grass']
box_1 = ['pants']
box_2 = []
box_3 = ['rain', 'grinder']
box_4 = []
box_5 = ['oven']
box_6 = []
box_7 = ['shelf', 'puzzle']
box_8 = []

# Replace the pants with the chair in Box 1
box_1 = ['chair']

# Swap the oven in Box 5 with the shelf in Box 7
box_5, box_7 = box_7, box_5

# Replace the oven with the candle in Box 7
box_7 = ['candle']

# Swap the rain in Box 3 with the razor in Box 0
box_0, box_3 = box_3, box_0

# Swap the razor in Box 3 with the chair in Box 1
box_1, box_3 = box_3, box_1

# Put the camera and the bear into Box 8
box_8 = ['camera', 'bear']

# Swap the razor in Box 1 with the puzzle in Box 7
box_1, box_7 = box_7, box_1

# Swap the camera in Box 8 with the rain in Box 0
box_0, box_8 = box_8, box_0

# Replace the candle and the razor with the boat and the scissors in Box 7
box_7 = ['boat', 'scissors']

# Move the puzzle from Box 1 to Box 5
box_5 = box_5 + box_1
box_1 = []

# Move the grass and the needle and the camera from Box 0 to Box 1
box_1 = box_1 + box_0
box_0 = []

# Replace the shelf and the puzzle with the bird and the magnet in Box 5
box_5 = ['bird', 'magnet']

# Remove the magnet and the bird from Box 5
box_5 = []

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