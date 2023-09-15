box_0 = ['jungle', 'submarine', 'sandals']
box_1 = ['bear', 'usb', 'card', 'sock']
box_2 = ['motorcycle', 'bird']
box_3 = ['swimsuit']
box_4 = ['zipper']
box_5 = ['sun', 'mountain', 'razor']
box_6 = ['tiger']
box_7 = ['bus', 'fork', 'butterfly']
box_8 = ['soap', 'meteor', 'lipstick', 'toaster', 'guitar']
box_9 = ['oven']

def print_boxes():
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

# Put the meteor and the comet and the soap into Box 4
box_4.extend(['meteor', 'comet', 'soap'])

# Put the cow into Box 9
box_9.append('cow')

# Remove the bus and the fork and the butterfly from Box 7
box_7.remove('bus')
box_7.remove('fork')
box_7.remove('butterfly')

# Remove the comet from Box 4
box_4.remove('comet')

# Remove the toaster from Box 8
box_8.remove('toaster')

# Move the submarine and the jungle and the sandals from Box 0 to Box 4
box_4.extend(box_0)
box_0.clear()

# Put the belt and the harmonica and the pot into Box 1
box_1.extend(['belt', 'harmonica', 'pot'])

# Remove the swimsuit from Box 3
box_3.remove('swimsuit')

# Move the meteor and the zipper and the jungle from Box 4 to Box 7
box_7.extend(['meteor', 'zipper', 'jungle'])
box_4.clear()

# Swap the sun in Box 5 with the oven in Box 9
box_5.remove('sun')
box_9.remove('oven')
box_5.append('oven')
box_9.append('sun')

# Move the sandals and the submarine from Box 4 to Box 0
box_0.extend(['sandals', 'submarine'])
box_4.clear()

# Move the lipstick from Box 8 to Box 7
box_7.append('lipstick')
box_8.remove('lipstick')

# Empty Box 5
box_5.clear()

# Move the meteor from Box 7 to Box 0
box_0.append('meteor')
box_7.remove('meteor')

# Move the usb and the harmonica and the belt from Box 1 to Box 6
box_6.extend(['usb', 'harmonica', 'belt'])
box_1.remove('usb')
box_1.remove('harmonica')
box_1.remove('belt')

# Print the final state of the boxes
print_boxes()