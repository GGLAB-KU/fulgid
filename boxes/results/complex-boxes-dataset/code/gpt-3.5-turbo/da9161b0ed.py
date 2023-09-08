# Initial state of boxes
boxes = {
    0: ['seaweed'],
    1: ['puzzle'],
    2: ['charger', 'jacket'],
    3: ['telescope', 'grinder'],
    4: ['ship', 'dice', 'river'],
    5: ['usb', 'gloves', 'cow', 'key', 'tie'],
    6: ['watch', 'fork'],
    7: [],
    8: ['jungle', 'island', 'toaster', 'rock'],
    9: ['comet', 'towel', 'train'],
    10: ['coin', 'glasses', 'lock', 'elephant', 'sun'],
    11: [],
    12: ['boat', 'speaker', 'rocket', 'octopus', 'tiger'],
    13: []
}

# Remove the octopus from Box 12.
boxes[12].remove('octopus')

# Move the rocket from Box 12 to Box 13.
boxes[12].remove('rocket')
boxes[13].append('rocket')

# Swap the jacket in Box 2 with the grinder in Box 3.
boxes[2].remove('jacket')
boxes[3].remove('grinder')
boxes[2].append('grinder')
boxes[3].append('jacket')

# Move the seaweed from Box 0 to Box 13.
boxes[0].remove('seaweed')
boxes[13].append('seaweed')

# Swap the key in Box 5 with the grinder in Box 2.
boxes[5].remove('key')
boxes[2].remove('grinder')
boxes[5].append('grinder')
boxes[2].append('key')

# Remove the telescope and the jacket from Box 3.
boxes[3].remove('telescope')
boxes[3].remove('jacket')

# Swap the usb in Box 5 with the seaweed in Box 13.
boxes[5].remove('usb')
boxes[13].remove('seaweed')
boxes[5].append('seaweed')
boxes[13].append('usb')

# Remove the train and the towel and the comet from Box 9.
boxes[9].remove('train')
boxes[9].remove('towel')
boxes[9].remove('comet')

# Put the cow and the magnet and the desert into Box 3.
boxes[3].append('cow')
boxes[3].append('magnet')
boxes[3].append('desert')

# Remove the watch from Box 6.
boxes[6].remove('watch')

# Replace the fork with the tape in Box 6.
boxes[6].remove('fork')
boxes[6].append('tape')

# Put the sandals and the lightning and the dog into Box 5.
boxes[5].append('sandals')
boxes[5].append('lightning')
boxes[5].append('dog')

# Swap the usb in Box 13 with the desert in Box 3.
boxes[13].remove('usb')
boxes[3].remove('desert')
boxes[13].append('desert')
boxes[3].append('usb')

# Replace the ship with the polish in Box 4.
boxes[4].remove('ship')
boxes[4].append('polish')

# Remove the speaker from Box 12.
boxes[12].remove('speaker')

# Put the tiger into Box 12.
boxes[12].append('tiger')

# Move the cow and the magnet and the usb from Box 3 to Box 10.
items_to_move = ['cow', 'magnet', 'usb']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[10].append(item)

# Replace the lightning and the seaweed and the gloves with the dog and the magnet and the butterfly in Box 5.
boxes[5].remove('lightning')
boxes[5].remove('seaweed')
boxes[5].remove('gloves')
boxes[5].append('dog')
boxes[5].append('magnet')
boxes[5].append('butterfly')

# Remove the polish from Box 4.
boxes[4].remove('polish')

# Remove the dice and the boat from Box 12.
boxes[12].remove('dice')
boxes[12].remove('boat')

# Swap the jungle in Box 8 with the tiger in Box 12.
boxes[8].remove('jungle')
boxes[12].remove('tiger')
boxes[8].append('tiger')
boxes[12].append('jungle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")