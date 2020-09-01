test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(bootstrap(np.ones(10), np.mean, simple_resample))\n1000', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(bootstrap(np.ones(10), np.mean, simple_resample, replicates = 1000) == np.ones(1000))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # chances are less than 3.9 in 10^22 that this test fails when the function is correct;\n'
                                               '>>> sum(bootstrap(np.array([0,1]), np.median, simple_resample, replicates = 10000) == 0.5) in range(5000-500,5000+500)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
