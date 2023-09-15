box0 = ['toy', 'beach']
box1 = ['charger']
box2 = ['console', 'battery']
box3 = []

# Move the battery and the console from Box 2 to Box 0
box0.extend(box2)
box2.clear()

# Move the console from Box 0 to Box 1
box1.append(box0.pop(box0.index('console')))

# Replace the beach and the battery and the toy with the sculpture and the desert and the ring in Box 0
box0 = ['sculpture', 'desert', 'ring']

# Swap the desert in Box 0 with the charger in Box 1
box0[box0.index('desert')], box1[box1.index('charger')] = box1[box1.index('charger')], box0[box0.index('desert')]

# Replace the ring with the basket in Box 0
box0[box0.index('ring')] = 'basket'

# Replace the basket and the charger with the flower and the microscope in Box 0
box0[box0.index('basket')] = 'flower'
box0.append('microscope')
box1.remove('charger')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)