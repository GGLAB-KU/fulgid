# Initial state of boxes
boxes = {
    0: ['pillow', 'phone', 'shark'],
    1: [],
    2: ['grinder'],
    3: ['comet', 'coral', 'beach'],
    4: ['toothpaste', 'belt', 'book'],
    5: ['coat', 'umbrella', 'lion'],
    6: ['candle', 'dress', 'bag', 'razor', 'headphone'],
    7: [],
    8: ['comb', 'lipstick', 'lightning'],
    9: ['cat', 'seaweed', 'lamp', 'chair'],
    10: ['moon', 'wire', 'scissors', 'flute'],
    11: ['keyboard'],
    12: [],
    13: ['rain', 'cup', 'card'],
    14: []
}

# Put the scarf and the game into Box 0.
boxes[0].append('scarf')
boxes[0].append('game')

# Put the tiger into Box 1.
boxes[1].append('tiger')

# Put the dress and the rock and the perfume into Box 10.
boxes[10].append('dress')
boxes[10].append('rock')
boxes[10].append('perfume')

# Put the charger and the plane and the rocket into Box 10.
boxes[10].append('charger')
boxes[10].append('plane')
boxes[10].append('rocket')

# Move the cup and the rain from Box 13 to Box 6.
boxes[13].remove('cup')
boxes[13].remove('rain')
boxes[6].append('cup')
boxes[6].append('rain')

# Put the lipstick and the bowl and the desert into Box 11.
boxes[11].append('lipstick')
boxes[11].append('bowl')
boxes[11].append('desert')

# Put the grinder into Box 9.
boxes[9].append('grinder')

# Remove the grinder and the seaweed and the cat from Box 9.
boxes[9].remove('grinder')
boxes[9].remove('seaweed')
boxes[9].remove('cat')

# Remove the tiger from Box 1.
boxes[1].remove('tiger')

# Move the card from Box 13 to Box 1.
boxes[13].remove('card')
boxes[1].append('card')

# Replace the coat and the lion and the umbrella with the note and the submarine and the sock in Box 5.
boxes[5].remove('coat')
boxes[5].remove('lion')
boxes[5].remove('umbrella')
boxes[5].append('note')
boxes[5].append('submarine')
boxes[5].append('sock')

# Swap the bag in Box 6 with the grinder in Box 2.
boxes[6].remove('bag')
boxes[2].remove('grinder')
boxes[6].append('grinder')
boxes[2].append('bag')

# Move the card from Box 1 to Box 6.
boxes[1].remove('card')
boxes[6].append('card')

# Move the belt and the toothpaste and the book from Box 4 to Box 12.
boxes[4].remove('belt')
boxes[4].remove('toothpaste')
boxes[4].remove('book')
boxes[12].append('belt')
boxes[12].append('toothpaste')
boxes[12].append('book')

# Remove the sock from Box 5.
boxes[5].remove('sock')

# Move the lipstick from Box 8 to Box 9.
boxes[8].remove('lipstick')
boxes[9].append('lipstick')

# Replace the rock and the wire and the flute with the storm and the bag and the cat in Box 10.
boxes[10].remove('rock')
boxes[10].remove('wire')
boxes[10].remove('flute')
boxes[10].append('storm')
boxes[10].append('bag')
boxes[10].append('cat')

# Replace the pillow and the scarf and the shark with the tiger and the necklace and the cow in Box 0.
boxes[0].remove('pillow')
boxes[0].remove('scarf')
boxes[0].remove('shark')
boxes[0].append('tiger')
boxes[0].append('necklace')
boxes[0].append('cow')

# Replace the desert and the bowl and the lipstick with the dress and the oven and the elephant in Box 11.
boxes[11].remove('desert')
boxes[11].remove('bowl')
boxes[11].remove('lipstick')
boxes[11].append('dress')
boxes[11].append('oven')
boxes[11].append('elephant')

# Remove the chair and the lipstick from Box 9.
boxes[9].remove('chair')
boxes[9].remove('lipstick')

# Move the dress and the perfume and the scissors from Box 10 to Box 12.
boxes[10].remove('dress')
boxes[10].remove('perfume')
boxes[10].remove('scissors')
boxes[12].append('dress')
boxes[12].append('perfume')
boxes[12].append('scissors')

# Put the ring into Box 14.
boxes[14].append('ring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")