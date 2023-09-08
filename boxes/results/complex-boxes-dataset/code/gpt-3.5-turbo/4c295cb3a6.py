# Initial state of boxes
boxes = {
    0: [],
    1: ['pen', 'swimsuit'],
    2: ['lipstick', 'comet'],
    3: ['pillow'],
    4: ['spoon', 'helmet', 'scissors', 'train', 'freezer']
}

# Remove the pen from Box 1.
boxes[1].remove('pen')

# Move the comet and the lipstick from Box 2 to Box 3.
boxes[2].remove('comet')
boxes[2].remove('lipstick')
boxes[3].append('comet')
boxes[3].append('lipstick')

# Swap the scissors in Box 4 with the swimsuit in Box 1.
boxes[4].remove('scissors')
boxes[1].remove('swimsuit')
boxes[4].append('swimsuit')
boxes[1].append('scissors')

# Remove the scissors from Box 1.
boxes[1].remove('scissors')

# Swap the pillow in Box 3 with the helmet in Box 4.
boxes[3].remove('pillow')
boxes[4].remove('helmet')
boxes[3].append('helmet')
boxes[4].append('pillow')

# Swap the swimsuit in Box 4 with the lipstick in Box 3.
boxes[4].remove('swimsuit')
boxes[3].remove('lipstick')
boxes[4].append('lipstick')
boxes[3].append('swimsuit')

# Replace the lipstick and the pillow and the train with the butterfly and the lock and the microscope in Box 4.
boxes[4].remove('lipstick')
boxes[4].remove('pillow')
boxes[4].remove('train')
boxes[4].append('butterfly')
boxes[4].append('lock')
boxes[4].append('microscope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")