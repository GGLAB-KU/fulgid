box_0 = ['camera', 'candle', 'zipper', 'basket']
box_1 = ['helmet', 'needle', 'truck']
box_2 = ['glove', 'bus']
box_3 = ['blanket']
box_4 = ['razor', 'horse', 'grass']
box_5 = ['fork', 'spoon', 'coat', 'mask']
box_6 = ['bear', 'shoes']
box_7 = ['makeup']
box_8 = []

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)
    print("Box 8:", box_8)

# Initial state
print_boxes()

# Put the toy and the submarine into Box 5
box_5.extend(['toy', 'submarine'])

# Remove the helmet from Box 1
box_1.remove('helmet')

# Put the toy and the desert into Box 8
box_8.extend(['toy', 'desert'])

# Swap the submarine in Box 5 with the zipper in Box 0
box_0.remove('zipper')
box_5.remove('submarine')
box_0.append('submarine')
box_5.append('zipper')

# Put the shoes and the shark into Box 4
box_4.extend(['shoes', 'shark'])

# Put the shelf and the soap and the seaweed into Box 4
box_4.extend(['shelf', 'soap', 'seaweed'])

# Remove the grass and the seaweed from Box 4
box_4.remove('grass')
box_4.remove('seaweed')

# Put the leaf and the shark and the chair into Box 2
box_2.extend(['leaf', 'shark', 'chair'])

# Remove the shoes and the shark and the soap from Box 4
box_4.remove('shoes')
box_4.remove('shark')
box_4.remove('soap')

# Move the leaf from Box 2 to Box 0
box_2.remove('leaf')
box_0.append('leaf')

# Replace the shelf with the lamp in Box 4
box_4.remove('shelf')
box_4.append('lamp')

# Remove the shoes from Box 6
box_6.remove('shoes')

# Move the fork and the coat and the zipper from Box 5 to Box 3
box_5.remove('fork')
box_5.remove('coat')
box_5.remove('zipper')
box_3.extend(['fork', 'coat', 'zipper'])

# Final state
print_boxes()