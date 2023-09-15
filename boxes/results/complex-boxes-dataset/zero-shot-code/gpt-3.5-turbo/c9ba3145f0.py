box0 = ['bell', 'drum', 'blender', 'thread', 'brush']
box1 = []
box2 = []
box3 = ['ship', 'charger', 'fridge']

# Replace the fridge with the coat in Box 3
box3.remove('fridge')
box3.append('coat')

# Move the brush and the drum and the bell from Box 0 to Box 3
box3.extend(['brush', 'drum', 'bell'])
box0.remove('brush')
box0.remove('drum')
box0.remove('bell')

# Move the blender and the thread from Box 0 to Box 3
box3.extend(['blender', 'thread'])
box0.remove('blender')
box0.remove('thread')

# Move the blender from Box 3 to Box 0
box0.append('blender')
box3.remove('blender')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)