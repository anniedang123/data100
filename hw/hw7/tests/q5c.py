test = {   'name': 'q5c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> x1 = np.array([80, 100, 120]).reshape(-1, 1);\n'
                                               '>>> x2 = np.ones(len(x1)).reshape(-1, 1);\n'
                                               '>>> x = np.hstack((x1, x2));\n'
                                               '>>> prob80, prob100, prob120 = predicted_probability_of_winning_given_features(x, np.array([theta1, theta2]));\n'
                                               '>>> prob80 < 0.05 and np.allclose(prob100, 0.5) and prob120 > 0.95\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
