# Initial state of boxes
boxes = {
    0: ['sandals', 'shorts'],
    1: [],
    2: ['oven', 'pen'],
    3: ['cloud'],
    4: ['star', 'harmonica']
}

# Put the star into Box 3.
boxes[3].append('star')

# Swap the sandals in Box 0 with the harmonica in Box 4.
boxes[0].remove('sandals')
boxes[4].remove('harmonica')
boxes[0].append('harmonica')
boxes[4].append('sandals')

# Put the lipstick and the bowl into Box 1.
boxes[1].append('lipstick')
boxes[1].append('bowl')

# Replace the harmonica with the car in Box 0.
boxes[0].remove('harmonica')
boxes[0].append('car')

# Swap the car in Box 0 with the pen in Box 2.
boxes[0].remove('car')
boxes[2].remove('pen')
boxes[0].append('pen')
boxes[2].append('car')

# Put the makeup and the mixer and the tiger into Box 1.
boxes[1].append('makeup')
boxes[1].append('mixer')
boxes[1].append('tiger')

# Swap the car in Box 2 with the tiger in Box 1.
boxes[2].remove('car')
boxes[1].remove('tiger')
boxes[2].append('tiger')
boxes[1].append('car')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")