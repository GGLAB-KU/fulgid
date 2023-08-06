def what_was_casual():
    items = {
        'woven necklace': 'necklace_type',
        'ball': 'event_type'
    }

    for item, description in items.items():
        if description == 'event_type':
            return item

print(what_was_casual())  # This should print 'ball'