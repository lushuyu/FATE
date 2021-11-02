# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lr-model-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lr-model-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\021LRModelParamProto'),
  serialized_pb=_b('\n\x14lr-model-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\x85\x05\n\x0cLRModelParam\x12\r\n\x05iters\x18\x01 \x01(\x05\x12\x14\n\x0closs_history\x18\x02 \x03(\x01\x12\x14\n\x0cis_converged\x18\x03 \x01(\x08\x12P\n\x06weight\x18\x04 \x03(\x0b\x32@.com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.WeightEntry\x12\x11\n\tintercept\x18\x05 \x01(\x01\x12\x0e\n\x06header\x18\x06 \x03(\t\x12S\n\x12one_vs_rest_result\x18\x07 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.OneVsRestResult\x12\x18\n\x10need_one_vs_rest\x18\x08 \x01(\x08\x12\x16\n\x0e\x62\x65st_iteration\x18\t \x01(\x05\x12\x63\n\x10\x65ncrypted_weight\x18\n \x03(\x0b\x32I.com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.EncryptedWeightEntry\x12>\n\x06\x63ipher\x18\x0b \x01(\x0b\x32..com.webank.ai.fate.core.mlmodel.buffer.Cipher\x1a-\n\x0bWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1aj\n\x14\x45ncryptedWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.com.webank.ai.fate.core.mlmodel.buffer.CipherText:\x02\x38\x01\"\x93\x04\n\x0bSingleModel\x12\r\n\x05iters\x18\x01 \x01(\x05\x12\x14\n\x0closs_history\x18\x02 \x03(\x01\x12\x14\n\x0cis_converged\x18\x03 \x01(\x08\x12O\n\x06weight\x18\x04 \x03(\x0b\x32?.com.webank.ai.fate.core.mlmodel.buffer.SingleModel.WeightEntry\x12\x11\n\tintercept\x18\x05 \x01(\x01\x12\x0e\n\x06header\x18\x06 \x03(\t\x12\x16\n\x0e\x62\x65st_iteration\x18\x07 \x01(\x05\x12\x62\n\x10\x65ncrypted_weight\x18\x08 \x03(\x0b\x32H.com.webank.ai.fate.core.mlmodel.buffer.SingleModel.EncryptedWeightEntry\x12>\n\x06\x63ipher\x18\t \x01(\x0b\x32..com.webank.ai.fate.core.mlmodel.buffer.Cipher\x1a-\n\x0bWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1aj\n\x14\x45ncryptedWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.com.webank.ai.fate.core.mlmodel.buffer.CipherText:\x02\x38\x01\"}\n\x0fOneVsRestResult\x12M\n\x10\x63ompleted_models\x18\x01 \x03(\x0b\x32\x33.com.webank.ai.fate.core.mlmodel.buffer.SingleModel\x12\x1b\n\x13one_vs_rest_classes\x18\x02 \x03(\t\"\xa4\x01\n\x06\x43ipher\x12K\n\npublic_key\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey\x12M\n\x0bprivate_key\x18\x02 \x01(\x0b\x32\x38.com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey\"\x1c\n\x0f\x43ipherPublicKey\x12\t\n\x01n\x18\x01 \x01(\t\"(\n\x10\x43ipherPrivateKey\x12\t\n\x01p\x18\x01 \x01(\t\x12\t\n\x01q\x18\x02 \x01(\t\"\x97\x01\n\nCipherText\x12K\n\npublic_key\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey\x12\x13\n\x0b\x63ipher_text\x18\x02 \x01(\t\x12\x10\n\x08\x65xponent\x18\x03 \x01(\t\x12\x15\n\ris_obfuscator\x18\x04 \x01(\x08\x42\x13\x42\x11LRModelParamProtob\x06proto3')
)




_LRMODELPARAM_WEIGHTENTRY = _descriptor.Descriptor(
  name='WeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.WeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.WeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.WeightEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=602,
)

_LRMODELPARAM_ENCRYPTEDWEIGHTENTRY = _descriptor.Descriptor(
  name='EncryptedWeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.EncryptedWeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.EncryptedWeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.EncryptedWeightEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=710,
)

_LRMODELPARAM = _descriptor.Descriptor(
  name='LRModelParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.iters', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_history', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.loss_history', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.is_converged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.weight', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intercept', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.intercept', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.header', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_vs_rest_result', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.one_vs_rest_result', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_one_vs_rest', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.need_one_vs_rest', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_iteration', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.best_iteration', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encrypted_weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.encrypted_weight', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipher', full_name='com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.cipher', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LRMODELPARAM_WEIGHTENTRY, _LRMODELPARAM_ENCRYPTEDWEIGHTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=710,
)


_SINGLEMODEL_WEIGHTENTRY = _descriptor.Descriptor(
  name='WeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.WeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.WeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.WeightEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=602,
)

_SINGLEMODEL_ENCRYPTEDWEIGHTENTRY = _descriptor.Descriptor(
  name='EncryptedWeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.EncryptedWeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.EncryptedWeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.EncryptedWeightEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=710,
)

_SINGLEMODEL = _descriptor.Descriptor(
  name='SingleModel',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.iters', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_history', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.loss_history', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.is_converged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.weight', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intercept', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.intercept', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.header', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_iteration', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.best_iteration', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encrypted_weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.encrypted_weight', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipher', full_name='com.webank.ai.fate.core.mlmodel.buffer.SingleModel.cipher', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SINGLEMODEL_WEIGHTENTRY, _SINGLEMODEL_ENCRYPTEDWEIGHTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=1244,
)


_ONEVSRESTRESULT = _descriptor.Descriptor(
  name='OneVsRestResult',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.OneVsRestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='completed_models', full_name='com.webank.ai.fate.core.mlmodel.buffer.OneVsRestResult.completed_models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_vs_rest_classes', full_name='com.webank.ai.fate.core.mlmodel.buffer.OneVsRestResult.one_vs_rest_classes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1246,
  serialized_end=1371,
)


_CIPHER = _descriptor.Descriptor(
  name='Cipher',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.Cipher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='com.webank.ai.fate.core.mlmodel.buffer.Cipher.public_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='com.webank.ai.fate.core.mlmodel.buffer.Cipher.private_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1374,
  serialized_end=1538,
)


_CIPHERPUBLICKEY = _descriptor.Descriptor(
  name='CipherPublicKey',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey.n', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1540,
  serialized_end=1568,
)


_CIPHERPRIVATEKEY = _descriptor.Descriptor(
  name='CipherPrivateKey',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey.p', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey.q', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1570,
  serialized_end=1610,
)


_CIPHERTEXT = _descriptor.Descriptor(
  name='CipherText',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherText.public_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipher_text', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherText.cipher_text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exponent', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherText.exponent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_obfuscator', full_name='com.webank.ai.fate.core.mlmodel.buffer.CipherText.is_obfuscator', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1613,
  serialized_end=1764,
)

_LRMODELPARAM_WEIGHTENTRY.containing_type = _LRMODELPARAM
_LRMODELPARAM_ENCRYPTEDWEIGHTENTRY.fields_by_name['value'].message_type = _CIPHERTEXT
_LRMODELPARAM_ENCRYPTEDWEIGHTENTRY.containing_type = _LRMODELPARAM
_LRMODELPARAM.fields_by_name['weight'].message_type = _LRMODELPARAM_WEIGHTENTRY
_LRMODELPARAM.fields_by_name['one_vs_rest_result'].message_type = _ONEVSRESTRESULT
_LRMODELPARAM.fields_by_name['encrypted_weight'].message_type = _LRMODELPARAM_ENCRYPTEDWEIGHTENTRY
_LRMODELPARAM.fields_by_name['cipher'].message_type = _CIPHER
_SINGLEMODEL_WEIGHTENTRY.containing_type = _SINGLEMODEL
_SINGLEMODEL_ENCRYPTEDWEIGHTENTRY.fields_by_name['value'].message_type = _CIPHERTEXT
_SINGLEMODEL_ENCRYPTEDWEIGHTENTRY.containing_type = _SINGLEMODEL
_SINGLEMODEL.fields_by_name['weight'].message_type = _SINGLEMODEL_WEIGHTENTRY
_SINGLEMODEL.fields_by_name['encrypted_weight'].message_type = _SINGLEMODEL_ENCRYPTEDWEIGHTENTRY
_SINGLEMODEL.fields_by_name['cipher'].message_type = _CIPHER
_ONEVSRESTRESULT.fields_by_name['completed_models'].message_type = _SINGLEMODEL
_CIPHER.fields_by_name['public_key'].message_type = _CIPHERPUBLICKEY
_CIPHER.fields_by_name['private_key'].message_type = _CIPHERPRIVATEKEY
_CIPHERTEXT.fields_by_name['public_key'].message_type = _CIPHERPUBLICKEY
DESCRIPTOR.message_types_by_name['LRModelParam'] = _LRMODELPARAM
DESCRIPTOR.message_types_by_name['SingleModel'] = _SINGLEMODEL
DESCRIPTOR.message_types_by_name['OneVsRestResult'] = _ONEVSRESTRESULT
DESCRIPTOR.message_types_by_name['Cipher'] = _CIPHER
DESCRIPTOR.message_types_by_name['CipherPublicKey'] = _CIPHERPUBLICKEY
DESCRIPTOR.message_types_by_name['CipherPrivateKey'] = _CIPHERPRIVATEKEY
DESCRIPTOR.message_types_by_name['CipherText'] = _CIPHERTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LRModelParam = _reflection.GeneratedProtocolMessageType('LRModelParam', (_message.Message,), dict(

  WeightEntry = _reflection.GeneratedProtocolMessageType('WeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _LRMODELPARAM_WEIGHTENTRY,
    __module__ = 'lr_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.WeightEntry)
    ))
  ,

  EncryptedWeightEntry = _reflection.GeneratedProtocolMessageType('EncryptedWeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _LRMODELPARAM_ENCRYPTEDWEIGHTENTRY,
    __module__ = 'lr_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.LRModelParam.EncryptedWeightEntry)
    ))
  ,
  DESCRIPTOR = _LRMODELPARAM,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.LRModelParam)
  ))
_sym_db.RegisterMessage(LRModelParam)
_sym_db.RegisterMessage(LRModelParam.WeightEntry)
_sym_db.RegisterMessage(LRModelParam.EncryptedWeightEntry)

SingleModel = _reflection.GeneratedProtocolMessageType('SingleModel', (_message.Message,), dict(

  WeightEntry = _reflection.GeneratedProtocolMessageType('WeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _SINGLEMODEL_WEIGHTENTRY,
    __module__ = 'lr_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SingleModel.WeightEntry)
    ))
  ,

  EncryptedWeightEntry = _reflection.GeneratedProtocolMessageType('EncryptedWeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _SINGLEMODEL_ENCRYPTEDWEIGHTENTRY,
    __module__ = 'lr_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SingleModel.EncryptedWeightEntry)
    ))
  ,
  DESCRIPTOR = _SINGLEMODEL,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.SingleModel)
  ))
_sym_db.RegisterMessage(SingleModel)
_sym_db.RegisterMessage(SingleModel.WeightEntry)
_sym_db.RegisterMessage(SingleModel.EncryptedWeightEntry)

OneVsRestResult = _reflection.GeneratedProtocolMessageType('OneVsRestResult', (_message.Message,), dict(
  DESCRIPTOR = _ONEVSRESTRESULT,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.OneVsRestResult)
  ))
_sym_db.RegisterMessage(OneVsRestResult)

Cipher = _reflection.GeneratedProtocolMessageType('Cipher', (_message.Message,), dict(
  DESCRIPTOR = _CIPHER,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Cipher)
  ))
_sym_db.RegisterMessage(Cipher)

CipherPublicKey = _reflection.GeneratedProtocolMessageType('CipherPublicKey', (_message.Message,), dict(
  DESCRIPTOR = _CIPHERPUBLICKEY,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherPublicKey)
  ))
_sym_db.RegisterMessage(CipherPublicKey)

CipherPrivateKey = _reflection.GeneratedProtocolMessageType('CipherPrivateKey', (_message.Message,), dict(
  DESCRIPTOR = _CIPHERPRIVATEKEY,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherPrivateKey)
  ))
_sym_db.RegisterMessage(CipherPrivateKey)

CipherText = _reflection.GeneratedProtocolMessageType('CipherText', (_message.Message,), dict(
  DESCRIPTOR = _CIPHERTEXT,
  __module__ = 'lr_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.CipherText)
  ))
_sym_db.RegisterMessage(CipherText)


DESCRIPTOR._options = None
_LRMODELPARAM_WEIGHTENTRY._options = None
_LRMODELPARAM_ENCRYPTEDWEIGHTENTRY._options = None
_SINGLEMODEL_WEIGHTENTRY._options = None
_SINGLEMODEL_ENCRYPTEDWEIGHTENTRY._options = None
# @@protoc_insertion_point(module_scope)
