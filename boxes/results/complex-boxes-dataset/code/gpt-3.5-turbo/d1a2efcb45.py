# Initial state of boxes
boxes = {
    0: ['clock'],
    1: ['card', 'star', 'bracelet'],
    2: ['freezer', 'lightning', 'skirt', 'fish', 'razor'],
    3: ['coin', 'boot', 'harmonica'],
    4: ['train'],
    5: ['scarf']
}

# Put the lion into Box 4.
boxes[4].append('lion')

# Move the clock from Box 0 to Box 3.
boxes[0].remove('clock')
boxes[3].append('clock')

# Replace the fish and the lightning with the pot and the scissors in Box 2.
boxes[2].remove('fish')
boxes[2].remove('lightning')
boxes[2].append('pot')
boxes[2].append('scissors')

# Move the scarf from Box 5 to Box 0.
boxes[5].remove('scarf')
boxes[0].append('scarf')

# Move the coin and the harmonica and the boot from Box 3 to Box 5.
items_to_move = ['coin', 'harmonica', 'boot']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Replace the coin with the pan in Box 5.
boxes[5].remove('coin')
boxes[5].append('pan')

# Swap the boot in Box 5 with the card in Box 1.
boxes[5].remove('boot')
boxes[1].remove('card')
boxes[5].append('card')
boxes[1].append('boot')

# Move the scarf from Box 0 to Box 3.
boxes[0].remove('scarf')
boxes[3].append('scarf')

# Remove the harmonica from Box 5.
boxes[5].remove('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")