box_0 = ['swimsuit', 'belt', 'clock']
box_1 = []
box_2 = ['toothpaste']
box_3 = ['shark', 'headphone', 'skirt']
box_4 = ['mixer', 'drum', 'sculpture', 'fish']
box_5 = []
box_6 = ['fork', 'whistle', 'key', 'butterfly', 'cup']

# Put the brush and the snow into Box 0
box_0.extend(['brush', 'snow'])

# Move the toothpaste from Box 2 to Box 3
box_3.append(box_2.pop())

# Put the paint into Box 0
box_0.append('paint')

# Swap the clock in Box 0 with the headphone in Box 3
box_0[2], box_3[1] = box_3[1], box_0[2]

# Swap the skirt in Box 3 with the paint in Box 0
box_3[2], box_0[3] = box_0[3], box_3[2]

# Remove the sculpture and the mixer and the drum from Box 4
box_4.remove('sculpture')
box_4.remove('mixer')
box_4.remove('drum')

# Remove the brush from Box 0
box_0.remove('brush')

# Replace the cup and the butterfly with the tiger and the towel in Box 6
box_6[4] = 'tiger'
box_6[3] = 'towel'

# Replace the tiger and the towel and the key with the pillow and the battery and the cat in Box 6
box_6[4] = 'pillow'
box_6[3] = 'battery'
box_6[2] = 'cat'

# Swap the paint in Box 3 with the pillow in Box 6
box_3[3], box_6[4] = box_6[4], box_3[3]

# Put the glove into Box 6
box_6.append('glove')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)