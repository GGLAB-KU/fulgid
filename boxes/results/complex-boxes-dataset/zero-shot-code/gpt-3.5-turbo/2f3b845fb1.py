box0 = ['wig', 'fridge', 'makeup']
box1 = ['violin', 'ring', 'branch']
box2 = ['bird', 'meteor']
box3 = ['lightning', 'battery', 'ship', 'clock']

# Swap violin with battery
box1.remove('violin')
box3.remove('battery')
box1.append('battery')
box3.append('violin')

# Swap branch with clock
box1.remove('branch')
box3.remove('clock')
box1.append('clock')
box3.append('branch')

# Move ship, violin, and branch from box3 to box1
box1.extend(box3)
box3.clear()

# Replace makeup with laptop in box0
box0.remove('makeup')
box0.append('laptop')

# Remove bird and meteor from box2
box2.remove('bird')
box2.remove('meteor')

# Move laptop, wig, and fridge from box0 to box2
box2.extend(box0)
box0.clear()

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)