# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/traffic_maneuver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3sensoris/protobuf/categories/traffic_maneuver.proto\x12,sensoris.protobuf.categories.trafficmaneuver\x1a\"sensoris/protobuf/types/base.proto\"\xf1\x04\n\x08Maneuver\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12\x65\n\x13type_and_confidence\x18\x02 \x01(\x0b\x32H.sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence\x1a\xbe\x03\n\x11TypeAndConfidence\x12[\n\x04type\x18\x01 \x01(\x0e\x32M.sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\x8d\x02\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0b\n\x07\x45VASIVE\x10\x01\x12\x0f\n\x0bLANE_CHANGE\x10\x02\x12\x15\n\x11LANE_CHANGE_RIGHT\x10\x03\x12\x14\n\x10LANE_CHANGE_LEFT\x10\x04\x12\x0e\n\nOVERTAKING\x10\x05\x12\x15\n\x11INTERSECTION_STOP\x10\x06\x12\x0b\n\x07TURNING\x10\x07\x12\x11\n\rTURNING_RIGHT\x10\x08\x12\x10\n\x0cTURNING_LEFT\x10\t\x12\x17\n\x13SHARP_TURNING_RIGHT\x10\n\x12\x16\n\x12SHARP_TURNING_LEFT\x10\x0b\x12\x10\n\x0c\x41\x43\x43\x45LERATING\x10\x0c\x12\x0c\n\x08\x42REAKING\x10\r\"\xb4\x03\n\x08\x43harging\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12I\n\x04type\x18\x02 \x01(\x0e\x32;.sensoris.protobuf.categories.trafficmaneuver.Charging.Type\x12W\n\x14voltage_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x12W\n\x14\x63urrent_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x01\"l\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0e\n\nPORT_J1772\x10\x01\x12\x0b\n\x07\x43HADEMO\x10\x02\x12\r\n\tSAE_COMBO\x10\x03\x12\x0e\n\nTESLA_HPWC\x10\x04\x12\x16\n\x12TESLA_SUPERCHARGER\x10\x05\"\x86\x03\n\tRefueling\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12J\n\x04type\x18\x02 \x01(\x0e\x32<.sensoris.protobuf.categories.trafficmaneuver.Refueling.Type\x12`\n\x1dquantity_to_full_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x01\"\x8b\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x12\n\x0ePETROL_PREMIUM\x10\x01\x12\x10\n\x0cPETROL_SUPER\x10\x02\x12\n\n\x06\x44IESEL\x10\x03\x12\x07\n\x03LPG\x10\x04\x12\x07\n\x03\x43NG\x10\x05\x12\x0e\n\nBIO_DIESEL\x10\x06\x12\x0f\n\x0b\x42IO_ETHANOL\x10\x07\x12\x0c\n\x08HYDROGEN\x10\x08\"\xbb\x02\n\x17TrafficManeuverCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12H\n\x08maneuver\x18\x02 \x03(\x0b\x32\x36.sensoris.protobuf.categories.trafficmaneuver.Maneuver\x12H\n\x08\x63harging\x18\x03 \x03(\x0b\x32\x36.sensoris.protobuf.categories.trafficmaneuver.Charging\x12J\n\trefueling\x18\x04 \x03(\x0b\x32\x37.sensoris.protobuf.categories.trafficmaneuver.RefuelingB\x86\x01\n\'org.sensoris.categories.trafficmaneuverB\x1fSensorisTrafficManeuverCategoryP\x01Z5sensoris.org/specification/categories/trafficmaneuver\xf8\x01\x01\x62\x06proto3')



_MANEUVER = DESCRIPTOR.message_types_by_name['Maneuver']
_MANEUVER_TYPEANDCONFIDENCE = _MANEUVER.nested_types_by_name['TypeAndConfidence']
_CHARGING = DESCRIPTOR.message_types_by_name['Charging']
_REFUELING = DESCRIPTOR.message_types_by_name['Refueling']
_TRAFFICMANEUVERCATEGORY = DESCRIPTOR.message_types_by_name['TrafficManeuverCategory']
_MANEUVER_TYPEANDCONFIDENCE_TYPE = _MANEUVER_TYPEANDCONFIDENCE.enum_types_by_name['Type']
_CHARGING_TYPE = _CHARGING.enum_types_by_name['Type']
_REFUELING_TYPE = _REFUELING.enum_types_by_name['Type']
Maneuver = _reflection.GeneratedProtocolMessageType('Maneuver', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _MANEUVER_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Maneuver.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _MANEUVER,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Maneuver)
  })
_sym_db.RegisterMessage(Maneuver)
_sym_db.RegisterMessage(Maneuver.TypeAndConfidence)

Charging = _reflection.GeneratedProtocolMessageType('Charging', (_message.Message,), {
  'DESCRIPTOR' : _CHARGING,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Charging)
  })
_sym_db.RegisterMessage(Charging)

Refueling = _reflection.GeneratedProtocolMessageType('Refueling', (_message.Message,), {
  'DESCRIPTOR' : _REFUELING,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.Refueling)
  })
_sym_db.RegisterMessage(Refueling)

TrafficManeuverCategory = _reflection.GeneratedProtocolMessageType('TrafficManeuverCategory', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICMANEUVERCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.traffic_maneuver_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.trafficmaneuver.TrafficManeuverCategory)
  })
_sym_db.RegisterMessage(TrafficManeuverCategory)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'org.sensoris.categories.trafficmaneuverB\037SensorisTrafficManeuverCategoryP\001Z5sensoris.org/specification/categories/trafficmaneuver\370\001\001'
  _CHARGING.fields_by_name['voltage_and_accuracy']._options = None
  _CHARGING.fields_by_name['voltage_and_accuracy']._serialized_options = b'\210\265\030\000'
  _CHARGING.fields_by_name['current_and_accuracy']._options = None
  _CHARGING.fields_by_name['current_and_accuracy']._serialized_options = b'\210\265\030\001'
  _REFUELING.fields_by_name['quantity_to_full_and_accuracy']._options = None
  _REFUELING.fields_by_name['quantity_to_full_and_accuracy']._serialized_options = b'\210\265\030\001'
  _MANEUVER._serialized_start=138
  _MANEUVER._serialized_end=763
  _MANEUVER_TYPEANDCONFIDENCE._serialized_start=317
  _MANEUVER_TYPEANDCONFIDENCE._serialized_end=763
  _MANEUVER_TYPEANDCONFIDENCE_TYPE._serialized_start=494
  _MANEUVER_TYPEANDCONFIDENCE_TYPE._serialized_end=763
  _CHARGING._serialized_start=766
  _CHARGING._serialized_end=1202
  _CHARGING_TYPE._serialized_start=1094
  _CHARGING_TYPE._serialized_end=1202
  _REFUELING._serialized_start=1205
  _REFUELING._serialized_end=1595
  _REFUELING_TYPE._serialized_start=1456
  _REFUELING_TYPE._serialized_end=1595
  _TRAFFICMANEUVERCATEGORY._serialized_start=1598
  _TRAFFICMANEUVERCATEGORY._serialized_end=1913
# @@protoc_insertion_point(module_scope)
