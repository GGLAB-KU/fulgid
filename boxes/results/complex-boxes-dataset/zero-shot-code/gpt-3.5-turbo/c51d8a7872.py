box_0 = ['crown', 'flute', 'bear', 'makeup', 'sculpture']
box_1 = []
box_2 = ['button', 'gloves']
box_3 = ['drum', 'lightning', 'oven', 'magnet']
box_4 = []
box_5 = []
box_6 = []
box_7 = ['elephant', 'microwave']
box_8 = ['violin', 'blender', 'glove', 'dolphin']
box_9 = ['mixer', 'tiger']
box_10 = ['umbrella', 'river', 'butterfly', 'seaweed']
box_11 = ['note', 'mountain', 'rocket', 'card', 'zipper']
box_12 = ['toothbrush', 'moon']
box_13 = ['bird', 'shelf', 'shoe', 'jacket', 'shampoo']

# Replace the plane with the river in Box 6
box_6 = ['river']

# Remove the table and the river from Box 6
box_6 = []

# Remove the shelf and the bird and the shampoo from Box 13
box_13 = []

# Move the note and the mountain from Box 11 to Box 1
box_1.extend(['note', 'mountain'])
box_11 = []

# Swap the glove in Box 8 with the moon in Box 12
box_8.remove('glove')
box_12.append('glove')

# Replace the button and the gloves with the rock and the pen in Box 2
box_2 = ['rock', 'pen']

# Empty Box 3
box_3 = []

# Remove the seaweed and the umbrella and the river from Box 10
box_10.remove('seaweed')
box_10.remove('umbrella')
box_10.remove('river')

# Remove the toothbrush and the glove from Box 12
box_12.remove('toothbrush')
box_12.remove('glove')

# Put the zipper and the cloud and the dice into Box 3
box_3.extend(['zipper', 'cloud', 'dice'])

# Put the leaf and the belt and the frame into Box 11
box_11.extend(['leaf', 'belt', 'frame'])

# Move the dice and the zipper and the cloud from Box 3 to Box 6
box_6.extend(['dice', 'zipper', 'cloud'])
box_3 = []

# Remove the jacket and the shoe from Box 13
box_13.remove('jacket')
box_13.remove('shoe')

# Put the planet into Box 1
box_1.append('planet')

# Move the violin and the dolphin from Box 8 to Box 9
box_9.extend(['violin', 'dolphin'])
box_8 = []

# Put the beach and the storm and the pot into Box 2
box_2.extend(['beach', 'storm', 'pot'])

# Remove the butterfly from Box 10
box_10.remove('butterfly')

# Replace the mixer with the shelf in Box 9
box_9.remove('mixer')
box_9.append('shelf')

# Remove the note and the mountain and the planet from Box 1
box_1 = []

# Remove the blender and the moon from Box 8
box_8 = []

# Swap the sculpture in Box 0 with the tiger in Box 9
box_0.remove('sculpture')
box_9.append('sculpture')

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
print("Box 13:", box_13)