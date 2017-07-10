# encoding: utf-8

from __future__ import print_function, unicode_literals

import json

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
from parsimonious.exceptions import IncompleteParseError


class HieraOutputParser(NodeVisitor):

    grammar = """
        input          = token*
        token          = nil / symbol / array / hash / string / whitespace

        nil            = "nil"

        arrow          = "=>"
        comma          = ","
        quote          = '"'
        equals         = ~r"=(?!>)" # negative lookahead
        open_bracket   = "["
        close_bracket  = "]"
        open_curly     = "{"
        close_curly    = "}"
        symbol         = arrow / comma / quote / equals / open_bracket / close_bracket / open_curly / close_curly

        whitespace     = ~"[\\n\\s]*"

        array          = open_bracket token* close_bracket
        hash           = open_curly token* close_curly
        string         = whitespace* chars whitespace*
        chars          = ~r"[a-zäöüÄÖÜß0-9@!%$%&\/\(\)~\+*#,;\.:\-_\|\?\\\\]*"i
    """

    def __init__(self, grammar=None, text=None, debug=False, quiet=False,
                 encoding='iso-8859-1'):
        self.grammar = grammar or HieraOutputParser.grammar
        self.debug = debug
        self.quiet = quiet
        self.result = text
        self.encoding = encoding
        try:
            ast = Grammar(self.grammar).parse(text)
        except IncompleteParseError as err:
            if not self.quiet:
                print(err)
        else:
            self.result = []
            self.visit(ast)

    def visit_nil(self, node, children):
        self.result.append("null")
        if self.debug:
            print(node)

    def visit_arrow(self, node, children):
        self.result.append(":")
        if self.debug:
            print(node)

    def visit_quote(self, node, children):
        self.replay(node)

    def visit_open_bracket(self, node, children):
        self.replay(node)

    def visit_close_bracket(self, node, children):
        self.replay(node)

    def visit_open_curly(self, node, children):
        self.replay(node)

    def visit_close_curly(self, node, children):
        self.replay(node)

    def visit_comma(self, node, children):
        self.replay(node)

    def visit_chars(self, node, children):
        self.replay(node)

    def visit_equals(self, node, children):
        self.replay(node)

    def visit_whitespace(self, node, children):
        self.replay(node)

    def replay(self, node):
        self.result.append(node.text)
        if self.debug:
            print(node)

    def generic_visit(self, node, children):
        pass

    def get_json(self):
        return "".join(self.result)

    def get_python(self):
        j = self.get_json()
        try:
            return json.loads(j.encode(self.encoding).decode())
        except Exception as err:
            if not self.quiet:
                print("HieraOutputParser: {err}.".format(err=err))
        return j
