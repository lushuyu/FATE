# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: column-expand-param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='column-expand-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=b'B\021ColumnExpandProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x63olumn-expand-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"#\n\x11\x43olumnExpandParam\x12\x0e\n\x06header\x18\x01 \x03(\tB\x13\x42\x11\x43olumnExpandProtob\x06proto3'
)




_COLUMNEXPANDPARAM = _descriptor.Descriptor(
  name='ColumnExpandParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandParam.header', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['ColumnExpandParam'] = _COLUMNEXPANDPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColumnExpandParam = _reflection.GeneratedProtocolMessageType('ColumnExpandParam', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNEXPANDPARAM,
  '__module__' : 'column_expand_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandParam)
  })
_sym_db.RegisterMessage(ColumnExpandParam)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
