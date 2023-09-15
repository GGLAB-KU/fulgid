box = {
    0: ['battery'],
    1: [],
    2: ['telescope'],
    3: ['spoon'],
    4: ['laptop'],
    5: ['shelf'],
    6: ['elephant', 'soap'],
    7: [],
    8: ['ring', 'coin', 'mixer'],
    9: [],
    10: [],
    11: ['note'],
    12: ['bowl', 'usb', 'moon', 'bag', 'bear'],
    13: ['candle', 'dice', 'cow']
}

def print_box_contents():
    for index, items in box.items():
        print(f"Box {index}: {items}")

# Remove the candle, cow, and dice from Box 13
box[13].remove('candle')
box[13].remove('dice')
box[13].remove('cow')

# Put the towel and tree into Box 13
box[13].extend(['towel', 'tree'])

# Move the bag and usb from Box 12 to Box 11
box[11].extend(box[12].pop(box[12].index('bag')))
box[11].extend(box[12].pop(box[12].index('usb')))

# Move the bear from Box 12 to Box 10
box[10].extend(box[12].pop(box[12].index('bear')))

# Move the soap and elephant from Box 6 to Box 11
box[11].extend(box[6].pop(box[6].index('soap')))
box[11].extend(box[6].pop(box[6].index('elephant')))

# Move the spoon from Box 3 to Box 0
box[0].extend(box[3].pop(box[3].index('spoon')))

# Put the console, plane, and pot into Box 3
box[3].extend(['console', 'plane', 'pot'])

# Empty Box 13
box[13] = []

# Put the microwave into Box 11
box[11].extend(['microwave'])

# Remove the bear from Box 10
box[10] = []

# Remove the mixer and ring from Box 8
box[8].remove('mixer')
box[8].remove('ring')

# Replace the spoon and battery with the puzzle and mirror in Box 0
box[0] = ['puzzle', 'mirror']

# Put the brush, flute, and pot into Box 13
box[13].extend(['brush', 'flute', 'pot'])

# Replace the brush with the lipstick in Box 13
box[13].remove('brush')
box[13].append('lipstick')

# Swap the moon in Box 12 with the puzzle in Box 0
box[0], box[12] = box[12], box[0]

# Move the shelf from Box 5 to Box 4
box[4].extend(box[5].pop(box[5].index('shelf')))

# Swap the moon in Box 0 with the coin in Box 8
box[0], box[8] = box[8], box[0]

# Remove the laptop and shelf from Box 4
box[4] = []

# Swap the flute in Box 13 with the moon in Box 8
box[8], box[13] = box[13], box[8]

# Move the puzzle from Box 12 to Box 4
box[4].extend(box[12].pop(box[12].index('puzzle')))

# Move the flute from Box 8 to Box 7
box[7].extend(box[8].pop(box[8].index('flute')))

# Print the contents of each box
print_box_contents()