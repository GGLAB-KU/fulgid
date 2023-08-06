def what_would_be_too_full():
    items = {
        'bathroom': 'room_to_build',
        'floor': 'space_to_fill'
    }

    for item, description in items.items():
        if description == 'space_to_fill':
            return item

print(what_would_be_too_full())  # This should print 'floor'