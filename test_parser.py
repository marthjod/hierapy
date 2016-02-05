#!/usr/bin/python

from parser import HieraOutputParser


def main():
    assert HieraOutputParser(text="nil").get_json() == "null"
    assert HieraOutputParser(text="nil").get_python() is None

    assert HieraOutputParser(text="=>").get_json() == ":"
    assert HieraOutputParser(text="=>").get_python() == ":"

    assert HieraOutputParser(text="some string").get_json() == "some string"
    assert HieraOutputParser(text="some string").get_python() == "some string"

    assert HieraOutputParser(text="[]").get_json() == "[]"
    assert HieraOutputParser(text="[]").get_python() == []

    assert HieraOutputParser(text="{}").get_json() == "{}"
    assert HieraOutputParser(text="{}").get_python() == {}

    assert HieraOutputParser(text='{"foo"=>"bar"}').get_json() == '{"foo":"bar"}'
    assert HieraOutputParser(text='{"foo"=>"bar"}').get_python() == {"foo":"bar"}

    assert HieraOutputParser(text='{"foo" => "bar"}').get_json() == '{"foo" : "bar"}'
    assert HieraOutputParser(text='{"foo" => "bar"}').get_python() == {"foo":"bar"}

    assert HieraOutputParser(text='{"foo"=>[1,2]}').get_json() == '{"foo":[1,2]}'
    assert HieraOutputParser(text='{"foo"=>[1,2]}').get_python() == {"foo": [1, 2]}

    assert HieraOutputParser(text='{"foo"=>nil}').get_json() == '{"foo":null}'
    assert HieraOutputParser(text='{"foo"=>nil}').get_python() == {"foo": None}

    assert HieraOutputParser(text='{"foo"=>[{}, 3]}').get_json() == '{"foo":[{}, 3]}'
    assert HieraOutputParser(text='{"foo"=>[{}, 3]}').get_python() == {"foo": [{}, 3]}


if __name__ == "__main__":
    main()
