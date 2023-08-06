def what_was_refused():
    treatments = {
        'diet': 'slow',
        'surgery': 'quick'
    }

    for treatment, speed in treatments.items():
        if speed == 'quick':
            return treatment

print(what_was_refused())  # This should print 'surgery'