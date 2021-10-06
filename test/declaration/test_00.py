import unittest

from broutonblocks.declaration import Project, SessionInfo
from broutonblocks.typesparser import TypesParser


class CheckDeclaration_00(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super(CheckDeclaration_00, self).__init__(methodName)
        self.my_type = """
                node FirstNode:
                    properties:
                        threshold?: float(0.8) // default value
                        border_width: int(10)
                """

    def test(self):
        try:
            parser = TypesParser()
            node_types = parser.parse(self.my_type)
            my_node_type = node_types["FirstNode"]

            project = Project()
            project.register_types([my_node_type])

            session = SessionInfo()
            my_node = project.add_node(my_node_type, session)
            my_node.set_property("threshold", 0.5)

            project.serialize()
        except RuntimeError:
            self.fail("test_graph_properties01")