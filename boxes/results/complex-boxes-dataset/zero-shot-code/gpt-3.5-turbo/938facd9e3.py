box_0 = ['dolphin', 'coat', 'flute', 'helmet']
box_1 = ['jungle', 'grinder', 'planet']
box_2 = ['pillow', 'horse']
box_3 = []
box_4 = ['boot', 'comb', 'candle']
box_5 = ['boat', 'branch', 'lipstick']
box_6 = []
box_7 = ['shorts', 'magnet', 'keyboard']

# Remove the pillow from Box 2
box_2.remove('pillow')

# Put the polish and the candle into Box 2
box_2.extend(['polish', 'candle'])

# Swap the candle in Box 4 with the keyboard in Box 7
box_4.remove('candle')
box_7.remove('keyboard')
box_4.append('keyboard')
box_7.append('candle')

# Replace the shorts and the magnet with the console and the gloves in Box 7
box_7.remove('shorts')
box_7.remove('magnet')
box_7.extend(['console', 'gloves'])

# Remove the grinder from Box 1
box_1.remove('grinder')

# Move the branch and the lipstick from Box 5 to Box 2
box_5.remove('branch')
box_5.remove('lipstick')
box_2.extend(['branch', 'lipstick'])

# Put the scarf and the necklace into Box 4
box_4.extend(['scarf', 'necklace'])

# Put the piano and the earring and the spoon into Box 6
box_6.extend(['piano', 'earring', 'spoon'])

# Remove the boat from Box 5
box_5.remove('boat')

# Put the frame and the wig and the horse into Box 6
box_6.extend(['frame', 'wig', 'horse'])

# Replace the scarf and the comb with the tiger and the branch in Box 4
box_4.remove('scarf')
box_4.remove('comb')
box_4.extend(['tiger', 'branch'])

# Put the thunder into Box 2
box_2.append('thunder')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)