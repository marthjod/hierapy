#!/usr/bin/python

from parser import HieraOutputParser
from unittest import TestCase
from nose.tools import assert_equal, assert_is_none


class TestHieraOutputParser(TestCase):

    def setUp(self):
        self.debug = False

    def tearDown(self):
        pass

    def test_nil(self):
        assert_equal(HieraOutputParser(text="nil", debug=self.debug).get_json(), "null")
        assert_is_none(HieraOutputParser(text="nil").get_python())

    def test_arrow(self):
        assert_equal(HieraOutputParser(text="=>", debug=self.debug).get_json(), ":")
        assert_equal(HieraOutputParser(text="=>").get_python(), ":")

    def test_string(self):
        assert_equal(HieraOutputParser(text="string", debug=self.debug).get_json(), "string")
        assert_equal(HieraOutputParser(text="string").get_python(), "string")

    def test_phrase(self):
        assert_equal(HieraOutputParser(text="some string", debug=self.debug).get_json(), "some string")
        assert_equal(HieraOutputParser(text="some string").get_python(), "some string")

    def test_empty_array(self):
        assert_equal(HieraOutputParser(text="[]", debug=self.debug).get_json(), "[]")
        assert_equal(HieraOutputParser(text="[]").get_python(), [])

    def test_empty_hash(self):
        assert_equal(HieraOutputParser(text="{}", debug=self.debug).get_json(), "{}")
        assert_equal(HieraOutputParser(text="{}").get_python(), {})

    def test_simple_hash(self):
        assert_equal(HieraOutputParser(text='{"foo"=>"bar"}', debug=self.debug).get_json(), '{"foo":"bar"}')
        assert_equal(HieraOutputParser(text='{"foo"=>"bar"}').get_python(), {"foo":"bar"})

    def test_simple_hash_whitespace(self):
        assert_equal(HieraOutputParser(text='{"foo" => "bar"}', debug=self.debug).get_json(), '{"foo" : "bar"}')
        assert_equal(HieraOutputParser(text='{"foo" => "bar"}').get_python(), {"foo":"bar"})

    def test_hash_value_list_ints(self):
        assert_equal(HieraOutputParser(text='{"foo"=>[1,2]}', debug=self.debug).get_json(), '{"foo":[1,2]}')
        assert_equal(HieraOutputParser(text='{"foo"=>[1,2]}').get_python(), {"foo": [1, 2]})

    def test_hash_value_list_strings(self):
        assert_equal(HieraOutputParser(text='{"foo"=>["a","b"]}', debug=self.debug).get_json(), '{"foo":["a","b"]}')
        assert_equal(HieraOutputParser(text='{"foo"=>["a","b"]}').get_python(), {"foo": ["a", "b"]})

    def test_hash_value_nil(self):
        assert_equal(HieraOutputParser(text='{"foo"=>nil}', debug=self.debug).get_json(), '{"foo":null}')
        assert_equal(HieraOutputParser(text='{"foo"=>nil}').get_python(), {"foo": None})

    def test_hash_value_list_misc(self):
        assert_equal(HieraOutputParser(text='{"foo"=>[{}, 3]}', debug=self.debug).get_json(), '{"foo":[{}, 3]}')
        assert_equal(HieraOutputParser(text='{"foo"=>[{}, 3]}').get_python(), {"foo": [{}, 3]})

    def test_hash_value_list_nil(self):
        assert_equal(HieraOutputParser(text='{"foo"=>[nil]}', debug=self.debug).get_json(), '{"foo":[null]}')
        assert_equal(HieraOutputParser(text='{"foo"=>[nil]}').get_python(), {"foo": [None]})
