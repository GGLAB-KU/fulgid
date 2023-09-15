box_0 = ['toothpaste', 'river']
box_1 = ['basket']
box_2 = ['makeup', 'dog', 'watch', 'jacket', 'toothbrush']
box_3 = ['desert', 'rocket', 'fridge']
box_4 = ['branch', 'necklace', 'motorcycle', 'telescope']
box_5 = ['skirt']
box_6 = ['puzzle', 'cat']
box_7 = ['shark', 'vase', 'soap', 'cow', 'toaster']
box_8 = []
box_9 = ['boot']
box_10 = ['jungle', 'flower']
box_11 = ['shoes', 'ship', 'needle', 'controller']

# Move the jungle and the flower from Box 10 to Box 1
box_1.extend(box_10)
box_10.clear()

# Replace the branch with the mask in Box 4
box_4.remove('branch')
box_4.append('mask')

# Put the pillow and the lipstick and the comet into Box 7
box_7.extend(['pillow', 'lipstick', 'comet'])

# Put the perfume and the doll into Box 8
box_8.extend(['perfume', 'doll'])

# Swap the perfume in Box 8 with the mask in Box 4
box_8.remove('perfume')
box_8.append('mask')
box_4.remove('mask')
box_4.append('perfume')

# Swap the lipstick in Box 7 with the mask in Box 8
box_7.remove('lipstick')
box_7.append('mask')
box_8.remove('mask')
box_8.append('lipstick')

# Remove the toothpaste and the river from Box 0
box_0.clear()

# Swap the motorcycle in Box 4 with the lipstick in Box 8
box_4.remove('motorcycle')
box_4.append('lipstick')
box_8.remove('lipstick')
box_8.append('motorcycle')

# Put the meteor and the wig and the necklace into Box 1
box_1.extend(['meteor', 'wig', 'necklace'])

# Put the cloud and the fish and the thread into Box 9
box_9.extend(['cloud', 'fish', 'thread'])

# Put the forest and the river and the pants into Box 8
box_8.extend(['forest', 'river', 'pants'])

# Move the mask and the cow and the shark from Box 7 to Box 4
box_4.extend(['mask', 'cow', 'shark'])
box_7.remove('mask')
box_7.remove('cow')
box_7.remove('shark')

# Remove the needle and the controller from Box 11
box_11.remove('needle')
box_11.remove('controller')

# Move the cat from Box 6 to Box 0
box_0.append('cat')
box_6.remove('cat')

# Put the towel and the clock into Box 6
box_6.extend(['towel', 'clock'])

# Move the towel and the clock from Box 6 to Box 3
box_3.extend(['towel', 'clock'])
box_6.remove('towel')
box_6.remove('clock')

# Swap the jacket in Box 2 with the toaster in Box 7
box_2.remove('jacket')
box_2.append('toaster')
box_7.remove('toaster')
box_7.append('jacket')

# Put the skirt into Box 3
box_3.append('skirt')

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