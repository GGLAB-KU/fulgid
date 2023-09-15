box_0 = ['pillow', 'phone', 'shark']
box_1 = []
box_2 = ['grinder']
box_3 = ['comet', 'coral', 'beach']
box_4 = ['toothpaste', 'belt', 'book']
box_5 = ['coat', 'umbrella', 'lion']
box_6 = ['candle', 'dress', 'bag', 'razor', 'headphone']
box_7 = []
box_8 = ['comb', 'lipstick', 'lightning']
box_9 = ['cat', 'seaweed', 'lamp', 'chair']
box_10 = ['moon', 'wire', 'scissors', 'flute']
box_11 = ['keyboard']
box_12 = []
box_13 = ['rain', 'cup', 'card']
box_14 = []

# Put the scarf and the game into Box 0
box_0.extend(['scarf', 'game'])

# Put the tiger into Box 1
box_1.append('tiger')

# Put the dress and the rock and the perfume into Box 10
box_10.extend(['dress', 'rock', 'perfume'])

# Put the charger and the plane and the rocket into Box 10
box_10.extend(['charger', 'plane', 'rocket'])

# Move the cup and the rain from Box 13 to Box 6
box_6.extend([box_13.pop(box_13.index('cup')), box_13.pop(box_13.index('rain'))])

# Put the lipstick and the bowl and the desert into Box 11
box_11.extend(['lipstick', 'bowl', 'desert'])

# Put the grinder into Box 9
box_9.append('grinder')

# Remove the grinder and the seaweed and the cat from Box 9
box_9.remove('grinder')
box_9.remove('seaweed')
box_9.remove('cat')

# Remove the tiger from Box 1
box_1.remove('tiger')

# Move the card from Box 13 to Box 1
box_1.append(box_13.pop(box_13.index('card')))

# Replace the coat and the lion and the umbrella with the note and the submarine and the sock in Box 5
box_5 = ['note', 'submarine', 'sock']

# Swap the bag in Box 6 with the grinder in Box 2
box_6.remove('bag')
box_2.remove('grinder')
box_6.append('grinder')
box_2.append('bag')

# Move the card from Box 1 to Box 6
box_6.append(box_1.pop(box_1.index('card')))

# Move the belt and the toothpaste and the book from Box 4 to Box 12
box_12.extend([box_4.pop(box_4.index('belt')), box_4.pop(box_4.index('toothpaste')), box_4.pop(box_4.index('book'))])

# Remove the sock from Box 5
box_5.remove('sock')

# Move the lipstick from Box 8 to Box 9
box_9.append(box_8.pop(box_8.index('lipstick')))

# Replace the rock and the wire and the flute with the storm and the bag and the cat in Box 10
box_10 = ['storm', 'bag', 'cat']

# Replace the pillow and the scarf and the shark with the tiger and the necklace and the cow in Box 0
box_0 = ['tiger', 'necklace', 'cow']

# Replace the desert and the bowl and the lipstick with the dress and the oven and the elephant in Box 11
box_11 = ['dress', 'oven', 'elephant']

# Remove the chair and the lipstick from Box 9
box_9.remove('chair')
box_9.remove('lipstick')

# Move the dress and the perfume and the scissors from Box 10 to Box 12
box_12.extend([box_10.pop(box_10.index('dress')), box_10.pop(box_10.index('perfume')), box_10.pop(box_10.index('scissors'))])

# Put the ring into Box 14
box_14.append('ring')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
    print(f"Box {i}: {box}")