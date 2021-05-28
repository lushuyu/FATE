# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-binning-param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-binning-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=b'B\030FeatureBinningParamProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x66\x65\x61ture-binning-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\x85\x02\n\x07IVParam\x12\x11\n\twoe_array\x18\x01 \x03(\x01\x12\x10\n\x08iv_array\x18\x02 \x03(\x01\x12\x19\n\x11\x65vent_count_array\x18\x03 \x03(\x03\x12\x1d\n\x15non_event_count_array\x18\x04 \x03(\x03\x12\x18\n\x10\x65vent_rate_array\x18\x05 \x03(\x01\x12\x1c\n\x14non_event_rate_array\x18\x06 \x03(\x01\x12\x14\n\x0csplit_points\x18\x07 \x03(\x01\x12\n\n\x02iv\x18\x08 \x01(\x01\x12\x18\n\x10is_woe_monotonic\x18\t \x01(\x08\x12\x10\n\x08\x62in_nums\x18\n \x01(\x03\x12\x15\n\rbin_anonymous\x18\x0b \x03(\t\"\x9c\x02\n\x1fSingleLabelFeatureBinningResult\x12r\n\x0e\x62inning_result\x18\x01 \x03(\x0b\x32Z.com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.BinningResultEntry\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x10\n\x08party_id\x18\x03 \x01(\t\x1a\x65\n\x12\x42inningResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.com.webank.ai.fate.core.mlmodel.buffer.IVParam:\x02\x38\x01\"\xfe\x01\n\x14\x46\x65\x61tureBinningResult\x12g\n\x0e\x62inning_result\x18\x01 \x03(\x0b\x32O.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry\x1a}\n\x12\x42inningResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12V\n\x05value\x18\x02 \x01(\x0b\x32G.com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult:\x02\x38\x01\"R\n\x19\x42inningSingleFeatureValue\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x11\n\tcol_names\x18\x02 \x03(\t\x12\x12\n\nvalue_name\x18\x03 \x01(\t\"\xfd\x01\n\x13\x46\x65\x61tureBinningParam\x12T\n\x0e\x62inning_result\x18\x01 \x01(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12R\n\x0chost_results\x18\x02 \x03(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12\x0e\n\x06header\x18\x03 \x03(\t\x12\x18\n\x10header_anonymous\x18\x04 \x03(\t\x12\x12\n\nmodel_name\x18\x05 \x01(\tB\x1a\x42\x18\x46\x65\x61tureBinningParamProtob\x06proto3'
)




_IVPARAM = _descriptor.Descriptor(
  name='IVParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='woe_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.woe_array', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iv_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.iv_array', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_count_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.event_count_array', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_event_count_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.non_event_count_array', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_rate_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.event_rate_array', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_event_rate_array', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.non_event_rate_array', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_points', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.split_points', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iv', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.iv', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_woe_monotonic', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.is_woe_monotonic', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bin_nums', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.bin_nums', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bin_anonymous', full_name='com.webank.ai.fate.core.mlmodel.buffer.IVParam.bin_anonymous', index=10,
      number=11, type=9, cpp_type=9, label=3,
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
  serialized_start=72,
  serialized_end=333,
)


_SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY = _descriptor.Descriptor(
  name='BinningResultEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.BinningResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.BinningResultEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.BinningResultEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=620,
)

_SINGLELABELFEATUREBINNINGRESULT = _descriptor.Descriptor(
  name='SingleLabelFeatureBinningResult',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binning_result', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.binning_result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='party_id', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.party_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=620,
)


_FEATUREBINNINGRESULT_BINNINGRESULTENTRY = _descriptor.Descriptor(
  name='BinningResultEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=877,
)

_FEATUREBINNINGRESULT = _descriptor.Descriptor(
  name='FeatureBinningResult',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binning_result', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.binning_result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FEATUREBINNINGRESULT_BINNINGRESULTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=623,
  serialized_end=877,
)


_BINNINGSINGLEFEATUREVALUE = _descriptor.Descriptor(
  name='BinningSingleFeatureValue',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='col_names', full_name='com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue.col_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_name', full_name='com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue.value_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=961,
)


_FEATUREBINNINGPARAM = _descriptor.Descriptor(
  name='FeatureBinningParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binning_result', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam.binning_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_results', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam.host_results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam.header', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header_anonymous', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam.header_anonymous', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam.model_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=1217,
)

_SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY.fields_by_name['value'].message_type = _IVPARAM
_SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY.containing_type = _SINGLELABELFEATUREBINNINGRESULT
_SINGLELABELFEATUREBINNINGRESULT.fields_by_name['binning_result'].message_type = _SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY
_FEATUREBINNINGRESULT_BINNINGRESULTENTRY.fields_by_name['value'].message_type = _SINGLELABELFEATUREBINNINGRESULT
_FEATUREBINNINGRESULT_BINNINGRESULTENTRY.containing_type = _FEATUREBINNINGRESULT
_FEATUREBINNINGRESULT.fields_by_name['binning_result'].message_type = _FEATUREBINNINGRESULT_BINNINGRESULTENTRY
_FEATUREBINNINGPARAM.fields_by_name['binning_result'].message_type = _FEATUREBINNINGRESULT
_FEATUREBINNINGPARAM.fields_by_name['host_results'].message_type = _FEATUREBINNINGRESULT
DESCRIPTOR.message_types_by_name['IVParam'] = _IVPARAM
DESCRIPTOR.message_types_by_name['SingleLabelFeatureBinningResult'] = _SINGLELABELFEATUREBINNINGRESULT
DESCRIPTOR.message_types_by_name['FeatureBinningResult'] = _FEATUREBINNINGRESULT
DESCRIPTOR.message_types_by_name['BinningSingleFeatureValue'] = _BINNINGSINGLEFEATUREVALUE
DESCRIPTOR.message_types_by_name['FeatureBinningParam'] = _FEATUREBINNINGPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IVParam = _reflection.GeneratedProtocolMessageType('IVParam', (_message.Message,), {
  'DESCRIPTOR' : _IVPARAM,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVParam)
  })
_sym_db.RegisterMessage(IVParam)

SingleLabelFeatureBinningResult = _reflection.GeneratedProtocolMessageType('SingleLabelFeatureBinningResult', (_message.Message,), {

  'BinningResultEntry' : _reflection.GeneratedProtocolMessageType('BinningResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY,
    '__module__' : 'feature_binning_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult.BinningResultEntry)
    })
  ,
  'DESCRIPTOR' : _SINGLELABELFEATUREBINNINGRESULT,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SingleLabelFeatureBinningResult)
  })
_sym_db.RegisterMessage(SingleLabelFeatureBinningResult)
_sym_db.RegisterMessage(SingleLabelFeatureBinningResult.BinningResultEntry)

FeatureBinningResult = _reflection.GeneratedProtocolMessageType('FeatureBinningResult', (_message.Message,), {

  'BinningResultEntry' : _reflection.GeneratedProtocolMessageType('BinningResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREBINNINGRESULT_BINNINGRESULTENTRY,
    '__module__' : 'feature_binning_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry)
    })
  ,
  'DESCRIPTOR' : _FEATUREBINNINGRESULT,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult)
  })
_sym_db.RegisterMessage(FeatureBinningResult)
_sym_db.RegisterMessage(FeatureBinningResult.BinningResultEntry)

BinningSingleFeatureValue = _reflection.GeneratedProtocolMessageType('BinningSingleFeatureValue', (_message.Message,), {
  'DESCRIPTOR' : _BINNINGSINGLEFEATUREVALUE,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue)
  })
_sym_db.RegisterMessage(BinningSingleFeatureValue)

FeatureBinningParam = _reflection.GeneratedProtocolMessageType('FeatureBinningParam', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREBINNINGPARAM,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam)
  })
_sym_db.RegisterMessage(FeatureBinningParam)


DESCRIPTOR._options = None
_SINGLELABELFEATUREBINNINGRESULT_BINNINGRESULTENTRY._options = None
_FEATUREBINNINGRESULT_BINNINGRESULTENTRY._options = None
# @@protoc_insertion_point(module_scope)
