import unittest

from caracal.declaration import datatypes
from caracal.execution import Event, handler, Node, Session

result = 0


class TicksGen(Node):
    tick = Event("tick", datatypes.Tuple(datatypes.Int()))

    def run(self):
        for i in range(1, 5):
            self.fire(self.tick, i)


class DoSmth(Node):
    output = Event("output", datatypes.Tuple(datatypes.Int()))

    @handler("input_number", datatypes.Tuple(datatypes.Int()))
    def input_numbers(self, msg):
        self.fire(self.output, msg.value, msg.id)


class DoSmthWithErr(Node):
    output = Event("output", datatypes.Tuple(datatypes.Int()))

    @handler("input_number", datatypes.Tuple(datatypes.Int()))
    def input_number(self, msg):
        if msg.value not in [2, 3]:
            self.fire(self.output, msg.value, msg.id)


class Summat(Node):
    @handler("input_numbers", datatypes.Tuple(datatypes.Object()), True)
    def input_numbers(self, msgs):
        global result
        result += sum((msg.value for msg in msgs.value))
        if result == 15:
            print(result)
            self.terminate()


class MultiplaHandlers(unittest.TestCase):
    def test_something(self):
        with Session() as session:
            gen = TicksGen()
            action1 = DoSmth(id_="action1")
            action2 = DoSmthWithErr(id_="action2")
            action3 = DoSmth(id_="action3")
            summat = Summat()

            action1.input_numbers.connect(gen.tick)
            action2.input_number.connect(gen.tick)
            action3.input_numbers.connect(gen.tick)

            summat.input_numbers.connect(action1.output)
            summat.input_numbers.connect(action2.output)
            summat.input_numbers.connect(action3.output)

            session.run()
        global result
        self.assertEqual(result, 15)