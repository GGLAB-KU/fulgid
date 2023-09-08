# Initial state of boxes
boxes = {
    0: ['shark', 'tree', 'zipper', 'guitar'],
    1: ['dress', 'cloud', 'violin'],
    2: ['thunder', 'bird', 'grinder', 'pan'],
    3: ['microscope', 'pants', 'makeup', 'wig', 'charger'],
    4: ['coin', 'lock', 'book', 'cow', 'river'],
    5: ['whistle', 'mask'],
    6: [],
    7: ['toaster'],
    8: [],
    9: ['pillow', 'flower', 'lightning'],
    10: ['ring', 'dice', 'branch', 'candle']
}

# Replace the candle and the branch with the shoe and the lightning in Box 10.
boxes[10].remove('candle')
boxes[10].remove('branch')
boxes[10].append('shoe')
boxes[10].append('lightning')

# Put the guitar and the lightning and the game into Box 0.
boxes[0].append('guitar')
boxes[0].append('lightning')
boxes[0].append('game')

# Move the whistle from Box 5 to Box 10.
boxes[5].remove('whistle')
boxes[10].append('whistle')

# Put the fridge and the ring into Box 3.
boxes[3].append('fridge')
boxes[3].append('ring')

# Remove the dress from Box 1.
boxes[1].remove('dress')

# Replace the cloud and the violin with the laptop and the jacket in Box 1.
boxes[1].remove('cloud')
boxes[1].remove('violin')
boxes[1].append('laptop')
boxes[1].append('jacket')

# Replace the mask with the usb in Box 5.
boxes[5].remove('mask')
boxes[5].append('usb')

# Replace the grinder and the thunder with the frame and the wire in Box 2.
boxes[2].remove('grinder')
boxes[2].remove('thunder')
boxes[2].append('frame')
boxes[2].append('wire')

# Remove the makeup and the ring from Box 3.
boxes[3].remove('makeup')
boxes[3].remove('ring')

# Put the lipstick into Box 7.
boxes[7].append('lipstick')

# Replace the lock and the cow with the snow and the bag in Box 4.
boxes[4].remove('lock')
boxes[4].remove('cow')
boxes[4].append('snow')
boxes[4].append('bag')

# Remove the coin and the bag and the snow from Box 4.
boxes[4].remove('coin')
boxes[4].remove('bag')
boxes[4].remove('snow')

# Move the shark from Box 0 to Box 4.
boxes[0].remove('shark')
boxes[4].append('shark')

# Swap the microscope in Box 3 with the lipstick in Box 7.
boxes[3].remove('microscope')
boxes[7].remove('lipstick')
boxes[3].append('lipstick')
boxes[7].append('microscope')

# Put the forest into Box 4.
boxes[4].append('forest')

# Empty Box 1.
boxes[1] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")