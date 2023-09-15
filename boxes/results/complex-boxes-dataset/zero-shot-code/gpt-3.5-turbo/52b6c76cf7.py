box_0 = ['charger', 'coat', 'shoes', 'tape']
box_1 = ['spoon', 'keyboard', 'belt']
box_2 = ['helmet', 'ocean']
box_3 = ['magnet']
box_4 = ['needle', 'grass', 'hat', 'submarine', 'scissors']
box_5 = []
box_6 = ['card']
box_7 = ['key', 'guitar']
box_8 = []
box_9 = ['planet']
box_10 = ['cup', 'polish', 'storm']
box_11 = ['mixer', 'whistle']

# Remove the hat and the needle from Box 4
box_4.remove('hat')
box_4.remove('needle')

# Swap the cup in Box 10 with the card in Box 6
box_10.remove('cup')
box_6.remove('card')
box_10.append('card')
box_6.append('cup')

# Move the belt and the keyboard from Box 1 to Box 2
box_1.remove('belt')
box_1.remove('keyboard')
box_2.append('belt')
box_2.append('keyboard')

# Put the lipstick and the earring into Box 10
box_10.append('lipstick')
box_10.append('earring')

# Remove the whistle from Box 11
box_11.remove('whistle')

# Swap the mixer in Box 11 with the coat in Box 0
box_11.remove('mixer')
box_0.remove('coat')
box_11.append('coat')
box_0.append('mixer')

# Put the fridge and the swimsuit into Box 0
box_0.append('fridge')
box_0.append('swimsuit')

# Remove the planet from Box 9
box_9.remove('planet')

# Swap the magnet in Box 3 with the coat in Box 11
box_3.remove('magnet')
box_11.remove('coat')
box_3.append('coat')
box_11.append('magnet')

# Put the cup and the dolphin and the shirt into Box 5
box_5.append('cup')
box_5.append('dolphin')
box_5.append('shirt')

# Remove the lipstick from Box 10
box_10.remove('lipstick')

# Remove the coat from Box 3
box_3.remove('coat')

# Remove the guitar from Box 7
box_7.remove('guitar')

# Replace the scissors with the shark in Box 4
box_4.remove('scissors')
box_4.append('shark')

# Remove the storm from Box 10
box_10.remove('storm')

# Swap the card in Box 10 with the key in Box 7
box_10.remove('card')
box_7.remove('key')
box_10.append('key')
box_7.append('card')

# Put the makeup into Box 9
box_9.append('makeup')

# Move the polish and the key from Box 10 to Box 2
box_10.remove('polish')
box_10.remove('key')
box_2.append('polish')
box_2.append('key')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)