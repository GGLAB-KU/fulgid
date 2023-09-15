box_0 = ['whistle', 'comet', 'blanket', 'bear']
box_1 = ['shirt']
box_2 = ['needle', 'planet', 'scarf']
box_3 = ['motorcycle', 'paint']
box_4 = ['watch', 'car', 'bell']
box_5 = ['pants', 'piano', 'headphone', 'shampoo', 'snow']
box_6 = ['game', 'camera', 'microscope', 'branch']
box_7 = ['frame', 'rock', 'pillow', 'thread', 'lamp']
box_8 = ['violin', 'console', 'ship']
box_9 = []
box_10 = []
box_11 = ['blender', 'bus', 'table']
box_12 = ['scissors', 'rain', 'note', 'mountain']

# Replace the scarf, planet, and needle in Box 2
box_2 = ['octopus', 'bowl', 'shoes']

# Put the mirror, bowl, and grass into Box 3
box_3.extend(['mirror', 'bowl', 'grass'])

# Move the ship, console, and violin from Box 8 to Box 12
box_12.extend(['ship', 'console', 'violin'])
box_8 = []

# Put the storm, oven, and comb into Box 0
box_0.extend(['storm', 'oven', 'comb'])

# Replace the console, violin, and note with the shoe, makeup, and candle in Box 12
box_12 = ['shoe', 'makeup', 'candle']

# Empty Box 12
box_12 = []

# Put the fridge into Box 1
box_1 = ['fridge']

# Move the rock from Box 7 to Box 4
box_4.append('rock')
box_7.remove('rock')

# Swap the octopus in Box 2 with the branch in Box 6
box_2.remove('octopus')
box_6.remove('branch')
box_2.append('branch')
box_6.append('octopus')

# Swap the grass in Box 3 with the bus in Box 11
box_3.remove('grass')
box_11.remove('bus')
box_3.append('bus')
box_11.append('grass')

# Move the snow, headphone, and shampoo from Box 5 to Box 4
box_4.extend(['snow', 'headphone', 'shampoo'])
box_5 = []

# Replace the camera with the brush in Box 6
box_6.remove('camera')
box_6.append('brush')

# Put the grinder into Box 3
box_3.append('grinder')

# Swap the blender in Box 11 with the fridge in Box 1
box_11.remove('blender')
box_1.remove('fridge')
box_11.append('fridge')
box_1.append('blender')

# Remove the bowl, shoes, and branch from Box 2
box_2 = []

# Replace the headphone, snow, and car with the frame, toothbrush, and shorts in Box 4
box_4 = ['frame', 'toothbrush', 'shorts']

# Move the fridge, table, and grass from Box 11 to Box 1
box_1.extend(['fridge', 'table', 'grass'])
box_11 = []

# Replace the frame, rock, and shorts with the watch, toy, and button in Box 4
box_4 = ['watch', 'toy', 'button']

# Replace the grinder, bus, and mirror with the freezer, pot, and shoe in Box 3
box_3 = ['freezer', 'pot', 'shoe']

# Replace the microscope, brush, and octopus with the rocket, tape, and cup in Box 6
box_6 = ['rocket', 'tape', 'cup']

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
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)