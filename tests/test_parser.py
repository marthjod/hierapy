# encoding: utf-8

from __future__ import unicode_literals

import sys

from unittest import TestCase

from nose.tools import assert_equal
from parameterized import parameterized

from hipy.parser import HieraOutputParser


class TestHieraOutputParser(TestCase):
    @parameterized.expand([
        ("nil", "null", None),
        ("=>", ":", ":"),
        ("string", "string", "string"),
        ("some string", "some string", "some string"),
        ("[]", "[]", []),
        ("{}", "{}", {}),
        ("[", "[", "["),
        ("]", "]", "]"),
        ("{", "{", "{"),
        ("}", "}", "}"),
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
        ('{"foo"=>[1, 2], "bar"=>["f-o_o@gee.la"]}',
         '{"foo":[1, 2], "bar":["f-o_o@gee.la"]}',
         {"foo": [1, 2], "bar": ["f-o_o@gee.la"]}),
        ('{"foo"=>[nil,nil]}',
         '{"foo":[null,null]}',
         {"foo": [None, None]}),
        ('true', 'true', True),
        ('false', 'false', False),
        ('{"foo"=>false, "bar"=>true}', '{"foo":false, "bar":true}',
         {"foo": False, "bar": True}),
        ('["127.0.0.1"]', '["127.0.0.1"]', ["127.0.0.1"]),
        ('["127.0.0.1", "127.0.0.2"]', '["127.0.0.1", "127.0.0.2"]',
         ["127.0.0.1", "127.0.0.2"]),
        ('ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de',
         'ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de',
         'ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de'),
        ('!"$%&/()=~[]{}+*#?', '!"$%&/()=~[]{}+*#?', '!"$%&/()=~[]{}+*#?'),
        ('{"one"=>{"two"=>{"three"=>{"four"=>["five@bar.com"]}}}}',
         '{"one":{"two":{"three":{"four":["five@bar.com"]}}}}',
         {"one": {"two": {"three": {"four": ["five@bar.com"]}}}}),
        ("foo \n bar", "foo \n bar", "foo \n bar"),
        ("äöüß", "äöüß", "äöüß"),
        ("ÄÖÜ", "ÄÖÜ", "ÄÖÜ")
    ])
    def test_conversion(self, input, expected_json, expected_python):
        p = HieraOutputParser(text=input)
        assert_equal(p.get_json(), expected_json)
        assert_equal(p.get_python(), expected_python)

    @parameterized.expand([
        ("nil", "null", None),
        ("=>", ":", ":"),
        ("string", "string", "string"),
        ("some string", "some string", "some string"),
        ("[]", "[]", []),
        ("{}", "{}", {}),
        ("[", "[", "["),
        ("]", "]", "]"),
        ("{", "{", "{"),
        ("}", "}", "}"),
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
        ('{"foo"=>[1, 2], "bar"=>["f-o_o@gee.la"]}',
         '{"foo":[1, 2], "bar":["f-o_o@gee.la"]}',
         {"foo": [1, 2], "bar": ["f-o_o@gee.la"]}),
        ('{"foo"=>[nil,nil]}',
         '{"foo":[null,null]}',
         {"foo": [None, None]}),
        ('true', 'true', True),
        ('false', 'false', False),
        ('{"foo"=>false, "bar"=>true}', '{"foo":false, "bar":true}',
         {"foo": False, "bar": True}),
        ('["127.0.0.1"]', '["127.0.0.1"]', ["127.0.0.1"]),
        ('["127.0.0.1", "127.0.0.2"]', '["127.0.0.1", "127.0.0.2"]',
         ["127.0.0.1", "127.0.0.2"]),
        ('ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de',
         'ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de',
         'ou=TESTCA 2:PN\,o=TESTCA Foo Com\,c=de'),
        ('!"$%&/()=~[]{}+*#?', '!"$%&/()=~[]{}+*#?', '!"$%&/()=~[]{}+*#?'),
        ('{"one"=>{"two"=>{"three"=>{"four"=>["five@bar.com"]}}}}',
         '{"one":{"two":{"three":{"four":["five@bar.com"]}}}}',
         {"one": {"two": {"three": {"four": ["five@bar.com"]}}}}),
        ("foo \n bar", "foo \n bar", "foo \n bar"),
        ("äöüß", "äöüß", "äöüß"),
        ("ÄÖÜ", "ÄÖÜ", "ÄÖÜ")
    ])
    def test_conversion_debug(self, input, expected_json, expected_python):
        p = HieraOutputParser(text=input, debug=True)
        assert_equal(p.get_json(), expected_json)
        assert_equal(p.get_python(), expected_python)

    @parameterized.expand([
        ("foo", 'Expecting value: line 1 column 1 (char 0)', False),
        ("foo", '', True)
    ])
    def test_invalid_input_ge_py34(self, input, stdoutput, quiet):
        if sys.version_info.major == 3 and sys.version_info.minor >= 4:
            from contextlib import redirect_stdout
            from io import StringIO

            p = HieraOutputParser(text=input, quiet=quiet)

            f = StringIO()
            with redirect_stdout(f):
                p.get_python()
            output = f.getvalue().strip()

            assert_equal(stdoutput, output)

    @parameterized.expand([
        ("foo", 'No JSON object could be decoded', False),
        ("foo", '', True)
    ])
    def test_invalid_input_eq_py27(self, input, stdoutput, quiet):
        if sys.version_info.major == 2 and sys.version_info.minor == 7:
            from cStringIO import StringIO

            p = HieraOutputParser(text=input, quiet=quiet)

            orig_stdout = sys.stdout
            try:
                out = StringIO()
                sys.stdout = out
                p.get_python()
                output = out.getvalue().strip()
            finally:
                sys.stdout = orig_stdout

            assert_equal(stdoutput, output)
