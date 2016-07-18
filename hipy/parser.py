# encoding: utf-8

import json

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor


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

    def __init__(self, grammar=None, text=None, debug=False, quiet=False):
        self.grammar = grammar or HieraOutputParser.grammar
        self.debug = debug
        self.quiet = quiet
        ast = Grammar(self.grammar).parse(text)
        self.result = []
        self.visit(ast)

    def visit_nil(self, node, children):
        if self.debug:
            self.safe_print(node)
        self.result.append("null")

    def visit_arrow(self, node, children):
        if self.debug:
            self.safe_print(node)
        self.result.append(":")

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
        if self.debug:
            self.safe_print(node)
        self.result.append(node.text)

    @staticmethod
    def safe_print(inp):
        try:
            print inp
        except UnicodeDecodeError:
            # TODO printing here may lead to problems preventing the parser
            # from continuing
            pass

    def generic_visit(self, node, children):
        pass

    def get_json(self):
        return "".join(self.result)

    def get_python(self):
        j = self.get_json()
        try:
            return json.loads(j)
        except ValueError as err:
            if not self.quiet:
                self.safe_print(err)
            return j
