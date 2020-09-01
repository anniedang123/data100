test = {   'name': 'q5a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.allclose(predicted_probability_of_winning_given_features(points_and_bias.iloc[0:3, :], np.array([0.1, -10])), np.array([0.6899744811276126, '
                                               '0.5, 0.21416501695744153]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.allclose(predicted_probability_of_winning_given_features(points_and_bias.iloc[0:3, :], np.array([0.01, 1])), np.array([0.8889440332885924, '
                                               '0.8807970779778823, 0.8664582774667876]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(predicted_probability_of_winning_given_features(points_and_bias.iloc[0:3, :], np.array([0.01, 1]))[0], 0.8889440332885924)\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
