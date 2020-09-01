test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> train.shape == (1600, 82) # train should contain 80% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> val.shape == (400, 82) # val should contain 20% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.intersect1d(train['PID'], val['PID']).size == 0 # make sure train and val have no overlapping houses\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sum(train['SalePrice']) == 290405887 # If this doesn't match, you might have still answered the question, but please adjust your code so that your "
                                               'split matches ours by setting the random_state parameter to be 42.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> sum(val['SalePrice']) == 71145908 # If this doesn't match, you might have still answered the question, but please adjust your code so that your "
                                               'split matches ours by setting the random_state parameter to be 42.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
