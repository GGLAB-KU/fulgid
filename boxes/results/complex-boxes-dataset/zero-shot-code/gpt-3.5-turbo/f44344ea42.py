box_0 = ['toothpaste', 'frame', 'lightning', 'magnet']
box_1 = []
box_2 = ['scarf', 'pot']
box_3 = ['fish', 'cat', 'dog', 'belt', 'shelf']
box_4 = ['harmonica', 'seaweed']
box_5 = ['tie']
box_6 = ['island', 'scissors', 'branch']
box_7 = []
box_8 = ['comet']
box_9 = []
box_10 = ['ring', 'dress']
box_11 = ['mask', 'bear', 'tiger']
box_12 = ['apple', 'bracelet']

# Swap fish in Box 3 with lightning in Box 0
box_0.remove('lightning')
box_3.remove('fish')
box_0.append('fish')
box_3.append('lightning')

# Put gloves into Box 11
box_11.append('gloves')

# Put leaf and toy into Box 12
box_12.extend(['leaf', 'toy'])

# Replace tie with pants in Box 5
box_5.remove('tie')
box_5.append('pants')

# Swap scissors in Box 6 with scarf in Box 2
box_2.remove('scarf')
box_6.remove('scissors')
box_2.append('scissors')
box_6.append('scarf')

# Move ring and dress from Box 10 to Box 6
box_10.remove('ring')
box_10.remove('dress')
box_6.extend(['ring', 'dress'])

# Move dress from Box 6 to Box 9
box_6.remove('dress')
box_9.append('dress')

# Remove apple from Box 12
box_12.remove('apple')

# Replace toy and bracelet with dolphin and toothbrush in Box 12
box_12.remove('toy')
box_12.remove('bracelet')
box_12.extend(['dolphin', 'toothbrush'])

# Move scarf, branch, and island from Box 6 to Box 11
box_6.remove('scarf')
box_6.remove('branch')
box_6.remove('island')
box_11.extend(['scarf', 'branch', 'island'])

# Remove dress from Box 9
box_9.remove('dress')

# Replace pants with zipper in Box 5
box_5.remove('pants')
box_5.append('zipper')

# Replace ring with island in Box 6
box_6.remove('ring')
box_6.append('island')

# Remove seaweed and harmonica from Box 4
box_4.remove('seaweed')
box_4.remove('harmonica')

# Swap toothbrush in Box 12 with island in Box 6
box_6.remove('island')
box_12.remove('toothbrush')
box_6.append('toothbrush')
box_12.append('island')

# Remove leaf and island from Box 12
box_12.remove('leaf')
box_12.remove('island')

# Remove pot and scissors from Box 2
box_2.remove('pot')
box_2.remove('scissors')

# Swap zipper in Box 5 with frame in Box 0
box_0.remove('frame')
box_5.remove('zipper')
box_0.append('zipper')
box_5.append('frame')

# Remove toothbrush from Box 6
box_6.remove('toothbrush')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")