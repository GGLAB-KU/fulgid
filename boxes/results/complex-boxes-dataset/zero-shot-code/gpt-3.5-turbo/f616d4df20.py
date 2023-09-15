box_0 = ['camera', 'pen', 'crown']
box_1 = ['brush', 'shark']
box_2 = []
box_3 = ['blanket', 'vase', 'island', 'paint', 'sculpture']
box_4 = ['puzzle', 'lipstick', 'key', 'charger']
box_5 = ['toothbrush', 'blender', 'drum', 'coral', 'keyboard']
box_6 = ['tape', 'magnet', 'bracelet']
box_7 = ['shoe', 'tree', 'star']
box_8 = ['octopus']
box_9 = ['submarine']
box_10 = []
box_11 = ['lion', 'wire', 'umbrella']
box_12 = ['shorts', 'bear', 'necklace', 'leaf']
box_13 = []

# Swap bear and umbrella
box_11.remove('umbrella')
box_12.remove('bear')
box_11.append('bear')
box_12.append('umbrella')

# Replace star, shoe, and tree with spoon, scarf, and fork
box_7.remove('star')
box_7.remove('shoe')
box_7.remove('tree')
box_7.append('spoon')
box_7.append('scarf')
box_7.append('fork')

# Put needle into Box 7
box_7.append('needle')

# Move brush and shark from Box 1 to Box 12
box_1.remove('brush')
box_1.remove('shark')
box_12.append('brush')
box_12.append('shark')

# Move blender and coral from Box 5 to Box 10
box_5.remove('blender')
box_5.remove('coral')
box_10.append('blender')
box_10.append('coral')

# Put crown into Box 12
box_12.append('crown')

# Move keyboard from Box 5 to Box 6
box_5.remove('keyboard')
box_6.append('keyboard')

# Remove needle from Box 7
box_7.remove('needle')

# Put toothbrush into Box 4
box_4.append('toothbrush')

# Replace coral with glasses in Box 10
box_10.remove('coral')
box_10.append('glasses')

# Remove crown, pen, and camera from Box 0
box_0.remove('crown')
box_0.remove('pen')
box_0.remove('camera')

# Swap keyboard in Box 6 with charger in Box 4
box_6.remove('keyboard')
box_4.remove('charger')
box_6.append('charger')
box_4.append('keyboard')

# Move wire and lion from Box 11 to Box 10
box_11.remove('wire')
box_11.remove('lion')
box_10.append('wire')
box_10.append('lion')

# Move sculpture from Box 3 to Box 8
box_3.remove('sculpture')
box_8.append('sculpture')

# Replace wire, glasses, and lion with cloud, vase, and fish in Box 10
box_10.remove('wire')
box_10.remove('glasses')
box_10.remove('lion')
box_10.append('cloud')
box_10.append('vase')
box_10.append('fish')

# Remove fork, spoon, and scarf from Box 7
box_7.remove('fork')
box_7.remove('spoon')
box_7.remove('scarf')

# Put bird, grass, and pot into Box 11
box_11.append('bird')
box_11.append('grass')
box_11.append('pot')

# Replace octopus with snow in Box 8
box_8.remove('octopus')
box_8.append('snow')

# Replace submarine with apple in Box 9
box_9.remove('submarine')
box_9.append('apple')

# Put scarf and frame into Box 9
box_9.append('scarf')
box_9.append('frame')

# Remove keyboard from Box 4
box_4.remove('keyboard')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")