#!/usr/bin/python

from parser import HieraOutputParser


def main():
    assert HieraOutputParser(text='''nil''').result is None
    assert HieraOutputParser(text='''9''').result == 9
    assert HieraOutputParser(text='''some string''').result == "some string"
    assert HieraOutputParser(text='''[]''').result == []

if __name__ == "__main__":
    main()