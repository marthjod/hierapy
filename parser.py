import json

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor


class HieraOutputParser(NodeVisitor):

    grammar = """
        input          = token*
        token          = nil / arrow / quote / rest
        nil            = "nil"
        arrow          = "=>"
        quote          = '"'
        rest           = ~r"[a-z 0-9\[\]\{\},]*"i
    """

    def __init__(self, grammar=None, text=None):
        self.grammar = grammar or HieraOutputParser.grammar
        ast = Grammar(self.grammar).parse(text)
        self.result = []
        self.visit(ast)

    def visit_nil(self, node, children):
        self.result.append("null")

    def visit_arrow(self, node, children):
        self.result.append(":")

    def visit_quote(self, node, children):
        self.result.append(node.text)

    def visit_rest(self, node, children):
        self.result.append(node.text)

    def generic_visit(self, node, children):
        pass

    def get_json(self):
        return "".join(self.result)

    def get_python(self):
        j = self.get_json()
        try:
            return json.loads(j)
        except ValueError:
            return j
