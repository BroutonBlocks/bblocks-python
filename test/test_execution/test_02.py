import bblocks.execution.session
import bblocks.declaration.datatypes as bbtypes
from bblocks.execution.node import *
from bblocks.declaration.nodetype import *

class InitialList(Node):
    def __init__(self):
        super().__init__()
        self.values = Event("values", bbtypes.List(bbtypes.Int()))

    def run(self):
        self.fire(self.values, [1, 2, 3])


class Exp(Node):
    def __init__(self):
        super().__init__()
        self.result = Event("result", bbtypes.List(bbtypes.Int()))

    @handler(name="value", type=bbtypes.List(bbtypes.Int()))
    def on_process_value(self, msg):
        self.fire(self.result, msg.value ** 2, msg.id)


class Map(Node):
    def __init__(self):
        super().__init__()
        self.map_value = Event("map_value", bbtypes.Object())
        self.result = Event("result", bbtypes.List(bbtypes.Object()))
        self.requests = {}
        self.results = []
        self.counter = 0

    @handler(name="initial_values", type=bbtypes.List(bbtypes.Int()))
    def set_initial_values(self, msg):
        self.requests[msg.id] = {"result": [], "size": len(msg.value)}
        for item in msg.value:
            self.fire(self.map_value, item, msg_id=msg.id)

    @handler(name="processed_value", type=bbtypes.Object())
    def process_value(self, msg):
        self.requests[msg.id]["result"].append(msg.value)
        if len(self.requests[msg.id]["result"]) == self.requests[msg.id]["size"]:
            self.counter += 1
            self.results.append(self.requests[msg.id]["result"])
            logging.debug(self.requests[msg.id])

            self.results = []
            del self.requests[msg.id]

            # if self.counter == test_count:
            #     sock = self.context.socket(zmq.REQ)
            #     sock.connect(result_receiver.endpoint)
            #     sock.send_string(json.dumps({"results": self._results}))
            #     sock.close()


if __name__ == "__main__":
    with bblocks.execution.session.Session() as session:
        logging.basicConfig(level=logging.DEBUG)

        listNode = InitialList()
        mapNode = Map()
        expNode = Exp()

        mapNode.set_initial_values.connect(listNode.values)
        mapNode.process_value.connect(expNode.result)
        expNode.on_process_value.connect(mapNode.map_value)
        session.run()


#session.uploadProject(<user-name>, <pass>, <project>)
#session.downloadProject(<user-name>, <pass>, <project>)

# class CheckGraphExecution(unittest.TestCase):
#     def test_first(self):
#         global result_receiver
#
#         result_receiver = ResultReceiver(localhost)
#         logging.basicConfig(level=logging.CRITICAL)
#
#         declaration = create_graph()
#         config = json.loads(declaration.serializeForExecutor())
#
#         server_endpoint = 'tcp://127.0.0.1:2000'
#         myFabric = MyNodeCluster("python-service", config)
#         myFabric.start(server_endpoint)
#
#         msg = result_receiver.wait_results()
#         self.assertTrue("results" in msg)
#         for i in range(test_count):
#             for k in range(list_size):
#                 self.assertEqual(msg["results"][i][k], (i + k)**2)
#         myFabric.wait_for_finished()