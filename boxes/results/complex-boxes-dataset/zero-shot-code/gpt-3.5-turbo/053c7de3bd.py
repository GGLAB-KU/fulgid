box0 = ['river']
box1 = []
box2 = ['fridge', 'basket', 'button']
box3 = ['tree', 'butterfly']

# Move fridge and button from Box 2 to Box 1
box1.extend([box2.pop(box2.index('fridge')), box2.pop(box2.index('button'))])

# Remove basket from Box 2
box2.remove('basket')

# Move fridge from Box 1 to Box 0
box0.append(box1.pop(box1.index('fridge')))

# Replace butterfly and tree with pan and snow in Box 3
box3 = ['pan', 'snow']

# Put lion and cup into Box 3
box3.extend(['lion', 'cup'])

# Put controller, plate, and comb into Box 0
box0.extend(['controller', 'plate', 'comb'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)