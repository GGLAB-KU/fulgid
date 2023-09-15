box_0 = ['usb', 'bell', 'sculpture', 'telescope']
box_1 = ['guitar', 'phone', 'cat', 'cup']
box_2 = ['bag', 'jungle', 'mountain']
box_3 = ['leaf']
box_4 = ['tie', 'book']
box_5 = ['island']
box_6 = ['umbrella', 'zipper', 'polish', 'violin']

# Replace the book with the shark in Box 4
box_4.remove('book')
box_4.append('shark')

# Move the toaster from Box 5 to Box 0
box_0.append(box_5.pop(box_5.index('toaster')))

# Move the violin and the umbrella from Box 6 to Box 2
box_2.extend([box_6.pop(box_6.index('violin')), box_6.pop(box_6.index('umbrella'))])

# Replace the zipper with the blanket in Box 6
box_6[box_6.index('zipper')] = 'blanket'

# Put the toothbrush and the jacket into Box 3
box_3.extend(['toothbrush', 'jacket'])

# Move the guitar and the cup and the cat from Box 1 to Box 5
box_5.extend([box_1.pop(box_1.index('guitar')), box_1.pop(box_1.index('cup')), box_1.pop(box_1.index('cat'))])

# Move the shark from Box 4 to Box 5
box_5.append(box_4.pop(box_4.index('shark')))

# Put the coral and the paint and the ring into Box 4
box_4.extend(['coral', 'paint', 'ring'])

# Put the ring into Box 4
box_4.append('ring')

# Move the polish from Box 6 to Box 4
box_4.append(box_6.pop(box_6.index('polish')))

# Put the flute into Box 0
box_0.append('flute')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)