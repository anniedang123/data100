test = {   'name': 'q5a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> "name" in ins_named and "address" in ins_named\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(ins_named) == len(ins)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> ins_named[ins_named['score'] > 0].reset_index()['date'].equals(ins[ins['score'] > 0].reset_index()['date'])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
