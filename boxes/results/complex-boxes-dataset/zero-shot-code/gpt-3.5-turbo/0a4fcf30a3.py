box_0 = ['ring', 'apple']
box_1 = ['shirt']
box_2 = ['sock', 'coral', 'butterfly', 'candle']
box_3 = []
box_4 = []
box_5 = ['planet', 'shampoo', 'rocket', 'dress']
box_6 = ['paint', 'motorcycle', 'tie']

# Replace items in Box 2
box_2 = ['sock', 'fridge', 'coin', 'train']

# Add items to Box 5
box_5.extend(['toothbrush', 'lion', 'bird'])

# Replace items in Box 0
box_0 = ['bracelet', 'mask']

# Move items from Box 6 to Box 4
box_4.extend(['motorcycle', 'tie'])
box_6 = []

# Remove shirt from Box 1
box_1 = []

# Replace train with console in Box 2
box_2 = ['sock', 'fridge', 'coin', 'console']

# Add toothpaste and bird to Box 4
box_4.extend(['toothpaste', 'bird'])

# Replace paint with pan in Box 6
box_6 = ['pan']

# Remove tie from Box 4
box_4.remove('tie')

# Move toothpaste, motorcycle, and bird from Box 4 to Box 0
box_0.extend(['toothpaste', 'motorcycle', 'bird'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)