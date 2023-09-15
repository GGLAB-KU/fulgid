box0 = ['apple', 'shark', 'coral']
box1 = []
box2 = ['telescope', 'pan', 'shorts', 'branch', 'moon']
box3 = ['coat', 'soap']

# Move the coat and the soap from Box 3 to Box 0
box0.extend(box3)
box3.clear()

# Swap the apple in Box 0 with the shorts in Box 2
box0[0], box2[2] = box2[2], box0[0]

# Swap the telescope in Box 2 with the coral in Box 0
box2[0], box0[2] = box0[2], box2[0]

# Replace the apple and the moon with the lion and the butterfly in Box 2
box2[0] = 'lion'
box2[4] = 'butterfly'

# Remove the soap and the telescope and the shark from Box 0
box0.remove('soap')
box0.remove('telescope')
box0.remove('shark')

# Move the coat from Box 0 to Box 3
box3.append(box0.pop(0))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)