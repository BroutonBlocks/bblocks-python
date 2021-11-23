class ProgrammingLanguage:
    Python = (0,)
    Cpp = (1,)
    NodeJs = (2,)


class Attribute:
    def __init__(self):
        self.name = ""
        self.values = {}


class MetaInfo:
    def __init__(self, **kwargs):
        pass


class PropertyDeclaration:
    def __init__(self, data_type, optional, default_value=None,):
        self.data_type = data_type
        self.optional = optional
        self.default_value = default_value

    @property
    def uid(self):
        return "property"

    def __str__(self):
        if self.default_value is None:
            return f'{self.name}: {self.data_type}'
        else:
            return f'{self.name}: {self.data_type}({self.default_value})'


class MethodDeclaration:
    def __init__(self, name, data_type, info=None):
        self.name = name
        self.data_type = data_type

    @property
    def argument_names(self):
        return self.data_type.names

    @property
    def argument_types(self):
        return self.data_type.item_types



class HandlerDeclaration(MethodDeclaration):
    def __init__(self, name, data_type, receives_multiple, info=None):
        super(HandlerDeclaration, self).__init__(name, data_type, info)
        self.receives_multiple = receives_multiple

    def __str__(self):
        result = f'{self.name}+' if self.receives_multiple else f'{self.name}'
        result += f'{tuple(f"value{idx}: {arg_type}" for idx, arg_type in enumerate(self.argument_types, start=1))}'
        return result.replace("'", '').replace(',)', ')')

    @property
    def uid(self):
        return self.name


class EventDeclaration(MethodDeclaration):
    def __str__(self):
        result = "{type}".format(type=self.data_type)
        return result

    @property
    def uid(self):
        return self.name

    def __str__(self):
        result = f'{self.name}'
        result += f'{tuple(f"value{idx}: {arg_type}" for idx, arg_type in enumerate(self.argument_types, start=1))}'
        return result.replace("'", '').replace(',)', ')')


class NodeTypeDeclaration:
    def __init__(self):
        self.handlers = {}
        self.events = {}
        self.properties = {}
        self.name = None
        self.attributes = {}

    # TODO
    @property
    def namespace(self):
        try:
            return self.attributes["namespace"].values["value"]
        except Exception:
            pass
        return "global"

    @property
    def uid(self):
        if self.namespace == "global":
            return self.name
        return ":".join([self.namespace, self.name])

    def __str__(self):
        result = "node {name}\n".format(name=self.name)
        properties = "\tproperties:\n"
        for value in self.properties.values():
            properties += "\t\t{prop}\n".format(prop=str(value))
        if properties != "\tproperties:\n":
            result += properties
        handlers = "\thandlers:\n"
        for value in self.handlers.values():
            handlers += "\t\t{handler}\n".format(handler=str(value))
        if properties != "\thandlers:\n":
            result += handlers
        events = "\tevents:\n"
        for value in self.events.values():
            events += "\t\t{event}\n".format(event=str(value))
        if properties != "\tevents:\n":
            result += events
        return result

    # def serialize(self):
    #     result = {"name": self.name}
    #
    #     handlers = {}
    #     for item in self.handlers.values():
    #         handlers[item.id] = item.serialize()
    #     result["handlers"] = handlers
    #
    #     events = {}
    #     for item in self.events.values():
    #         events[item.id] = item.serialize()
    #     result["events"] = events
    #
    #     declaration = {}
    #     for item in self.declaration.values():
    #         declaration[item.id] = item.serialize()
    #     result["declaration"] = declaration
    #
    #     return result
    #
    #     # for n in self.nodes.values():
    #     #     declaration = {}
    #     #     for prop_name, info in n.type.declaration.items():
    #     #         prop_value = info.default_value
    #     #         if prop_name in n.property_values:
    #     #             prop_value = n.property_values[prop_name]
    #     #         if prop_value != None:
    #     #             declaration[prop_name] = base64.b64encode(
    #     #                 ProtoSerializer().serialize_message(0, prop_value)
    #     #                 .SerializeToString()
    #     #             ).decode('ascii')
    #     #     result["nodes"][n.id] = {
    #     #         "type": {
    #     #             "name": n.type.name,
    #     #             "declaration": declaration
    #     #         }
    #     #     }
