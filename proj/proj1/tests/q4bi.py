test = {   'name': 'q4bi',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> 'bid' in ins.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> ins['bid'].dtype == int\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> len(ins[ins['score'] > 0]['bid'].unique()) == 5724\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
