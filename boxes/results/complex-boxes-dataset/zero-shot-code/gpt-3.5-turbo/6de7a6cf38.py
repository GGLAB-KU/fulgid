box_0 = ['doll', 'comb', 'lipstick', 'shoe', 'rain']
box_1 = ['flute', 'desert', 'wallet', 'bird', 'blanket']
box_2 = ['truck', 'microscope', 'ocean', 'spoon']
box_3 = ['table', 'tie', 'ring', 'zipper']
box_4 = ['tree', 'storm', 'pen', 'plate', 'bowl']
box_5 = ['pan', 'frame', 'boot']
box_6 = []
box_7 = ['cup', 'button', 'bear', 'branch', 'microwave']
box_8 = ['freezer', 'headphone', 'key']
box_9 = []
box_10 = ['speaker', 'thread', 'battery', 'car', 'skirt']
box_11 = ['keyboard', 'train', 'belt', 'violin']
box_12 = []

# Put the starfish and the note and the train into Box 4
box_4.extend(['starfish', 'note', 'train'])

# Swap the zipper in Box 3 with the button in Box 7
box_3.remove('zipper')
box_7.remove('button')
box_3.append('button')
box_7.append('zipper')

# Replace the table and the tie with the horn and the microscope in Box 3
box_3.remove('table')
box_3.remove('tie')
box_3.extend(['horn', 'microscope'])

# Replace the freezer with the dice in Box 8
box_8.remove('freezer')
box_8.append('dice')

# Put the flute and the cup and the piano into Box 9
box_9.extend(['flute', 'cup', 'piano'])

# Swap the cup in Box 9 with the train in Box 4
box_9.remove('cup')
box_4.remove('train')
box_9.append('train')
box_4.append('cup')

# Put the cow and the leaf into Box 10
box_10.extend(['cow', 'leaf'])

# Swap the note in Box 4 with the wallet in Box 1
box_4.remove('note')
box_1.remove('wallet')
box_4.append('wallet')
box_1.append('note')

# Put the toaster and the fridge into Box 10
box_10.extend(['toaster', 'fridge'])

# Swap the boot in Box 5 with the train in Box 11
box_5.remove('boot')
box_11.remove('train')
box_5.append('train')
box_11.append('boot')

# Swap the belt in Box 11 with the horn in Box 3
box_11.remove('belt')
box_3.remove('horn')
box_11.append('horn')
box_3.append('belt')

# Replace the cup and the branch with the helmet and the mirror in Box 7
box_7.remove('cup')
box_7.remove('branch')
box_7.extend(['helmet', 'mirror'])

# Remove the bear from Box 7
box_7.remove('bear')

# Swap the speaker in Box 10 with the key in Box 8
box_10.remove('speaker')
box_8.remove('key')
box_10.append('key')
box_8.append('speaker')

# Put the cow and the pillow into Box 12
box_12.extend(['cow', 'pillow'])

# Move the lipstick from Box 0 to Box 11
box_0.remove('lipstick')
box_11.append('lipstick')

# Put the coral and the wallet and the jungle into Box 7
box_7.extend(['coral', 'wallet', 'jungle'])

# Put the submarine into Box 2
box_2.append('submarine')

# Move the flute from Box 1 to Box 2
box_1.remove('flute')
box_2.append('flute')

# Swap the speaker in Box 8 with the cow in Box 12
box_8.remove('speaker')
box_12.remove('cow')
box_8.append('cow')
box_12.append('speaker')

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
print("Box 12:", box_12)