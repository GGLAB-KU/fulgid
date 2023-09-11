# Initial state of boxes
boxes = {
    0: ['umbrella', 'comb', 'phone', 'lightning', 'shirt'],
    1: ['cloud', 'train', 'jungle'],
    2: ['meteor', 'laptop', 'candle', 'towel'],
    3: ['comet', 'flower', 'planet', 'chair']
}

# Remove the train from Box 1.
boxes[1].remove('train')

# Replace the cloud and the jungle with the card and the piano in Box 1.
boxes[1].remove('cloud')
boxes[1].remove('jungle')
boxes[1].append('card')
boxes[1].append('piano')

# Remove the meteor and the candle from Box 2.
boxes[2].remove('meteor')
boxes[2].remove('candle')

# Remove the towel from Box 2.
boxes[2].remove('towel')

# Move the piano from Box 1 to Box 0.
boxes[1].remove('piano')
boxes[0].append('piano')

# Replace the laptop with the microscope in Box 2.
boxes[2].remove('laptop')
boxes[2].append('microscope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")