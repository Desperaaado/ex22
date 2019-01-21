from nose.tools import *
from ex22.ex22 import *

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    text = 'abracadabrabracabrac'
    stuff = SuffixArrays(text)
    result1 = stuff.find_shortest('abra')
    assert_equal(result1, 'abrac')
    result2 = stuff.find_longest('abra')
    assert_equal(result2, 'abracadabrabracabrac')
    result3 = stuff.find_all('abra')
    print(result3)

def test_BSTree():
    text = 'abracadabrabracabrac'
    stuff = BSTreeSuffixArrays(text)
    result1 = stuff.find_shortest('ac')
    assert_equal(result1, 'ac')
    # text = 'abracadabrabracabrac'
    # stuff = BSTreeSuffixArrays(text)
    # result1 = stuff.find_shortest('abra')
    # assert_equal(result1, 'abrac')
#     result2 = stuff.find_longest('abra')
#     assert_equal(result2, 'abracadabrabracabrac')
#     result3 = stuff.find_all('abra')
#     print(result3)