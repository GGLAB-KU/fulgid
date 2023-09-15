box0 = ['glasses']
box1 = ['horse']
box2 = ['star', 'branch']
box3 = ['bus', 'battery', 'game', 'brush', 'helmet']

# Put storm and card and boat into Box 1
box1.extend(['storm', 'card', 'boat'])

# Move bus and helmet from Box 3 to Box 0
box0.extend([box3.pop(0), box3.pop(-1)])

# Remove bus from Box 0
box0.remove('bus')

# Remove branch and star from Box 2
box2.remove('branch')
box2.remove('star')

# Put bus into Box 1
box1.append('bus')

# Replace battery and brush with swimsuit and cow in Box 3
box3.remove('battery')
box3.remove('brush')
box3.extend(['swimsuit', 'cow'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)