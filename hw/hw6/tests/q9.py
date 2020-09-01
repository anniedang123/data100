test = {   'name': 'q9',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> def rmse(predicted, actual):\n'
                                               '...     return np.sqrt(np.mean((actual - predicted)**2));\n'
                                               ">>> training_data = pd.read_csv('ames_train_cleaned.csv');\n"
                                               '>>> X_train, y_train = process_data_fm(training_data);\n'
                                               '>>> _ = final_model.fit(X_train, y_train);\n'
                                               '>>> y_predicted_train = final_model.predict(X_train);\n'
                                               '>>> training_rmse = rmse(y_predicted_train, y_train);\n'
                                               '>>> training_rmse <= 38000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def rmse(predicted, actual):\n'
                                               '...     return np.sqrt(np.mean((actual - predicted)**2));\n'
                                               ">>> training_data = pd.read_csv('ames_train_cleaned.csv');\n"
                                               ">>> test_data = pd.read_csv('ames_test_cleaned.csv');\n"
                                               '>>> X_train, y_train = process_data_fm(training_data);\n'
                                               '>>> X_test, y_test = process_data_fm(test_data);\n'
                                               '>>> X_test_public, y_test_public = X_test[::2], y_test[::2];\n'
                                               '>>> _ = final_model.fit(X_train, y_train);\n'
                                               '>>> y_predicted_train = final_model.predict(X_train);\n'
                                               '>>> y_predicted_test_public = final_model.predict(X_test_public);\n'
                                               '>>> training_rmse = rmse(y_predicted_train, y_train);\n'
                                               '>>> public_test_rmse = rmse(y_predicted_test_public, y_test_public);\n'
                                               '>>> public_test_rmse <= 39000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
