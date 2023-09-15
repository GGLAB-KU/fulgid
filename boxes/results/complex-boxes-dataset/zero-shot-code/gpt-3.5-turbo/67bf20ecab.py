box_0 = ['pot', 'controller']
box_1 = ['sculpture', 'sandals', 'magnet']
box_2 = ['fork']
box_3 = ['apple', 'helmet', 'dog', 'flower', 'beach']
box_4 = ['bell', 'note', 'watch', 'toaster']
box_5 = ['game', 'bicycle', 'desert']
box_6 = ['tiger', 'gloves', 'polish']
box_7 = ['headphone', 'doll', 'battery', 'branch']
box_8 = ['belt', 'comb', 'shelf', 'dice']

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

# Put the starfish into Box 4
box_4.append('starfish')

# Replace the game and the desert with the thunder and the gloves in Box 5
box_5.remove('game')
box_5.remove('desert')
box_5.extend(['thunder', 'gloves'])

# Move the sandals and the sculpture and the magnet from Box 1 to Box 3
box_3.extend(box_1)
box_1.clear()

# Put the jacket and the thread and the card into Box 1
box_1.extend(['jacket', 'thread', 'card'])

# Replace the thread and the card with the flower and the coin in Box 1
box_1.remove('thread')
box_1.remove('card')
box_1.extend(['flower', 'coin'])

# Put the lion and the mountain into Box 3
box_3.extend(['lion', 'mountain'])

# Remove the controller from Box 0
box_0.remove('controller')

# Replace the fork with the towel in Box 2
box_2.remove('fork')
box_2.append('towel')

# Remove the lion and the sandals from Box 3
box_3.remove('lion')
box_3.remove('sandals')

# Move the bell and the watch and the note from Box 4 to Box 3
box_3.extend(box_4)
box_4.clear()

# Put the necklace and the wallet and the battery into Box 5
box_5.extend(['necklace', 'wallet', 'battery'])

# Remove the starfish and the toaster from Box 4
box_4.remove('starfish')
box_4.remove('toaster')

# Replace the belt and the shelf with the note and the fork in Box 8
box_8.remove('belt')
box_8.remove('shelf')
box_8.extend(['note', 'fork'])

# Move the comb and the note from Box 8 to Box 5
box_5.extend(['comb', 'note'])
box_8.remove('comb')
box_8.remove('note')

print_boxes()