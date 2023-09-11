# Initial state of boxes
boxes = {
    0: ['swimsuit', 'belt', 'clock'],
    1: [],
    2: ['toothpaste'],
    3: ['shark', 'headphone', 'skirt'],
    4: ['mixer', 'drum', 'sculpture', 'fish'],
    5: [],
    6: ['fork', 'whistle', 'key', 'butterfly', 'cup']
}

# Put the brush and the snow into Box 0.
boxes[0].append('brush')
boxes[0].append('snow')

# Move the toothpaste from Box 2 to Box 3.
boxes[2].remove('toothpaste')
boxes[3].append('toothpaste')

# Put the paint into Box 0.
boxes[0].append('paint')

# Swap the clock in Box 0 with the headphone in Box 3.
boxes[0].remove('clock')
boxes[3].remove('headphone')
boxes[0].append('headphone')
boxes[3].append('clock')

# Swap the skirt in Box 3 with the paint in Box 0.
boxes[3].remove('skirt')
boxes[0].remove('paint')
boxes[3].append('paint')
boxes[0].append('skirt')

# Remove the sculpture and the mixer and the drum from Box 4.
items_to_remove = ['sculpture', 'mixer', 'drum']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the brush from Box 0.
boxes[0].remove('brush')

# Replace the cup and the butterfly with the tiger and the towel in Box 6.
boxes[6].remove('cup')
boxes[6].remove('butterfly')
boxes[6].append('tiger')
boxes[6].append('towel')

# Replace the tiger and the towel and the key with the pillow and the battery and the cat in Box 6.
boxes[6].remove('tiger')
boxes[6].remove('towel')
boxes[6].remove('key')
boxes[6].append('pillow')
boxes[6].append('battery')
boxes[6].append('cat')

# Swap the paint in Box 3 with the pillow in Box 6.
boxes[3].remove('paint')
boxes[6].remove('pillow')
boxes[3].append('pillow')
boxes[6].append('paint')

# Put the glove into Box 6.
boxes[6].append('glove')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")