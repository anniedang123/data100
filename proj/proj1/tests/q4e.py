test = {   'name': 'q4e',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> if type(ins_missing_score_pivot) == pd.DataFrame:\n'
                                               '...     if False in ins_missing_score_pivot.columns: \n'
                                               '...         ins_missing_score_pivot.rename(columns={False:"False"}, errors="raise",inplace=True)\n'
                                               '...     if True in ins_missing_score_pivot.columns:\n'
                                               '...         ins_missing_score_pivot.rename(columns={True:"True"}, errors="raise",inplace=True);\n'
                                               '>>> type(ins_missing_score_pivot) == pd.DataFrame\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
