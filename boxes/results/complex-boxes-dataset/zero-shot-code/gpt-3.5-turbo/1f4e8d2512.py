box_0 = ['thunder']
box_1 = ['rain']
box_2 = ['dolphin', 'belt', 'rock']
box_3 = ['fish']
box_4 = ['dress', 'piano', 'motorcycle', 'horse', 'toothpaste']
box_5 = []
box_6 = ['speaker', 'pot', 'harmonica', 'polish']
box_7 = ['magnet', 'lock']
box_8 = ['button', 'pan']
box_9 = ['phone', 'watch', 'skirt']
box_10 = ['bell', 'necklace', 'pillow', 'desert', 'console']
box_11 = ['fridge', 'ocean', 'tiger', 'laptop']
box_12 = ['blender', 'razor', 'lipstick', 'glove']

# Move the harmonica and the pot and the speaker from Box 6 to Box 2
box_2.extend([box_6.pop(box_6.index('harmonica'))])
box_2.extend([box_6.pop(box_6.index('pot'))])
box_2.extend([box_6.pop(box_6.index('speaker'))])

# Replace the speaker and the dolphin and the rock with the star and the puzzle and the fridge in Box 2
box_2.remove('speaker')
box_2.remove('dolphin')
box_2.remove('rock')
box_2.extend(['star', 'puzzle', 'fridge'])

# Remove the belt and the puzzle and the fridge from Box 2
box_2.remove('belt')
box_2.remove('puzzle')
box_2.remove('fridge')

# Swap the magnet in Box 7 with the harmonica in Box 2
box_7.extend([box_2.pop(box_2.index('magnet'))])
box_2.extend([box_7.pop(box_7.index('harmonica'))])

# Remove the fish from Box 3
box_3.remove('fish')

# Put the elephant and the fork into Box 11
box_11.extend(['elephant', 'fork'])

# Put the gloves and the thread and the crown into Box 5
box_5.extend(['gloves', 'thread', 'crown'])

# Move the skirt from Box 9 to Box 8
box_8.extend([box_9.pop(box_9.index('skirt'))])

# Put the mountain and the pen into Box 6
box_6.extend(['mountain', 'pen'])

# Replace the glove and the blender with the ring and the train in Box 12
box_12.remove('glove')
box_12.remove('blender')
box_12.extend(['ring', 'train'])

# Put the dog and the drum into Box 12
box_12.extend(['dog', 'drum'])

# Replace the dog with the magnet in Box 12
box_12.remove('dog')
box_12.extend(['magnet'])

# Move the thunder from Box 0 to Box 10
box_10.extend([box_0.pop(box_0.index('thunder'))])

# Swap the watch in Box 9 with the gloves in Box 5
box_9.extend([box_5.pop(box_5.index('gloves'))])
box_5.extend([box_9.pop(box_9.index('watch'))])

# Empty Box 5
box_5 = []

# Remove the ring from Box 12
box_12.remove('ring')

# Remove the magnet from Box 2
box_2.remove('magnet')

# Remove the console and the pillow and the desert from Box 10
box_10.remove('console')
box_10.remove('pillow')
box_10.remove('desert')

# Put the elephant and the forest into Box 5
box_5.extend(['elephant', 'forest'])

# Remove the mountain and the polish from Box 6
box_6.remove('mountain')
box_6.remove('polish')

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