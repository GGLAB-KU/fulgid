def what_was_too_bright():
    times = {
        'day': 'brightness_level',
        'night': 'brightness_level'
    }

    for time, brightness in times.items():
        if brightness == 'brightness_level':
            return time

print(what_was_too_bright())  # This should print 'day'