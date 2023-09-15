box0 = ['phone', 'star', 'jungle']
box1 = ['branch', 'ship', 'shorts', 'wig']
box2 = []
box3 = ['candle']

# Move the candle from Box 3 to Box 1
box1.append(box3.pop(0))

# Remove the star and the jungle from Box 0
box0.remove('star')
box0.remove('jungle')

# Replace the phone with the thunder in Box 0
box0.remove('phone')
box0.append('thunder')

# Remove the thunder from Box 0
box0.remove('thunder')

# Replace the branch and the wig with the meteor and the leaf in Box 1
box1.remove('branch')
box1.remove('wig')
box1.append('meteor')
box1.append('leaf')

# Remove the shorts from Box 1
box1.remove('shorts')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)