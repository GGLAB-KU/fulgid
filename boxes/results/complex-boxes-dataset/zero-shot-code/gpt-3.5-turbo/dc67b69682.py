box0 = []
box1 = []
box2 = []
box3 = []

# Initial state
box0 = []
box1 = ['candle']
box2 = ['glasses', 'speaker']
box3 = ['cloud', 'coral', 'glove', 'jacket', 'dog']

# Swap candle with dog
box1.remove('candle')
box3.remove('dog')
box1.append('dog')
box3.append('candle')

# Move dog from box1 to box0
box0.append(box1.pop())

# Replace speaker and glasses with coin and flute
box2.remove('speaker')
box2.remove('glasses')
box2.append('coin')
box2.append('flute')

# Move dog from box0 to box3
box3.append(box0.pop())

# Put grass into box1
box1.append('grass')

# Swap grass with flute
box1.remove('grass')
box2.remove('flute')
box1.append('flute')
box2.append('grass')

# Print the final state of the boxes
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)