# -*- coding: utf-8 -*-
'''
    File name: tests.py
    Author: Kasia Pekala
    Date last modified: 4/18/2018
    Python Version: 3.5
'''
import unittest

import rainbow_methods

class TestColoring(unittest.TestCase):
    def number_of_subgraphs(self):
        self.assertEqual(len(rainbow_methods.split_nodes(50,41)), 5)
        self.assertEqual(len(rainbow_methods.split_nodes(9,4)), 1)
    def size_of_subgraphs(self):
        self.assertEqual(rainbow_methods.split_nodes(50,40)[2].number_of_nodes(), 11)
        self.assertEqual(rainbow_methods.split_nodes(50,40)[0].number_of_nodes(), 17)
        self.assertEqual(rainbow_methods.split_nodes(9,4)[0].number_of_nodes(), 9)
    def nr_of_edges_in_subgraphs(self):
        self.assertEqual(rainbow_methods.split_nodes(50,40)[2].number_of_edges(), 55)
        self.assertEqual(rainbow_methods.split_nodes(50,40)[0].number_of_edges(), 136)
        self.assertEqual(rainbow_methods.split_nodes(9,4)[0].number_of_edges(), 36)
    def nr_of_colors(self):
        n = 10
        r = 7
        testGraph = rainbow_methods.find_coloring(n,r)
        self.assertEqual(rainbow_methods.how_many_colors_in_graph(testGraph), rainbow_methods.TaoJiang(n,r)[0])
    def nr_of_colors2(self):        
        n = 50
        r = 40
        testGraph = rainbow_methods.find_coloring(n,r)
        self.assertEqual(rainbow_methods.how_many_colors_in_graph(testGraph), rainbow_methods.TaoJiang(n,r)[0])
    def no_TMC_rainbow(self):
        n = 50
        r = 40
        testGraph = rainbow_methods.find_coloring(n,r)
        self.assertEqual(max(rainbow_methods.stars_colorings(testGraph).values()), r)
    def no_TMC_rainbow2(self):
        n = 49
        r = 40
        testGraph = rainbow_methods.find_coloring(n,r)
        self.assertEqual(max(rainbow_methods.stars_colorings(testGraph).values()), r)
    def nr_of_colors3(self):
        n = 11
        r = 4
        testGraph = rainbow_methods.find_coloring(n,r)
        self.assertEqual(rainbow_methods.how_many_colors_in_graph(testGraph), rainbow_methods.TaoJiang(n,r)[0])

def test_multiple_val():
   for n in range(20,30):
       for r in range(2,n-1):
         GG = rainbow_methods.find_coloring(n,r)
         m = math.floor(n/(n-r+1))   
         mnod = max(rainbow_methods.stars_colorings(GG).values())
         tj = rainbow_methods.TaoJiang(n,r)[0]
         hmc = rainbow_methods.how_many_colors_in_graph(GG)
         print("\nn =",n,"r =",r,"Największa gwiazda TMC = ",mnod,"Dolne ograniczenie =",tj,"Ile kolorów użyto =",hmc," m=",m)
         print(sorted(count_colors_freq(GG).values(),reverse=True))
         if (tj != hmc) or (r !=mnod):
             print("błąd!")
        
   return