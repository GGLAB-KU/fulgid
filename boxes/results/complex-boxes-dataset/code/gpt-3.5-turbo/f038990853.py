# Initial state of boxes
boxes = {
    0: ['crown'],
    1: ['harmonica', 'seaweed', 'grass'],
    2: ['helmet'],
    3: ['rain', 'wallet'],
    4: ['usb', 'bicycle', 'clock', 'dice', 'cat'],
    5: ['chair', 'tiger', 'lightning', 'zipper']
}

# Remove the chair and the lightning from Box 5.
boxes[5].remove('chair')
boxes[5].remove('lightning')

# Put the fork and the usb into Box 2.
boxes[2].append('fork')
boxes[2].append('usb')

# Swap the rain in Box 3 with the zipper in Box 5.
boxes[3].remove('rain')
boxes[5].remove('zipper')
boxes[3].append('zipper')
boxes[5].append('rain')

# Put the towel and the book into Box 0.
boxes[0].append('towel')
boxes[0].append('book')

# Remove the wallet and the zipper from Box 3.
boxes[3].remove('wallet')
boxes[3].remove('zipper')

# Move the helmet from Box 2 to Box 3.
boxes[2].remove('helmet')
boxes[3].append('helmet')

# Swap the seaweed in Box 1 with the cat in Box 4.
boxes[1].remove('seaweed')
boxes[4].remove('cat')
boxes[1].append('cat')
boxes[4].append('seaweed')

# Swap the book in Box 0 with the helmet in Box 3.
boxes[0].remove('book')
boxes[3].remove('helmet')
boxes[0].append('helmet')
boxes[3].append('book')

# Swap the bicycle in Box 4 with the grass in Box 1.
boxes[4].remove('bicycle')
boxes[1].remove('grass')
boxes[4].append('grass')
boxes[1].append('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")