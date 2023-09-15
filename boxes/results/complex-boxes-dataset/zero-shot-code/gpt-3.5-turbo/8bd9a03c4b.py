box = {
    0: [],
    1: ['butterfly', 'lipstick', 'desert', 'fork'],
    2: ['bicycle', 'watch', 'apple'],
    3: ['comb', 'bell', 'lightning', 'moon'],
    4: ['horn'],
    5: ['coral', 'needle', 'shelf', 'rain', 'coat'],
    6: ['dolphin', 'flute', 'game', 'boat', 'bus'],
    7: [],
    8: ['branch', 'snow', 'basket', 'frame'],
    9: ['fish'],
    10: ['helmet', 'battery']
}

# Remove the skirt from Box 1
box[1].remove('skirt')

# Swap the apple in Box 2 with the moon in Box 3
box[2].remove('apple')
box[3].remove('moon')
box[2].append('moon')
box[3].append('apple')

# Remove the battery from Box 10
box[10].remove('battery')

# Swap the needle in Box 5 with the fork in Box 1
box[5].remove('needle')
box[1].remove('fork')
box[5].append('fork')
box[1].append('needle')

# Put the octopus and the drum into Box 0
box[0].extend(['octopus', 'drum'])

# Replace the watch and the bicycle with the zipper and the note in Box 2
box[2].remove('watch')
box[2].remove('bicycle')
box[2].extend(['zipper', 'note'])

# Put the tree and the coin and the phone into Box 5
box[5].extend(['tree', 'coin', 'phone'])

# Move the frame and the branch from Box 8 to Box 2
box[8].remove('frame')
box[8].remove('branch')
box[2].extend(['frame', 'branch'])

# Empty Box 0
box[0] = []

# Swap the needle in Box 1 with the fish in Box 9
box[1].remove('needle')
box[9].remove('fish')
box[1].append('fish')
box[9].append('needle')

# Move the note and the moon and the frame from Box 2 to Box 5
box[2].remove('note')
box[2].remove('moon')
box[2].remove('frame')
box[5].extend(['note', 'moon', 'frame'])

# Replace the fish with the gloves in Box 1
box[1].remove('fish')
box[1].append('gloves')

# Move the lipstick and the desert and the gloves from Box 1 to Box 3
box[1].remove('lipstick')
box[1].remove('desert')
box[1].remove('gloves')
box[3].extend(['lipstick', 'desert', 'gloves'])

# Swap the needle in Box 9 with the zipper in Box 2
box[9].remove('needle')
box[2].remove('zipper')
box[9].append('zipper')
box[2].append('needle')

# Remove the needle from Box 2
box[2].remove('needle')

# Remove the horn from Box 4
box[4].remove('horn')

# Swap the helmet in Box 10 with the coat in Box 5
box[10].remove('helmet')
box[5].remove('coat')
box[10].append('coat')
box[5].append('helmet')

# Print the contents of each box
for i in range(11):
    print(f"Box {i}: {box[i]}")