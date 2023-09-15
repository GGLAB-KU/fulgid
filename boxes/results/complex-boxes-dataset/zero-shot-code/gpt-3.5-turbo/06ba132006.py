box_0 = ['coat', 'sandals']
box_1 = ['toothpaste', 'ring', 'toaster', 'candle', 'pen']
box_2 = ['jungle']
box_3 = ['meteor', 'puzzle']
box_4 = ['lightning']
box_5 = ['cloud', 'coin', 'pot', 'tie', 'planet']
box_6 = ['ocean', 'dress', 'bird', 'bear']
box_7 = ['storm', 'submarine', 'zipper']
box_8 = ['leaf', 'necklace', 'motorcycle', 'wig', 'apple']
box_9 = ['key', 'frame']
box_10 = ['swimsuit', 'seaweed', 'elephant']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

# Move the puzzle from Box 3 to Box 6
box_6.append(box_3.pop(box_3.index('puzzle')))

# Empty Box 5
box_5.clear()

# Swap the jungle in Box 2 with the meteor in Box 3
box_2.append(box_3.pop(box_3.index('meteor')))
box_3.append(box_2.pop(box_2.index('jungle')))

# Move the meteor from Box 2 to Box 9
box_9.append(box_2.pop(box_2.index('meteor')))

# Move the sandals and the coat from Box 0 to Box 8
box_8.extend([box_0.pop(box_0.index('sandals')), box_0.pop(box_0.index('coat'))])

# Remove the jungle from Box 3
box_3.remove('jungle')

# Move the sandals and the apple from Box 8 to Box 10
box_10.extend([box_8.pop(box_8.index('sandals')), box_8.pop(box_8.index('apple'))])

# Swap the necklace in Box 8 with the sandals in Box 10
box_8.append(box_10.pop(box_10.index('necklace')))
box_10.append(box_8.pop(box_8.index('sandals')))

# Remove the meteor from Box 9
box_9.remove('meteor')

# Swap the key in Box 9 with the lightning in Box 4
box_9.append(box_4.pop(box_4.index('lightning')))
box_4.append(box_9.pop(box_9.index('key')))

# Empty Box 9
box_9.clear()

# Put the leaf and the pants into Box 6
box_6.extend(['leaf', 'pants'])

# Put the perfume and the coral into Box 3
box_3.extend(['perfume', 'coral'])

# Replace the motorcycle and the coat with the book and the watch in Box 8
box_8.extend(['book', 'watch'])
box_8.remove('motorcycle')
box_8.remove('coat')

# Swap the ring in Box 1 with the necklace in Box 10
box_1.append(box_10.pop(box_10.index('ring')))
box_10.append(box_1.pop(box_1.index('necklace')))

# Move the zipper from Box 7 to Box 5
box_5.append(box_7.pop(box_7.index('zipper')))

print_boxes()