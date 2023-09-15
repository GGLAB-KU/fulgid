box0 = ['chair', 'helmet', 'necklace', 'toy']
box1 = ['battery', 'boot']
box2 = []
box3 = ['spoon', 'star', 'keyboard', 'shorts', 'console']
box4 = ['plate']

# Remove boot and battery from Box 1
box1.remove('boot')
box1.remove('battery')

# Replace chair and helmet with lion and forest in Box 0
box0.remove('chair')
box0.remove('helmet')
box0.append('lion')
box0.append('forest')

# Remove plate from Box 4
box4.remove('plate')

# Put cup into Box 2
box2.append('cup')

# Move keyboard and console from Box 3 to Box 2
box2.extend(['keyboard', 'console'])
box3.remove('keyboard')
box3.remove('console')

# Move forest and necklace from Box 0 to Box 4
box4.append('forest')
box4.append('necklace')
box0.remove('forest')
box0.remove('necklace')

# Swap toy in Box 0 with keyboard in Box 2
box0.remove('toy')
box2.remove('keyboard')
box0.append('keyboard')
box2.append('toy')

# Remove keyboard and lion from Box 0
box0.remove('keyboard')
box0.remove('lion')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)