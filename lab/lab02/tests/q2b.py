test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> res_q2b.shape == (5, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(res_q2b == res_q2b.sort_values('cand_name', ascending=False))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(res_q2b['cmte_nm'].unique()) == ['CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT', 'CONSTITUTIONAL COMMITTEE', 'JOE ZUCCOLO FOR CONGRESS', "
                                               "'ZUKOWSKI FOR CONGRESS', 'ZUMWALT FOR CONGRESS']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
