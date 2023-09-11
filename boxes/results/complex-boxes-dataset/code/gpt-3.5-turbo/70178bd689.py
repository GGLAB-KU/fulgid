# Initial state of boxes
boxes = {
    0: ['whistle', 'lamp', 'mask', 'keyboard'],
    1: ['mixer', 'sock', 'brush', 'bicycle'],
    2: ['rocket'],
    3: ['toaster', 'lightning', 'pillow', 'moon'],
    4: [],
    5: ['butterfly', 'jungle'],
    6: ['book', 'phone'],
    7: ['dress', 'umbrella', 'oven', 'jacket'],
    8: ['microwave']
}

# Swap the microwave in Box 8 with the butterfly in Box 5.
boxes[8], boxes[5] = boxes[5], boxes[8]

# Remove the brush and the bicycle from Box 1.
boxes[1].remove('brush')
boxes[1].remove('bicycle')

# Replace the mixer with the microwave in Box 1.
boxes[1].remove('mixer')
boxes[1].append('microwave')

# Remove the book from Box 6.
boxes[6].remove('book')

# Remove the keyboard from Box 0.
boxes[0].remove('keyboard')

# Replace the pillow with the branch in Box 3.
boxes[3].remove('pillow')
boxes[3].append('branch')

# Replace the rocket with the rain in Box 2.
boxes[2].remove('rocket')
boxes[2].append('rain')

# Remove the dress from Box 7.
boxes[7].remove('dress')

# Remove the rain from Box 2.
boxes[2].remove('rain')

# Remove the microwave from Box 5.
boxes[5].remove('microwave')

# Move the butterfly from Box 8 to Box 3.
boxes[8].remove('butterfly')
boxes[3].append('butterfly')

# Empty Box 6.
boxes[6] = []

# Remove the jacket and the oven and the umbrella from Box 7.
boxes[7].remove('jacket')
boxes[7].remove('oven')
boxes[7].remove('umbrella')

# Remove the sock and the microwave from Box 1.
boxes[1].remove('sock')
boxes[1].remove('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")