from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor


class HieraOutputParser(NodeVisitor):

    grammar = """
        value          = nil / int / string / array / hash
        array          = empty_array / nonempty_array
        empty_array    = open_bracket whitespace close_bracket
        nonempty_array = open_bracket whitespace value (whitespace comma whitespace value)* whitespace close_bracket
        hash           = empty_hash / nonempty_hash
        empty_hash     = open_curly whitespace close_curly
        nonempty_hash  = open_curly whitespace key whitespace arrow whitespace value whitespace close_curly
        open_bracket   = "["
        close_bracket  = "]"
        open_curly     = "{"
        close_curly    = "}"
        nil            = "nil"
        whitespace     = " "*
        comma          = whitespace* "," whitespace*
        string         = ~"[A-Z 0-9]*"i
        key            = string # alias
        int            = ~"[0-9]+"
        arrow          = "=>"
    """

    def __init__(self, grammar=None, text=None):
        self.grammar = grammar or HieraOutputParser.grammar
        ast = Grammar(self.grammar).parse(text)
        self.result = None
        self.visit(ast)

    def visit_empty_array(self, node, children):
        self.result = []

    def visit_nonempty_array(self, node, children):
        print node
        self.result = node.text

    def visit_nil(self, node, children):
        self.result = None

    def visit_int(self, node, children):
        try:
            self.result = int(node.text)
        except ValueError:
            self.result = node.text

    def visit_string(self, node, children):
        self.result = node.text

    def generic_visit(self, node, children):
        pass
