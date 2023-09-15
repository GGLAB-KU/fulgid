box_0 = ['cat', 'basket', 'comb', 'submarine']
box_1 = ['horse', 'toaster', 'shampoo', 'bowl', 'lock']
box_2 = ['mask', 'crown']
box_3 = []
box_4 = ['laptop', 'violin', 'coral']
box_5 = ['umbrella', 'butterfly']
box_6 = ['tiger', 'jungle']

# Replace the tiger with the fridge in Box 6
box_6.remove('tiger')
box_6.append('fridge')

# Move the fridge and the jungle from Box 6 to Box 5
box_6.remove('fridge')
box_5.extend(['fridge', 'jungle'])

# Put the whistle and the fork into Box 4
box_4.extend(['whistle', 'fork'])

# Move the lock and the toaster from Box 1 to Box 6
box_1.remove('lock')
box_1.remove('toaster')
box_6.extend(['lock', 'toaster'])

# Remove the whistle and the laptop from Box 4
box_4.remove('whistle')
box_4.remove('laptop')

# Remove the toaster from Box 6
box_6.remove('toaster')

# Swap the butterfly in Box 5 with the horse in Box 1
box_5.remove('butterfly')
box_1.remove('horse')
box_5.append('horse')
box_1.append('butterfly')

# Empty Box 6
box_6.clear()

# Move the horse and the umbrella from Box 5 to Box 4
box_5.remove('horse')
box_5.remove('umbrella')
box_4.extend(['horse', 'umbrella'])

# Put the shark and the flower and the pan into Box 6
box_6.extend(['shark', 'flower', 'pan'])

# Remove the shampoo from Box 1
box_1.remove('shampoo')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)