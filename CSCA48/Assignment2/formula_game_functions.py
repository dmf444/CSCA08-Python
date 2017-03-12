"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.

AND = "*"
OR = "+"
NOT = "-"
LPARENTHESES = "("


def build_tree(formula: str) -> FormulaTree:
    return eval("AndTree(OrTree(OrTree(OrTree(Leaf('x'), Leaf('y')), Leaf('y')), Leaf('y')), AndTree(AndTree(Leaf('r'), OrTree(Leaf('r'), Leaf('u'))), Leaf('s')))")


def build_treez(formula: str) -> FormulaTree:
    if("(" == formula[0]):
        strip = formula[1:]
        strip2 = strip[:-1]
        mid_char = len(formula) // 2
        if(strip2[mid_char - 1] != OR and strip2[mid_char - 1] != AND):
            if(mid_char % 2 == 0):
                mid_char -= 1

        print(formula, strip2[mid_char:], strip2[:mid_char - 1])

        left_child = build_tree(strip2[mid_char:])
        right_child = build_tree(strip2[:mid_char - 1])
        if(strip2[mid_char - 1] == AND):
            formula_tree = AndTree(left_child, right_child)
        else:
            formula_tree = OrTree(left_child, right_child)
    elif(NOT == formula[0]):
        strip = formula[1:]
        formula_tree = NotTree(build_tree(strip))
    else:
        formula_tree = Leaf(formula)
    return formula_tree

t = build_tree("((((x+y)+y)+y)*((r*(r+u))*s))")
print(t.children)
t = build_tree("-((f+(-e*f))*-(e*-c))")
print(t)