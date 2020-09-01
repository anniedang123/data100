test = {   'name': 'q6c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> sum(training_data.loc[:, 'in_rich_neighborhood']) == 191\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(training_data.loc[:, 'in_rich_neighborhood'].isnull()) == 0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(add_in_rich_neighborhood(training_data, ['NAmes']).loc[:, 'in_rich_neighborhood']) == 299\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
