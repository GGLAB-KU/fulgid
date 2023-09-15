box_0 = ['fridge']
box_1 = ['mountain', 'planet', 'whistle', 'grass', 'bear']
box_2 = ['pants', 'polish', 'freezer', 'soap', 'sun']
box_3 = ['zipper', 'lipstick', 'crown', 'comb']
box_4 = ['tiger', 'tie', 'cloud', 'swimsuit', 'gloves']
box_5 = []
box_6 = ['ocean', 'guitar', 'car', 'octopus']

# Replace the fridge with the zipper in Box 0
box_0.remove('fridge')
box_0.append('zipper')

# Move the zipper from Box 0 to Box 5
box_0.remove('zipper')
box_5.append('zipper')

# Swap the crown in Box 3 with the polish in Box 2
box_3.remove('crown')
box_2.remove('polish')
box_3.append('polish')
box_2.append('crown')

# Replace the whistle with the keyboard in Box 1
box_1.remove('whistle')
box_1.append('keyboard')

# Swap the cloud in Box 4 with the zipper in Box 5
box_4.remove('cloud')
box_5.remove('zipper')
box_4.append('zipper')
box_5.append('cloud')

# Move the crown from Box 2 to Box 6
box_2.remove('crown')
box_6.append('crown')

# Remove the crown from Box 6
box_6.remove('crown')

# Swap the freezer in Box 2 with the cloud in Box 5
box_2.remove('freezer')
box_5.remove('cloud')
box_2.append('cloud')
box_5.append('freezer')

# Empty Box 6
box_6 = []

# Empty Box 3
box_3 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)