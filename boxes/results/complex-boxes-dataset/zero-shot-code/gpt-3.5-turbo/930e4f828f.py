box0 = ['whistle']
box1 = []
box2 = ['polish', 'piano']
box3 = ['bracelet', 'spoon', 'telescope', 'lion']

# Move the spoon from Box 3 to Box 0
box0.append(box3.pop(box3.index('spoon')))

# Put the towel and the scissors into Box 3
box3.extend(['towel', 'scissors'])

# Put the freezer into Box 3
box3.append('freezer')

# Empty Box 3
box3 = []

# Move the polish from Box 2 to Box 1
box1.append(box2.pop(box2.index('polish')))

# Replace the whistle and the spoon with the boot and the shoes in Box 0
box0.remove('whistle')
box0.append('boot')
box0.append('shoes')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)