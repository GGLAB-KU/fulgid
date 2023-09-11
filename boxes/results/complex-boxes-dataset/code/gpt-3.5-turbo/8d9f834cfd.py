# Initial state of boxes
boxes = {
    0: ['skirt', 'toaster', 'telescope'],
    1: ['horse', 'umbrella', 'bicycle'],
    2: ['lion', 'puzzle', 'lightning', 'swimsuit'],
    3: ['watch', 'candle'],
    4: ['jacket', 'helmet', 'motorcycle', 'pants', 'bell']
}

# Swap the swimsuit in Box 2 with the telescope in Box 0.
boxes[0].remove('telescope')
boxes[2].remove('swimsuit')
boxes[0].append('swimsuit')
boxes[2].append('telescope')

# Swap the watch in Box 3 with the bicycle in Box 1.
boxes[1].remove('bicycle')
boxes[3].remove('watch')
boxes[1].append('watch')
boxes[3].append('bicycle')

# Replace the bicycle with the boot in Box 3.
boxes[3].remove('bicycle')
boxes[3].append('boot')

# Put the grinder and the glove into Box 3.
boxes[3].append('grinder')
boxes[3].append('glove')

# Replace the grinder and the boot and the candle with the laptop and the earring and the makeup in Box 3.
boxes[3].remove('grinder')
boxes[3].remove('boot')
boxes[3].remove('candle')
boxes[3].append('laptop')
boxes[3].append('earring')
boxes[3].append('makeup')

# Put the table into Box 3.
boxes[3].append('table')

# Move the umbrella from Box 1 to Box 4.
boxes[1].remove('umbrella')
boxes[4].append('umbrella')

# Swap the makeup in Box 3 with the skirt in Box 0.
boxes[0].remove('skirt')
boxes[3].remove('makeup')
boxes[0].append('makeup')
boxes[3].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")