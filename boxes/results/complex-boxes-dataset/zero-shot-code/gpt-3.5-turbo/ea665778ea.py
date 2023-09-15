box_0 = ['mask', 'shelf', 'lightning', 'thread']
box_1 = ['jacket', 'coat', 'pen']
box_2 = ['apple', 'hat', 'wire']
box_3 = ['shark', 'headphone', 'dolphin']
box_4 = ['coral']
box_5 = ['island', 'tiger', 'usb', 'whistle', 'clock']
box_6 = ['bracelet']
box_7 = ['boot', 'octopus']
box_8 = ['plane', 'bird']

# Remove the bird from Box 8
box_8.remove('bird')

# Remove the thread and the lightning from Box 0
box_0.remove('thread')
box_0.remove('lightning')

# Replace the shark with the mountain in Box 3
box_3.remove('shark')
box_3.append('mountain')

# Swap the tiger in Box 5 with the coral in Box 4
box_5.remove('tiger')
box_4.remove('coral')
box_5.append('coral')
box_4.append('tiger')

# Swap the boot in Box 7 with the shelf in Box 0
box_7.remove('boot')
box_0.remove('shelf')
box_7.append('shelf')
box_0.append('boot')

# Empty Box 4
box_4 = []

# Move the hat and the apple from Box 2 to Box 8
box_2.remove('hat')
box_2.remove('apple')
box_8.append('hat')
box_8.append('apple')

# Replace the mountain and the headphone and the dolphin with the cat and the console and the boat in Box 3
box_3.remove('mountain')
box_3.remove('headphone')
box_3.remove('dolphin')
box_3.append('cat')
box_3.append('console')
box_3.append('boat')

# Swap the jacket in Box 1 with the octopus in Box 7
box_1.remove('jacket')
box_7.remove('octopus')
box_1.append('octopus')
box_7.append('jacket')

# Replace the pen and the octopus with the piano and the magnet in Box 1
box_1.remove('pen')
box_1.remove('octopus')
box_1.append('piano')
box_1.append('magnet')

# Empty Box 2
box_2 = []

# Swap the coat in Box 1 with the boot in Box 0
box_1.remove('coat')
box_0.remove('boot')
box_1.append('boot')
box_0.append('coat')

# Empty Box 5
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