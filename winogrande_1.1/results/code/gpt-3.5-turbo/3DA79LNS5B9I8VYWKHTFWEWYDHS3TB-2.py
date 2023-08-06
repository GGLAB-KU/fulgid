def which_was_closer():
    items = {
        'pudding': 15,
        'frosting': 5
    }

    for item, distance in items.items():
        if distance == min(items.values()):
            return item

print(which_was_closer())  # This should print 'frosting'