test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(my_zip, zipfile.ZipFile)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> list_files_defined = "list_files" in globals();\n'
                                               '>>> if list_files_defined:\n'
                                               '...     list_names = list_files;\n'
                                               '>>> isinstance(list_names, list)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> list_files_defined = "list_files" in globals();\n'
                                               '>>> if list_files_defined:\n'
                                               '...     list_names = list_files;\n'
                                               '>>> all([isinstance(file, str) for file in list_names]) \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
