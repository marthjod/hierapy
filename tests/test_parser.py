from parser.parser import HieraOutputParser
from unittest import TestCase
from nose.tools import assert_equal
from nose_parameterized import parameterized


class TestHieraOutputParser(TestCase):

    def setUp(self):
        self.debug = False

    @parameterized.expand([
        ("nil", "null", None),
        ("=>", ":", ":"),
        ("string", "string", "string"),
        ("some string", "some string", "some string"),
        ("[]", "[]", []),
        ("{}", "{}", {}),
        ('{"foo"=>"bar"}', '{"foo":"bar"}', {"foo": "bar"}),
        ('{"foo" => "bar"}', '{"foo" : "bar"}', {"foo": "bar"}),
        ('{"foo"=>[1,2]}', '{"foo":[1,2]}', {"foo": [1, 2]}),
        ('{"foo"=>["a","b"]}', '{"foo":["a","b"]}', {"foo": ["a", "b"]}),
        ('{"foo"=>nil}', '{"foo":null}', {"foo": None}),
        ('{"foo"=>[{}, 3]}', '{"foo":[{}, 3]}', {"foo": [{}, 3]}),
        ('{"foo"=>[nil]}', '{"foo":[null]}', {"foo": [None]}),
        ('{"foo"=>["01", "02"], "bar"=>[]}',
         '{"foo":["01", "02"], "bar":[]}',
         {"foo": ["01", "02"], "bar": []}),
        ('{"foo"=>["01", "02"], "bar"=>["f-oo@gee.la"]}',
         '{"foo":["01", "02"], "bar":["f-oo@gee.la"]}',
         {"foo": ["01", "02"], "bar": ["f-oo@gee.la"]}),
        ('{"foo"=>[1, 2], "bar"=>["f-oo@gee.la"]}',
         '{"foo":[1, 2], "bar":["f-oo@gee.la"]}',
         {"foo": [1, 2], "bar": ["f-oo@gee.la"]}),
        ('{"foo"=>[nil,nil]}',
         '{"foo":[null,null]}',
         {"foo": [None, None]})
    ])
    def test_conversion(self, input, expected_json, expected_python):
        p = HieraOutputParser(text=input, debug=self.debug)
        assert_equal(p.get_json(), expected_json)
        assert_equal(p.get_python(), expected_python)
