# Initial contents of the boxes
boxes = {
    0: ['wallet', 'fork', 'novel', 'coat'],
    1: ['candle', 'fork'],
    2: ['uniform'],
    3: ['eraser', 'fiction', 'biography', 'adventure'],
    4: ['basket'],
    5: ['cart', 'envelope', 'guitar', 'hat'],
    6: ['biography', 'book'],
    7: ['coverage', 'biography', 'spoon']
}

# Empty Box 0
boxes[0] = []

# Empty Box 5
boxes[5] = []

# Remove the basket from Box 4
boxes[4].remove('basket')

# Put the spoon into Box 3
boxes[3].append('spoon')

# Replace the fork with the knife in Box 1
index_fork = boxes[1].index('fork')
boxes[1][index_fork] = 'knife'


# Move the candle from Box 1 to Box 0
boxes[1].remove('candle')
boxes[0].append('candle')

# Swap the uniform in Box 2 with the candle in Box 0
index_candle = boxes[0].index('candle')
index_uniform = boxes[2].index('uniform')

boxes[0][index_candle] = 'uniform'
boxes[2][index_uniform] = 'candle'

# Remove the book from Box 6
boxes[6].remove('book')

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")
