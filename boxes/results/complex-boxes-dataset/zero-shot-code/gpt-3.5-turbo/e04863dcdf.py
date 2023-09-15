box_0 = ['candle', 'bear', 'beach', 'lipstick', 'boat']
box_1 = ['phone', 'wire']
box_2 = ['oven', 'coat']
box_3 = ['card', 'jacket']
box_4 = ['toothbrush', 'flute', 'river', 'guitar']
box_5 = ['frame', 'coral', 'scarf']
box_6 = ['shelf']
box_7 = ['microscope']
box_8 = ['flower', 'table', 'watch', 'grinder', 'tiger']
box_9 = ['planet']
box_10 = []

# Remove guitar, flute, and river from Box 4
box_4.remove('guitar')
box_4.remove('flute')
box_4.remove('river')

# Empty Box 8
box_8 = []

# Remove candle and lipstick from Box 0
box_0.remove('candle')
box_0.remove('lipstick')

# Replace toothbrush with brush from Box 4
box_4.remove('toothbrush')
box_4.append('brush')

# Remove shelf from Box 6
box_6 = []

# Swap bear in Box 0 with planet in Box 9
box_0.remove('bear')
box_9.remove('planet')
box_0.append('planet')
box_9.append('bear')

# Move phone from Box 1 to Box 0
box_1.remove('phone')
box_0.append('phone')

# Remove bear from Box 9
box_9.remove('bear')

# Swap coral in Box 5 with wire in Box 1
box_5.remove('coral')
box_1.remove('wire')
box_5.append('wire')
box_1.append('coral')

# Remove jacket from Box 3
box_3.remove('jacket')

# Remove card from Box 3
box_3.remove('card')

# Remove coral from Box 1
box_1.remove('coral')

# Remove brush from Box 4
box_4.remove('brush')

# Replace scarf and frame with toaster and comet in Box 5
box_5.remove('scarf')
box_5.remove('frame')
box_5.append('toaster')
box_5.append('comet')

# Remove boat from Box 0
box_0.remove('boat')

# Move phone and beach from Box 0 to Box 2
box_0.remove('phone')
box_0.remove('beach')
box_2.append('phone')
box_2.append('beach')

# Empty Box 2
box_2 = []

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