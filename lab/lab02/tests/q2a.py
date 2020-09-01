test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> res_q2a.shape == (5, 3)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(res_q2a == res_q2a.sort_values('count', ascending=False))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sorted(res_q2a['total_amount'].unique()) == [316019, 492567, 499659, 6989835, 25099091]\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
