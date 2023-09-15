box_0 = ['coin', 'battery']
box_1 = ['sock', 'wire', 'comb']
box_2 = ['zipper', 'key']
box_3 = []
box_4 = ['elephant']
box_5 = ['controller', 'bus', 'cow', 'plate', 'jacket']
box_6 = ['clock', 'jungle', 'laptop', 'pen']
box_7 = ['paint', 'shelf']
box_8 = ['vase', 'plane']

# Remove the battery and the coin from Box 0
box_0.remove('battery')
box_0.remove('coin')

# Replace the elephant with the skirt in Box 4
box_4.remove('elephant')
box_4.append('skirt')

# Move the wire and the sock from Box 1 to Box 8
box_1.remove('wire')
box_1.remove('sock')
box_8.extend(['wire', 'sock'])

# Put the vase and the wig into Box 4
box_4.extend(['vase', 'wig'])

# Swap the shelf in Box 7 with the zipper in Box 2
box_7.remove('shelf')
box_2.remove('zipper')
box_7.append('zipper')
box_2.append('shelf')

# Move the skirt and the wig and the vase from Box 4 to Box 0
box_4.remove('skirt')
box_4.remove('wig')
box_4.remove('vase')
box_0.extend(['skirt', 'wig', 'vase'])

# Put the necklace into Box 2
box_2.append('necklace')

# Replace the key with the skirt in Box 2
box_2.remove('key')
box_2.append('skirt')

# Put the pan and the doll and the button into Box 5
box_5.extend(['pan', 'doll', 'button'])

# Put the umbrella into Box 4
box_4.append('umbrella')

# Swap the comb in Box 1 with the paint in Box 7
box_1.remove('comb')
box_7.remove('paint')
box_1.append('paint')
box_7.append('comb')

# Move the necklace and the shelf and the skirt from Box 2 to Box 3
box_2.remove('necklace')
box_2.remove('shelf')
box_2.remove('skirt')
box_3.extend(['necklace', 'shelf', 'skirt'])

# Replace the skirt and the necklace and the shelf with the bowl and the coral and the spoon in Box 3
box_3.remove('skirt')
box_3.remove('necklace')
box_3.remove('shelf')
box_3.extend(['bowl', 'coral', 'spoon'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)