box0 = ['skirt', 'shorts', 'towel', 'needle']
box1 = ['shark', 'comb', 'bus']
box2 = []
box3 = ['candle']
box4 = []

# Swap needle in Box 0 with candle in Box 3
box0.remove('needle')
box3.remove('candle')
box0.append('candle')
box3.append('needle')

# Replace shorts with cow in Box 0
box0.remove('shorts')
box0.append('cow')

# Move cow, skirt, and towel from Box 0 to Box 4
box4.extend(box0)
box0.clear()

# Replace skirt and cow with keyboard and plane in Box 4
box4.remove('skirt')
box4.remove('cow')
box4.append('keyboard')
box4.append('plane')

# Put toy and soap into Box 3
box3.append('toy')
box3.append('soap')

# Move toy and needle from Box 3 to Box 2
box3.remove('toy')
box3.remove('needle')
box2.append('toy')
box2.append('needle')

# Replace plane and keyboard with whistle and button in Box 4
box4.remove('plane')
box4.remove('keyboard')
box4.append('whistle')
box4.append('button')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)