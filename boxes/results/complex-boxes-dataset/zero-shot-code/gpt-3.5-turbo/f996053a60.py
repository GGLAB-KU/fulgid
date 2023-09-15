box_0 = ['watch', 'blanket', 'lion']
box_1 = ['lock', 'apple', 'battery', 'jungle']
box_2 = ['dice', 'desert', 'bus', 'ocean', 'speaker']
box_3 = ['telescope']
box_4 = ['dress', 'plate']
box_5 = ['toy', 'drum', 'chair', 'boat', 'sock']
box_6 = ['pen', 'river', 'star', 'card']
box_7 = []
box_8 = ['phone', 'puzzle', 'cloud']
box_9 = ['ship', 'rocket', 'belt']
box_10 = ['button']
box_11 = ['storm', 'toothpaste', 'toaster', 'branch', 'seaweed']
box_12 = ['submarine', 'wig', 'shoe']

box_3.remove('telescope')
box_11.extend(['shoe', 'submarine'])
box_6.remove('star')
box_8.remove('cloud')
box_8.append('star')
box_11.append('grass')
box_12[box_12.index('wig')] = 'battery'
box_6.remove('card')
box_1[box_1.index('lock')] = 'river'
box_8.extend(['clock', 'sculpture', 'puzzle'])
box_0.append(box_12.pop(box_12.index('battery')))
box_7.extend(['rocket', 'scissors', 'ship'])
box_8.remove('sculpture')
box_9.extend(['plate', 'dress'])
box_3.append(box_10.pop(box_10.index('button')))
box_7.extend(['rocket', 'ship'])
box_9.extend(['key', 'bus', 'planet'])
box_3.extend(['lock', 'pen'])
box_6.extend(['rocket', 'ship'])
box_0.append('towel')
box_9.remove('belt')
box_9.remove('planet')
box_9.remove('bus')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)