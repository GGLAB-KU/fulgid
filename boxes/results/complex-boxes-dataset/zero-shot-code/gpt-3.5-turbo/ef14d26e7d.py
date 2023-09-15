box_0 = []
box_1 = []
box_2 = ['candle']
box_3 = ['key', 'meteor', 'blanket', 'violin', 'swimsuit']
box_4 = []
box_5 = ['microwave']

# Swap the microwave in Box 5 with the candle in Box 2
box_2.remove('candle')
box_5.remove('microwave')
box_2.append('microwave')
box_5.append('candle')

# Replace the candle with the book in Box 5
box_5.remove('candle')
box_5.append('book')

# Swap the blanket in Box 3 with the microwave in Box 2
box_2.remove('microwave')
box_3.remove('blanket')
box_2.append('blanket')
box_3.append('microwave')

# Put the branch into Box 1
box_1.append('branch')

# Move the key from Box 3 to Box 5
box_3.remove('key')
box_5.append('key')

# Put the whistle and the sculpture into Box 2
box_2.append('whistle')
box_2.append('sculpture')

# Remove the book and the key from Box 5
box_5.remove('book')
box_5.remove('key')

# Remove the branch from Box 1
box_1.remove('branch')

# Replace the whistle and the blanket with the thread and the tape in Box 2
box_2.remove('whistle')
box_2.remove('blanket')
box_2.append('thread')
box_2.append('tape')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)