box_0 = ['octopus', 'dog']
box_1 = ['doll', 'violin', 'piano', 'pan', 'butterfly']
box_2 = ['tie', 'freezer']
box_3 = ['grinder', 'camera', 'scarf', 'pot', 'gloves']
box_4 = []
box_5 = ['blender', 'candle']
box_6 = ['grass', 'bear', 'drum']
box_7 = ['sock', 'lamp']
box_8 = []
box_9 = ['jacket']
box_10 = ['shampoo', 'branch', 'desert', 'thread', 'table']
box_11 = ['skirt']
box_12 = ['spoon', 'pants', 'sandals']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Initial state
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)

# Remove the jacket from Box 9
box_9.remove('jacket')

# Put the starfish and the boat into Box 2
box_2.extend(['starfish', 'boat'])

# Replace the table and the desert with the boot and the cat in Box 10
box_10.remove('table')
box_10.remove('desert')
box_10.extend(['boot', 'cat'])

# Swap the skirt in Box 11 with the blender in Box 5
box_11.remove('skirt')
box_5.remove('blender')
box_11.append('blender')
box_5.append('skirt')

# Remove the bear and the grass and the drum from Box 6
box_6.remove('bear')
box_6.remove('grass')
box_6.remove('drum')

# Empty Box 12
box_12.clear()

# Replace the boot and the cat and the shampoo with the cloud and the keyboard and the microscope in Box 10
box_10.remove('boot')
box_10.remove('cat')
box_10.remove('shampoo')
box_10.extend(['cloud', 'keyboard', 'microscope'])

# Remove the boat from Box 2
box_2.remove('boat')

# Move the grinder from Box 3 to Box 4
box_3.remove('grinder')
box_4.append('grinder')

# Move the gloves from Box 3 to Box 0
box_3.remove('gloves')
box_0.append('gloves')

# Swap the sock in Box 7 with the blender in Box 11
box_7.remove('sock')
box_11.remove('blender')
box_7.append('blender')
box_11.append('sock')

# Put the sculpture and the starfish and the grass into Box 1
box_1.extend(['sculpture', 'starfish', 'grass'])

# Remove the lamp from Box 7
box_7.remove('lamp')

# Put the razor and the button and the bird into Box 3
box_3.extend(['razor', 'button', 'bird'])

# Replace the thread and the branch and the microscope with the bicycle and the whistle and the wallet in Box 10
box_10.remove('thread')
box_10.remove('branch')
box_10.remove('microscope')
box_10.extend(['bicycle', 'whistle', 'wallet'])

# Swap the octopus in Box 0 with the blender in Box 7
box_0.remove('octopus')
box_7.remove('blender')
box_0.append('blender')
box_7.append('octopus')

# Swap the camera in Box 3 with the whistle in Box 10
box_3.remove('camera')
box_10.remove('whistle')
box_3.append('whistle')
box_10.append('camera')

# Remove the grinder from Box 4
box_4.remove('grinder')

# Put the lipstick into Box 9
box_9.append('lipstick')

# Remove the piano and the sculpture and the starfish from Box 1
box_1.remove('piano')
box_1.remove('sculpture')
box_1.remove('starfish')

# Final state
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)