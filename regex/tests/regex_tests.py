from nose.tools import *
from RegexQuery.regex_query import regex_query_tool

def regex_test():
    assert_equals(regex_query_tool('ala ma kota', '[^\s]+'), ['ala', 'ma', 'kota'])
