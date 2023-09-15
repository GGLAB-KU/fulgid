box_0 = []
box_1 = ['boot', 'lipstick', 'shoe']
box_2 = ['needle', 'star']
box_3 = ['razor', 'pen']
box_4 = []
box_5 = ['microwave', 'truck', 'comb']
box_6 = ['plate', 'shorts', 'umbrella', 'cat', 'flute']
box_7 = ['blanket', 'blender']

# Move the razor from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('razor')))

# Replace the microwave and the truck with the octopus and the freezer in Box 5
box_5.remove('microwave')
box_5.remove('truck')
box_5.extend(['octopus', 'freezer'])

# Remove the pen from Box 3
box_3.remove('pen')

# Put the swimsuit and the lamp into Box 1
box_1.extend(['swimsuit', 'lamp'])

# Replace the umbrella and the plate with the elephant and the brush in Box 6
box_6.remove('umbrella')
box_6.remove('plate')
box_6.extend(['elephant', 'brush'])

# Move the shorts and the flute from Box 6 to Box 3
box_3.extend(['shorts', 'flute'])
box_6.remove('shorts')
box_6.remove('flute')

# Move the needle from Box 2 to Box 4
box_4.append(box_2.pop(box_2.index('needle')))

# Put the shoe and the bicycle into Box 3
box_3.extend(['shoe', 'bicycle'])

# Remove the lamp and the lipstick and the swimsuit from Box 1
box_1.remove('lamp')
box_1.remove('lipstick')
box_1.remove('swimsuit')

# Move the blanket and the razor from Box 7 to Box 0
box_0.extend([box_7.pop(box_7.index('blanket')), box_7.pop(box_7.index('razor'))])

# Put the controller into Box 5
box_5.append('controller')

# Move the cat and the brush and the elephant from Box 6 to Box 0
box_0.extend([box_6.pop(box_6.index('cat')), box_6.pop(box_6.index('brush')), box_6.pop(box_6.index('elephant'))])

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)