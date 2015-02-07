# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: layernet.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='layernet.proto',
  package='',
  serialized_pb='\n\x0elayernet.proto\"\xe1\x04\n\nLayerProto\x12#\n\x04type\x18\x06 \x02(\x0e\x32\x15.LayerProto.LayerType\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07num_out\x18\x02 \x02(\x05\x12\x11\n\x06num_in\x18\x03 \x01(\x05:\x01\x30\x12\x0c\n\x04\x66rom\x18\x04 \x03(\t\x12\x15\n\x06nobias\x18\x05 \x01(\x08:\x05\x66\x61lse\"\xd6\x03\n\tLayerType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08\x41\x43\x43URACY\x10\x01\x12\x08\n\x04\x42NLL\x10\x02\x12\n\n\x06\x43ONCAT\x10\x03\x12\x0f\n\x0b\x43ONVOLUTION\x10\x04\x12\x08\n\x04\x44\x41TA\x10\x05\x12\x0b\n\x07\x44ROPOUT\x10\x06\x12\x12\n\x0e\x45UCLIDEAN_LOSS\x10\x07\x12\x13\n\x0f\x45LTWISE_PRODUCT\x10\x19\x12\x0b\n\x07\x46LATTEN\x10\x08\x12\r\n\tHDF5_DATA\x10\t\x12\x0f\n\x0bHDF5_OUTPUT\x10\n\x12\x0e\n\nHINGE_LOSS\x10\x1c\x12\n\n\x06IM2COL\x10\x0b\x12\x0e\n\nIMAGE_DATA\x10\x0c\x12\x11\n\rINFOGAIN_LOSS\x10\r\x12\x11\n\rINNER_PRODUCT\x10\x0e\x12\x07\n\x03LRN\x10\x0f\x12\x0f\n\x0bMEMORY_DATA\x10\x1d\x12\x1d\n\x19MULTINOMIAL_LOGISTIC_LOSS\x10\x10\x12\x0b\n\x07POOLING\x10\x11\x12\t\n\x05POWER\x10\x1a\x12\x08\n\x04RELU\x10\x12\x12\x0b\n\x07SIGMOID\x10\x13\x12\x1e\n\x1aSIGMOID_CROSS_ENTROPY_LOSS\x10\x1b\x12\x0b\n\x07SOFTMAX\x10\x14\x12\x10\n\x0cSOFTMAX_LOSS\x10\x15\x12\t\n\x05SPLIT\x10\x16\x12\x08\n\x04TANH\x10\x17\x12\x0f\n\x0bWINDOW_DATA\x10\x18\"\xce\x01\n\tDataProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\npath_image\x18\x03 \x02(\t\x12\x12\n\npath_label\x18\x04 \x01(\t\x12\x16\n\x07shuffle\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06thread\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x14\n\tbatchsize\x18\x06 \x01(\x05:\x01\x31\x12\x11\n\tinputsize\x18\x64 \x01(\x05\x12\x14\n\tfileindex\x18\x62 \x01(\x05:\x01\x30\x12\x12\n\x07n_balls\x18  \x01(\x05:\x01\x33\x12\t\n\x01T\x18\x08 \x02(\x05\"\xaa\x01\n\x0cTrainerProto\x12\x0c\n\x04\x63\x64_n\x18\x07 \x01(\x05\x12\x11\n\tnum_round\x18\x01 \x02(\x05\x12\x16\n\x0eprint_interval\x18\x02 \x02(\x05\x12\x15\n\rsave_interval\x18\x03 \x02(\x05\x12\x14\n\x05\x62\x61tch\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0bsnapfrom_db\x18\r \x02(\t\x12\x11\n\tsnapto_db\x18\x0e \x02(\t\x12\x0c\n\x04load\x18\x17 \x02(\x08\"\xbc\x03\n\x04Task\x12\x1e\n\x07trainer\x18\x02 \x02(\x0b\x32\r.TrainerProto\x12\x0e\n\x06\x64ouble\x18\x37 \x02(\x08\x12\x10\n\x08numepoch\x18\x03 \x02(\x05\x12\x0f\n\x03res\x18\x33 \x01(\x05:\x02\x33\x30\x12\x11\n\x06\x64\x65vice\x18/ \x01(\x05:\x01\x30\x12\x0e\n\x06rnnrbm\x18. \x02(\x08\x12\x11\n\x04numh\x18\x07 \x01(\x05:\x03\x34\x30\x30\x12\x11\n\x03log\x18\x30 \x02(\x08:\x04true\x12\x19\n\x05\x64\x61tap\x18\x62 \x02(\x0b\x32\n.DataProto\x12\x1e\n\ndatap_test\x18\x63 \x01(\x0b\x32\n.DataProto\x12\x15\n\x08momentum\x18\t \x01(\x02:\x03\x30.9\x12\x16\n\tlearnrate\x18\n \x01(\x02:\x03\x30.1\x12\x16\n\x0bweightdecay\x18\x0b \x01(\x02:\x01\x30\x12\x11\n\x03gpu\x18\x0c \x01(\x08:\x04true\x12\x13\n\x08loglevel\x18\x61 \x01(\x05:\x01\x31\x12\x11\n\tnumrepeat\x18! \x02(\x05\x12\x13\n\x04\x64raw\x18\x10 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05train\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0bweight_size\x18\x64 \x02(\x05\x12\x1b\n\x06layers\x18\x01 \x03(\x0b\x32\x0b.LayerProto')



_LAYERPROTO_LAYERTYPE = _descriptor.EnumDescriptor(
  name='LayerType',
  full_name='LayerProto.LayerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCURACY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BNLL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONCAT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVOLUTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROPOUT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EUCLIDEAN_LOSS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELTWISE_PRODUCT', index=8, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLATTEN', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDF5_DATA', index=10, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDF5_OUTPUT', index=11, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HINGE_LOSS', index=12, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IM2COL', index=13, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_DATA', index=14, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFOGAIN_LOSS', index=15, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INNER_PRODUCT', index=16, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LRN', index=17, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEMORY_DATA', index=18, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTINOMIAL_LOGISTIC_LOSS', index=19, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POOLING', index=20, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER', index=21, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELU', index=22, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID', index=23, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID_CROSS_ENTROPY_LOSS', index=24, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTMAX', index=25, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTMAX_LOSS', index=26, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT', index=27, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TANH', index=28, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINDOW_DATA', index=29, number=24,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=158,
  serialized_end=628,
)


_LAYERPROTO = _descriptor.Descriptor(
  name='LayerProto',
  full_name='LayerProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='LayerProto.type', index=0,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='LayerProto.name', index=1,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_out', full_name='LayerProto.num_out', index=2,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_in', full_name='LayerProto.num_in', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='LayerProto.from', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nobias', full_name='LayerProto.nobias', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LAYERPROTO_LAYERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=628,
)


_DATAPROTO = _descriptor.Descriptor(
  name='DataProto',
  full_name='DataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DataProto.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_image', full_name='DataProto.path_image', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_label', full_name='DataProto.path_label', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shuffle', full_name='DataProto.shuffle', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread', full_name='DataProto.thread', index=4,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batchsize', full_name='DataProto.batchsize', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputsize', full_name='DataProto.inputsize', index=6,
      number=100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileindex', full_name='DataProto.fileindex', index=7,
      number=98, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_balls', full_name='DataProto.n_balls', index=8,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='T', full_name='DataProto.T', index=9,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=631,
  serialized_end=837,
)


_TRAINERPROTO = _descriptor.Descriptor(
  name='TrainerProto',
  full_name='TrainerProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cd_n', full_name='TrainerProto.cd_n', index=0,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_round', full_name='TrainerProto.num_round', index=1,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='print_interval', full_name='TrainerProto.print_interval', index=2,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_interval', full_name='TrainerProto.save_interval', index=3,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch', full_name='TrainerProto.batch', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapfrom_db', full_name='TrainerProto.snapfrom_db', index=5,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapto_db', full_name='TrainerProto.snapto_db', index=6,
      number=14, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='load', full_name='TrainerProto.load', index=7,
      number=23, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=840,
  serialized_end=1010,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer', full_name='Task.trainer', index=0,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double', full_name='Task.double', index=1,
      number=55, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numepoch', full_name='Task.numepoch', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='Task.res', index=3,
      number=51, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=30,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='Task.device', index=4,
      number=47, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rnnrbm', full_name='Task.rnnrbm', index=5,
      number=46, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numh', full_name='Task.numh', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log', full_name='Task.log', index=7,
      number=48, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datap', full_name='Task.datap', index=8,
      number=98, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datap_test', full_name='Task.datap_test', index=9,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum', full_name='Task.momentum', index=10,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learnrate', full_name='Task.learnrate', index=11,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weightdecay', full_name='Task.weightdecay', index=12,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu', full_name='Task.gpu', index=13,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loglevel', full_name='Task.loglevel', index=14,
      number=97, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numrepeat', full_name='Task.numrepeat', index=15,
      number=33, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='draw', full_name='Task.draw', index=16,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train', full_name='Task.train', index=17,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_size', full_name='Task.weight_size', index=18,
      number=100, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='Task.layers', index=19,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1013,
  serialized_end=1457,
)

_LAYERPROTO.fields_by_name['type'].enum_type = _LAYERPROTO_LAYERTYPE
_LAYERPROTO_LAYERTYPE.containing_type = _LAYERPROTO;
_TASK.fields_by_name['trainer'].message_type = _TRAINERPROTO
_TASK.fields_by_name['datap'].message_type = _DATAPROTO
_TASK.fields_by_name['datap_test'].message_type = _DATAPROTO
_TASK.fields_by_name['layers'].message_type = _LAYERPROTO
DESCRIPTOR.message_types_by_name['LayerProto'] = _LAYERPROTO
DESCRIPTOR.message_types_by_name['DataProto'] = _DATAPROTO
DESCRIPTOR.message_types_by_name['TrainerProto'] = _TRAINERPROTO
DESCRIPTOR.message_types_by_name['Task'] = _TASK

class LayerProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LAYERPROTO

  # @@protoc_insertion_point(class_scope:LayerProto)

class DataProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPROTO

  # @@protoc_insertion_point(class_scope:DataProto)

class TrainerProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAINERPROTO

  # @@protoc_insertion_point(class_scope:TrainerProto)

class Task(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASK

  # @@protoc_insertion_point(class_scope:Task)


# @@protoc_insertion_point(module_scope)
