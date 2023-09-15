boxes = [[], [], [], [], [], [], []]

# Initial state
boxes[0] = ['card', 'shirt', 'ring', 'fish']
boxes[1] = ['shorts', 'helmet', 'desert']
boxes[2] = ['piano', 'blender', 'cloud']
boxes[3] = ['book', 'star', 'lightning', 'thunder']
boxes[4] = []
boxes[5] = ['microwave', 'lock', 'branch']
boxes[6] = ['comet', 'butterfly']

# Remove items from Box 2
boxes[2].remove('cloud')
boxes[2].remove('blender')
boxes[2].remove('piano')

# Remove comet from Box 6
boxes[6].remove('comet')

# Move card from Box 0 to Box 1
boxes[1].append('card')
boxes[0].remove('card')

# Move card from Box 1 to Box 4
boxes[4].append('card')
boxes[1].remove('card')

# Move shirt from Box 0 to Box 5
boxes[5].append('shirt')
boxes[0].remove('shirt')

# Swap lock in Box 5 with helmet in Box 1
boxes[5].remove('lock')
boxes[1].remove('helmet')
boxes[5].append('helmet')
boxes[1].append('lock')

# Move butterfly from Box 6 to Box 1
boxes[1].append('butterfly')
boxes[6].remove('butterfly')

# Remove ring from Box 0
boxes[0].remove('ring')

# Remove lock from Box 1
boxes[1].remove('lock')

# Put sandals and lipstick into Box 4
boxes[4].extend(['sandals', 'lipstick'])

# Print the final state of the boxes
for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")