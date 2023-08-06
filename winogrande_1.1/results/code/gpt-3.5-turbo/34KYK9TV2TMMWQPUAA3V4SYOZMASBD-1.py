def what_was_susceptible_to_heat():
    substances = {
        'paint': 'susceptible',
        'varnish': 'not susceptible'
    }

    for substance, susceptibility in substances.items():
        if susceptibility == 'susceptible':
            return substance

print(what_was_susceptible_to_heat())  # This should print 'paint'