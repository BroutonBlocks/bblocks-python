# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basictypes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='basictypes.proto',
  package='BasicTypes',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x62\x61sictypes.proto\x12\nBasicTypes\x1a\x19google/protobuf/any.proto\":\n\x07Message\x12\n\n\x02id\x18\x01 \x02(\x04\x12#\n\x05value\x18\x02 \x02(\x0b\x32\x14.google.protobuf.Any\"A\n\x0cNdarrayValue\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x12#\n\x05shape\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"\x1c\n\x0bStringValue\x12\r\n\x05value\x18\x01 \x02(\t\"\x1d\n\x0c\x42ooleanValue\x12\r\n\x05value\x18\x01 \x02(\x08\"\x19\n\x08IntValue\x12\r\n\x05value\x18\x01 \x02(\x03\"\x1b\n\nFloatValue\x12\r\n\x05value\x18\x01 \x02(\x01\"\x1a\n\x0b\x43\x61meraValue\x12\x0b\n\x03url\x18\x01 \x02(\t\"1\n\nTupleValue\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"0\n\tListValue\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='BasicTypes.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BasicTypes.Message.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='BasicTypes.Message.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=117,
)


_NDARRAYVALUE = _descriptor.Descriptor(
  name='NdarrayValue',
  full_name='BasicTypes.NdarrayValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='BasicTypes.NdarrayValue.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='BasicTypes.NdarrayValue.shape', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=184,
)


_STRINGVALUE = _descriptor.Descriptor(
  name='StringValue',
  full_name='BasicTypes.StringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='BasicTypes.StringValue.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=214,
)


_BOOLEANVALUE = _descriptor.Descriptor(
  name='BooleanValue',
  full_name='BasicTypes.BooleanValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='BasicTypes.BooleanValue.value', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=245,
)


_INTVALUE = _descriptor.Descriptor(
  name='IntValue',
  full_name='BasicTypes.IntValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='BasicTypes.IntValue.value', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=272,
)


_FLOATVALUE = _descriptor.Descriptor(
  name='FloatValue',
  full_name='BasicTypes.FloatValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='BasicTypes.FloatValue.value', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=301,
)


_CAMERAVALUE = _descriptor.Descriptor(
  name='CameraValue',
  full_name='BasicTypes.CameraValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='BasicTypes.CameraValue.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=329,
)


_TUPLEVALUE = _descriptor.Descriptor(
  name='TupleValue',
  full_name='BasicTypes.TupleValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='BasicTypes.TupleValue.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=380,
)


_LISTVALUE = _descriptor.Descriptor(
  name='ListValue',
  full_name='BasicTypes.ListValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='BasicTypes.ListValue.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=430,
)

_MESSAGE.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_NDARRAYVALUE.fields_by_name['shape'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TUPLEVALUE.fields_by_name['items'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LISTVALUE.fields_by_name['items'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['NdarrayValue'] = _NDARRAYVALUE
DESCRIPTOR.message_types_by_name['StringValue'] = _STRINGVALUE
DESCRIPTOR.message_types_by_name['BooleanValue'] = _BOOLEANVALUE
DESCRIPTOR.message_types_by_name['IntValue'] = _INTVALUE
DESCRIPTOR.message_types_by_name['FloatValue'] = _FLOATVALUE
DESCRIPTOR.message_types_by_name['CameraValue'] = _CAMERAVALUE
DESCRIPTOR.message_types_by_name['TupleValue'] = _TUPLEVALUE
DESCRIPTOR.message_types_by_name['ListValue'] = _LISTVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.Message)
  })
_sym_db.RegisterMessage(Message)

NdarrayValue = _reflection.GeneratedProtocolMessageType('NdarrayValue', (_message.Message,), {
  'DESCRIPTOR' : _NDARRAYVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.NdarrayValue)
  })
_sym_db.RegisterMessage(NdarrayValue)

StringValue = _reflection.GeneratedProtocolMessageType('StringValue', (_message.Message,), {
  'DESCRIPTOR' : _STRINGVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.StringValue)
  })
_sym_db.RegisterMessage(StringValue)

BooleanValue = _reflection.GeneratedProtocolMessageType('BooleanValue', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEANVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.BooleanValue)
  })
_sym_db.RegisterMessage(BooleanValue)

IntValue = _reflection.GeneratedProtocolMessageType('IntValue', (_message.Message,), {
  'DESCRIPTOR' : _INTVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.IntValue)
  })
_sym_db.RegisterMessage(IntValue)

FloatValue = _reflection.GeneratedProtocolMessageType('FloatValue', (_message.Message,), {
  'DESCRIPTOR' : _FLOATVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.FloatValue)
  })
_sym_db.RegisterMessage(FloatValue)

CameraValue = _reflection.GeneratedProtocolMessageType('CameraValue', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.CameraValue)
  })
_sym_db.RegisterMessage(CameraValue)

TupleValue = _reflection.GeneratedProtocolMessageType('TupleValue', (_message.Message,), {
  'DESCRIPTOR' : _TUPLEVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.TupleValue)
  })
_sym_db.RegisterMessage(TupleValue)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), {
  'DESCRIPTOR' : _LISTVALUE,
  '__module__' : 'basictypes_pb2'
  # @@protoc_insertion_point(class_scope:BasicTypes.ListValue)
  })
_sym_db.RegisterMessage(ListValue)


# @@protoc_insertion_point(module_scope)
