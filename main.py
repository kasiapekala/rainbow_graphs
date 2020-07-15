# -*- coding: utf-8 -*-
'''
    File name: main.py
    Author: Kasia Pekala
    Date last modified: 4/18/2018
    Python Version: 3.5
'''

import os
#os.chdir("")
import rainbow_methods
import rainbow_tests

# examples
rainbow_methods.present_results(7,4)
rainbow_methods.present_results(14,6) #przykład 4.3.2
#rainbow_methods.present_results(20,8)

# testy
rainbow_tests.TestColoring().number_of_subgraphs()
rainbow_tests.TestColoring().size_of_subgraphs()
rainbow_tests.TestColoring().nr_of_edges_in_subgraphs()
rainbow_tests.TestColoring().nr_of_colors()
rainbow_tests.TestColoring().nr_of_colors2()
rainbow_tests.TestColoring().nr_of_colors3()
rainbow_tests.TestColoring().no_TMC_rainbow()
rainbow_tests.TestColoring().no_TMC_rainbow2()
