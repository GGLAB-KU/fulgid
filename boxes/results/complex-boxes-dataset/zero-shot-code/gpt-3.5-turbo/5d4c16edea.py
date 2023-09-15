box = {
    0: ['guitar'],
    1: ['earring'],
    2: ['dog', 'ship'],
    3: ['candle'],
    4: ['harmonica', 'star', 'basket'],
    5: ['blender', 'pants', 'cow', 'planet', 'wallet'],
    6: ['card', 'plate', 'laptop', 'wire'],
    7: ['makeup'],
    8: [],
    9: ['desert', 'needle'],
    10: [],
    11: ['car', 'grinder', 'key'],
    12: ['lamp', 'submarine', 'bag', 'microscope']
}

# Replace the earring with the ship in Box 1
box[1].remove('earring')
box[1].append('ship')

# Replace the ship with the storm in Box 1
box[1].remove('ship')
box[1].append('storm')

# Remove the basket and the harmonica from Box 4
box[4].remove('basket')
box[4].remove('harmonica')

# Move the candle from Box 3 to Box 4
box[3].remove('candle')
box[4].append('candle')

# Put the mirror and the button and the freezer into Box 0
box[0].extend(['mirror', 'button', 'freezer'])

# Put the shirt and the gloves into Box 5
box[5].extend(['shirt', 'gloves'])

# Replace the microscope and the bag and the lamp with the skirt and the dress and the zipper in Box 12
box[12].remove('microscope')
box[12].remove('bag')
box[12].remove('lamp')
box[12].extend(['skirt', 'dress', 'zipper'])

# Put the lightning and the starfish and the cloud into Box 8
box[8].extend(['lightning', 'starfish', 'cloud'])

# Swap the storm in Box 1 with the ship in Box 2
box[1].remove('storm')
box[2].remove('ship')
box[1].append('ship')
box[2].append('storm')

# Empty Box 9
box[9] = []

# Move the submarine and the skirt and the dress from Box 12 to Box 9
box[12].remove('submarine')
box[12].remove('skirt')
box[12].remove('dress')
box[9].extend(['submarine', 'skirt', 'dress'])

# Put the lipstick and the grinder and the jacket into Box 11
box[11].extend(['lipstick', 'grinder', 'jacket'])

# Put the harmonica and the shelf into Box 6
box[6].extend(['harmonica', 'shelf'])

# Remove the candle and the star from Box 4
box[4].remove('candle')
box[4].remove('star')

# Move the dress from Box 9 to Box 3
box[9].remove('dress')
box[3].append('dress')

# Swap the dog in Box 2 with the ship in Box 1
box[2].remove('dog')
box[1].remove('ship')
box[2].append('ship')
box[1].append('dog')

# Replace the makeup with the grinder in Box 7
box[7].remove('makeup')
box[7].append('grinder')

# Move the zipper from Box 12 to Box 6
box[12].remove('zipper')
box[6].append('zipper')

# Swap the submarine in Box 9 with the dog in Box 1
box[9].remove('submarine')
box[1].remove('dog')
box[9].append('dog')
box[1].append('submarine')

# Put the violin into Box 9
box[9].append('violin')

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")