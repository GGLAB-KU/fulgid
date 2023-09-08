# Initial state of boxes
boxes = {
    0: ['dolphin', 'coat', 'flute', 'helmet'],
    1: ['jungle', 'grinder', 'planet'],
    2: ['pillow', 'horse'],
    3: [],
    4: ['boot', 'comb', 'candle'],
    5: ['boat', 'branch', 'lipstick'],
    6: [],
    7: ['shorts', 'magnet', 'keyboard']
}

# Remove the pillow from Box 2.
boxes[2].remove('pillow')

# Put the polish and the candle into Box 2.
boxes[2].append('polish')
boxes[2].append('candle')

# Swap the candle in Box 4 with the keyboard in Box 7.
boxes[4].remove('candle')
boxes[7].remove('keyboard')
boxes[4].append('keyboard')
boxes[7].append('candle')

# Replace the shorts and the magnet with the console and the gloves in Box 7.
boxes[7].remove('shorts')
boxes[7].remove('magnet')
boxes[7].append('console')
boxes[7].append('gloves')

# Remove the grinder from Box 1.
boxes[1].remove('grinder')

# Move the branch and the lipstick from Box 5 to Box 2.
items_to_move = ['branch', 'lipstick']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Put the scarf and the necklace into Box 4.
boxes[4].append('scarf')
boxes[4].append('necklace')

# Put the piano and the earring and the spoon into Box 6.
boxes[6].append('piano')
boxes[6].append('earring')
boxes[6].append('spoon')

# Remove the boat from Box 5.
boxes[5].remove('boat')

# Put the frame and the wig and the horse into Box 6.
boxes[6].append('frame')
boxes[6].append('wig')
boxes[6].append('horse')

# Replace the scarf and the comb with the tiger and the branch in Box 4.
boxes[4].remove('scarf')
boxes[4].remove('comb')
boxes[4].append('tiger')
boxes[4].append('branch')

# Put the thunder into Box 2.
boxes[2].append('thunder')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")