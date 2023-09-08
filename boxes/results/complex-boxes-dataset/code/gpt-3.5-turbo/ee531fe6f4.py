# Initial state of boxes
boxes = {
    0: ['ocean', 'piano', 'key'],
    1: ['battery', 'coral', 'phone'],
    2: ['jacket', 'telescope', 'train'],
    3: ['clock', 'forest'],
    4: ['glove', 'flute', 'shorts', 'blender'],
    5: [],
    6: ['paint', 'comet', 'sock', 'coat'],
    7: ['scissors', 'octopus', 'basket'],
    8: ['harmonica', 'star', 'dolphin', 'perfume', 'sculpture'],
    9: ['dog', 'magnet', 'plate', 'wire', 'lipstick'],
    10: ['makeup', 'river'],
    11: ['tie', 'plane', 'shark', 'razor'],
    12: ['freezer', 'guitar', 'cat', 'sun'],
    13: ['mirror', 'microwave', 'card', 'toy', 'soap'],
    14: ['camera', 'violin', 'cow', 'ring', 'fork']
}

# Swap the key in Box 0 with the paint in Box 6.
boxes[0].remove('key')
boxes[6].remove('paint')
boxes[0].append('paint')
boxes[6].append('key')

# Move the scissors and the octopus and the basket from Box 7 to Box 10.
items_to_move = ['scissors', 'octopus', 'basket']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[10].append(item)

# Replace the freezer with the microwave in Box 12.
boxes[12].remove('freezer')
boxes[12].append('microwave')

# Put the makeup and the speaker into Box 2.
boxes[2].append('makeup')
boxes[2].append('speaker')

# Remove the cow from Box 14.
boxes[14].remove('cow')

# Remove the sock from Box 6.
boxes[6].remove('sock')

# Put the makeup into Box 14.
boxes[14].append('makeup')

# Move the ring and the makeup from Box 14 to Box 0.
boxes[14].remove('ring')
boxes[14].remove('makeup')
boxes[0].append('ring')
boxes[0].append('makeup')

# Swap the perfume in Box 8 with the clock in Box 3.
boxes[8].remove('perfume')
boxes[3].remove('clock')
boxes[8].append('clock')
boxes[3].append('perfume')

# Empty Box 14.
boxes[14] = []

# Replace the key and the comet with the lamp and the needle in Box 6.
boxes[0].remove('key')
boxes[6].remove('comet')
boxes[6].append('lamp')
boxes[6].append('needle')

# Replace the card with the island in Box 13.
boxes[13].remove('card')
boxes[13].append('island')

# Swap the dolphin in Box 8 with the speaker in Box 2.
boxes[8].remove('dolphin')
boxes[2].remove('speaker')
boxes[8].append('speaker')
boxes[2].append('dolphin')

# Put the starfish into Box 3.
boxes[3].append('starfish')

# Replace the wire and the plate with the cat and the keyboard in Box 9.
boxes[9].remove('wire')
boxes[9].remove('plate')
boxes[9].append('cat')
boxes[9].append('keyboard')

# Swap the ring in Box 0 with the plane in Box 11.
boxes[0].remove('ring')
boxes[11].remove('plane')
boxes[0].append('plane')
boxes[11].append('ring')

# Put the grinder and the dice into Box 4.
boxes[4].append('grinder')
boxes[4].append('dice')

# Replace the tie with the phone in Box 11.
boxes[11].remove('tie')
boxes[11].append('phone')

# Put the jacket and the soap into Box 11.
boxes[11].append('jacket')
boxes[11].append('soap')

# Remove the battery and the coral and the phone from Box 1.
items_to_remove = ['battery', 'coral', 'phone']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the jacket with the book in Box 2.
boxes[2].remove('jacket')
boxes[2].append('book')

# Move the grinder and the blender and the flute from Box 4 to Box 8.
items_to_move = ['grinder', 'blender', 'flute']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[8].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")