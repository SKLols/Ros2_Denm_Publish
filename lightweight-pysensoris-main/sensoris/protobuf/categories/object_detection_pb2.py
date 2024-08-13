# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/categories/object_detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from sensoris.protobuf.types import base_pb2 as sensoris_dot_protobuf_dot_types_dot_base__pb2
from sensoris.protobuf.types import spatial_pb2 as sensoris_dot_protobuf_dot_types_dot_spatial__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3sensoris/protobuf/categories/object_detection.proto\x12,sensoris.protobuf.categories.objectdetection\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\"sensoris/protobuf/types/base.proto\x1a%sensoris/protobuf/types/spatial.proto\"\xfb\x08\n\rMovableObject\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12.\n\tobject_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n\x14\x65xistence_confidence\x18\x03 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\x12L\n\x10\x64\x65tection_status\x18\x04 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12j\n\x13type_and_confidence\x18\x05 \x01(\x0b\x32M.sensoris.protobuf.categories.objectdetection.MovableObject.TypeAndConfidence\x12`\n\x1crectangular_box_and_accuracy\x18\x06 \x01(\x0b\x32:.sensoris.protobuf.types.spatial.RectangularBoxAndAccuracy\x12W\n\x12speed_and_accuracy\x18\x07 \x01(\x0b\x32\x35.sensoris.protobuf.types.spatial.XyzVectorAndAccuracyB\x04\x88\xb5\x18\x01\x12^\n\x19\x61\x63\x63\x65leration_and_accuracy\x18\x08 \x01(\x0b\x32\x35.sensoris.protobuf.types.spatial.XyzVectorAndAccuracyB\x04\x88\xb5\x18\x01\x12<\n\x11\x63ovariance_matrix\x18\t \x03(\x0b\x32\x1b.google.protobuf.Int64ValueB\x04\x88\xb5\x18\x01\x1a\x9f\x03\n\x11TypeAndConfidence\x12`\n\x04type\x18\x01 \x01(\x0e\x32R.sensoris.protobuf.categories.objectdetection.MovableObject.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\xe9\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\x12\x19\n\x15VEHICLE_PASSENGER_CAR\x10\x02\x12\x11\n\rVEHICLE_TRUCK\x10\x03\x12\x0f\n\x0bVEHICLE_BUS\x10\x04\x12\x10\n\x0cVEHICLE_TRAM\x10\x05\x12\x13\n\x0fVEHICLE_TRAILER\x10\x06\x12\x0f\n\x0bTWO_WHEELER\x10\x07\x12\x1a\n\x16TWO_WHEELER_MOTORCYCLE\x10\x08\x12\x17\n\x13TWO_WHEELER_BICYCLE\x10\t\x12\n\n\x06PERSON\x10\n\x12\n\n\x06\x41NIMAL\x10\x0b\"\xd9\x17\n\x0cStaticObject\x12=\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32+.sensoris.protobuf.types.base.EventEnvelope\x12.\n\tobject_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n\x14\x65xistence_confidence\x18\x03 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\x12L\n\x10\x64\x65tection_status\x18\x04 \x01(\x0b\x32\x32.sensoris.protobuf.types.base.EventDetectionStatus\x12i\n\x13type_and_confidence\x18\x05 \x01(\x0b\x32L.sensoris.protobuf.categories.objectdetection.StaticObject.TypeAndConfidence\x12\x62\n\x1crectangular_box_and_accuracy\x18\x06 \x01(\x0b\x32:.sensoris.protobuf.types.spatial.RectangularBoxAndAccuracyH\x00\x12g\n\x11\x63one_and_accuracy\x18\x07 \x01(\x0b\x32J.sensoris.protobuf.categories.objectdetection.StaticObject.ConeAndAccuracyH\x00\x12x\n\x1bsurface_type_and_confidence\x18\x08 \x01(\x0b\x32S.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceTypeAndConfidence\x12\x80\x01\n\x1fsurface_material_and_confidence\x18\t \x01(\x0b\x32W.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceMaterialAndConfidence\x12z\n\x1csurface_color_and_confidence\x18\n \x03(\x0b\x32T.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceColorAndConfidence\x1a\xea\x04\n\x11TypeAndConfidence\x12_\n\x04type\x18\x01 \x01(\x0e\x32Q.sensoris.protobuf.categories.objectdetection.StaticObject.TypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\xb5\x03\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\n\n\x06\x42RIDGE\x10\x01\x12\n\n\x06TUNNEL\x10\x02\x12\x08\n\x04POLE\x10\x03\x12\x0e\n\nPOLE_LIGHT\x10\x04\x12\x12\n\x0ePOLE_REFLECTOR\x10\x05\x12\x13\n\x0fPOLE_DELINEATOR\x10\x06\x12\x0f\n\x0bPOLE_GANTRY\x10\x07\x12\r\n\tPOLE_SIGN\x10\x08\x12\x13\n\x0fPOLE_GUARD_RAIL\x10\t\x12\x07\n\x03\x42\x41R\x10\n\x12\x08\n\x04TREE\x10\x0b\x12\x0b\n\x07\x42OLLARD\x10\x0c\x12\x08\n\x04\x43ONE\x10\r\x12\n\n\x06\x42\x41RREL\x10\x0e\x12\x08\n\x04WALL\x10\x0f\x12\x12\n\x0eTRAFFIC_ISLAND\x10\x10\x12\x0e\n\nSPEED_BUMP\x10\x11\x12\x0c\n\x08POT_HOLE\x10\x12\x12\x11\n\rMANHOLE_COVER\x10\x13\x12\x18\n\x14MANHOLE_COVER_CLOSED\x10\x14\x12\x16\n\x12MANHOLE_COVER_OPEN\x10\x15\x12\x0f\n\x0bSIGN_BRIDGE\x10\x16\x12\x16\n\x12TRAFFIC_LIGHT_BODY\x10\x17\x12\x17\n\x13\x42\x41RRIER_PARKING_LOT\x10\x18\x12\x12\n\x0eSURFACE_RAISED\x10\x19\x1a\xb0\x03\n\x0f\x43oneAndAccuracy\x12Y\n\x1blower_position_and_accuracy\x18\x01 \x01(\x0b\x32\x34.sensoris.protobuf.types.spatial.PositionAndAccuracy\x12Y\n\x1bupper_position_and_accuracy\x18\x02 \x01(\x0b\x32\x34.sensoris.protobuf.types.spatial.PositionAndAccuracy\x12^\n\x1blower_diameter_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x12^\n\x1bupper_diameter_and_accuracy\x18\x04 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\x12\'\n\textension\x18\x0f \x03(\x0b\x32\x14.google.protobuf.Any\x1a\xef\x01\n\x18SurfaceTypeAndConfidence\x12\x66\n\x04type\x18\x01 \x01(\x0e\x32X.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceTypeAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"-\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x08\n\x04\x46LAT\x10\x01\x12\t\n\x05ROUGH\x10\x02\x1a\x95\x03\n\x1cSurfaceMaterialAndConfidence\x12j\n\x04type\x18\x01 \x01(\x0e\x32\\.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceMaterialAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\x12\\\n\x19reflectivity_and_accuracy\x18\x03 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64ValueAndAccuracyB\x04\x88\xb5\x18\x00\"m\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\t\n\x05METAL\x10\x01\x12\x0c\n\x08\x43ONCRETE\x10\x02\x12\t\n\x05STONE\x10\x03\x12\x08\n\x04WOOD\x10\x04\x12\x0b\n\x07PLASTIC\x10\x05\x12\x0b\n\x07\x41SPHALT\x10\x06\x12\x0b\n\x07ORGANIC\x10\x07\x1a\xdc\x02\n\x19SurfaceColorAndConfidence\x12g\n\x04type\x18\x01 \x01(\x0e\x32Y.sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceColorAndConfidence.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\x97\x01\n\x04Type\x12\x0f\n\x0bUNKOWN_TYPE\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\x08\n\x04GRAY\x10\x03\x12\x0e\n\nGRAY_LIGHT\x10\x04\x12\r\n\tGRAY_DARK\x10\x05\x12\t\n\x05\x42LACK\x10\x06\x12\x07\n\x03RED\x10\x07\x12\t\n\x05GREEN\x10\x08\x12\x08\n\x04\x42LUE\x10\t\x12\n\n\x06YELLOW\x10\n\x12\n\n\x06ORANGE\x10\x0b\x42\n\n\x08geometry\"\x83\x02\n\x17ObjectDetectionCategory\x12@\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.CategoryEnvelope\x12S\n\x0emovable_object\x18\x02 \x03(\x0b\x32;.sensoris.protobuf.categories.objectdetection.MovableObject\x12Q\n\rstatic_object\x18\x03 \x03(\x0b\x32:.sensoris.protobuf.categories.objectdetection.StaticObjectB\x86\x01\n\'org.sensoris.categories.objectdetectionB\x1fSensorisObjectDetectionCategoryP\x01Z5sensoris.org/specification/categories/objectdetection\xf8\x01\x01\x62\x06proto3')



_MOVABLEOBJECT = DESCRIPTOR.message_types_by_name['MovableObject']
_MOVABLEOBJECT_TYPEANDCONFIDENCE = _MOVABLEOBJECT.nested_types_by_name['TypeAndConfidence']
_STATICOBJECT = DESCRIPTOR.message_types_by_name['StaticObject']
_STATICOBJECT_TYPEANDCONFIDENCE = _STATICOBJECT.nested_types_by_name['TypeAndConfidence']
_STATICOBJECT_CONEANDACCURACY = _STATICOBJECT.nested_types_by_name['ConeAndAccuracy']
_STATICOBJECT_SURFACETYPEANDCONFIDENCE = _STATICOBJECT.nested_types_by_name['SurfaceTypeAndConfidence']
_STATICOBJECT_SURFACEMATERIALANDCONFIDENCE = _STATICOBJECT.nested_types_by_name['SurfaceMaterialAndConfidence']
_STATICOBJECT_SURFACECOLORANDCONFIDENCE = _STATICOBJECT.nested_types_by_name['SurfaceColorAndConfidence']
_OBJECTDETECTIONCATEGORY = DESCRIPTOR.message_types_by_name['ObjectDetectionCategory']
_MOVABLEOBJECT_TYPEANDCONFIDENCE_TYPE = _MOVABLEOBJECT_TYPEANDCONFIDENCE.enum_types_by_name['Type']
_STATICOBJECT_TYPEANDCONFIDENCE_TYPE = _STATICOBJECT_TYPEANDCONFIDENCE.enum_types_by_name['Type']
_STATICOBJECT_SURFACETYPEANDCONFIDENCE_TYPE = _STATICOBJECT_SURFACETYPEANDCONFIDENCE.enum_types_by_name['Type']
_STATICOBJECT_SURFACEMATERIALANDCONFIDENCE_TYPE = _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE.enum_types_by_name['Type']
_STATICOBJECT_SURFACECOLORANDCONFIDENCE_TYPE = _STATICOBJECT_SURFACECOLORANDCONFIDENCE.enum_types_by_name['Type']
MovableObject = _reflection.GeneratedProtocolMessageType('MovableObject', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _MOVABLEOBJECT_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.MovableObject.TypeAndConfidence)
    })
  ,
  'DESCRIPTOR' : _MOVABLEOBJECT,
  '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.MovableObject)
  })
_sym_db.RegisterMessage(MovableObject)
_sym_db.RegisterMessage(MovableObject.TypeAndConfidence)

StaticObject = _reflection.GeneratedProtocolMessageType('StaticObject', (_message.Message,), {

  'TypeAndConfidence' : _reflection.GeneratedProtocolMessageType('TypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _STATICOBJECT_TYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject.TypeAndConfidence)
    })
  ,

  'ConeAndAccuracy' : _reflection.GeneratedProtocolMessageType('ConeAndAccuracy', (_message.Message,), {
    'DESCRIPTOR' : _STATICOBJECT_CONEANDACCURACY,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject.ConeAndAccuracy)
    })
  ,

  'SurfaceTypeAndConfidence' : _reflection.GeneratedProtocolMessageType('SurfaceTypeAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _STATICOBJECT_SURFACETYPEANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceTypeAndConfidence)
    })
  ,

  'SurfaceMaterialAndConfidence' : _reflection.GeneratedProtocolMessageType('SurfaceMaterialAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceMaterialAndConfidence)
    })
  ,

  'SurfaceColorAndConfidence' : _reflection.GeneratedProtocolMessageType('SurfaceColorAndConfidence', (_message.Message,), {
    'DESCRIPTOR' : _STATICOBJECT_SURFACECOLORANDCONFIDENCE,
    '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject.SurfaceColorAndConfidence)
    })
  ,
  'DESCRIPTOR' : _STATICOBJECT,
  '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.StaticObject)
  })
_sym_db.RegisterMessage(StaticObject)
_sym_db.RegisterMessage(StaticObject.TypeAndConfidence)
_sym_db.RegisterMessage(StaticObject.ConeAndAccuracy)
_sym_db.RegisterMessage(StaticObject.SurfaceTypeAndConfidence)
_sym_db.RegisterMessage(StaticObject.SurfaceMaterialAndConfidence)
_sym_db.RegisterMessage(StaticObject.SurfaceColorAndConfidence)

ObjectDetectionCategory = _reflection.GeneratedProtocolMessageType('ObjectDetectionCategory', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDETECTIONCATEGORY,
  '__module__' : 'sensoris.protobuf.categories.object_detection_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.categories.objectdetection.ObjectDetectionCategory)
  })
_sym_db.RegisterMessage(ObjectDetectionCategory)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'org.sensoris.categories.objectdetectionB\037SensorisObjectDetectionCategoryP\001Z5sensoris.org/specification/categories/objectdetection\370\001\001'
  _MOVABLEOBJECT.fields_by_name['speed_and_accuracy']._options = None
  _MOVABLEOBJECT.fields_by_name['speed_and_accuracy']._serialized_options = b'\210\265\030\001'
  _MOVABLEOBJECT.fields_by_name['acceleration_and_accuracy']._options = None
  _MOVABLEOBJECT.fields_by_name['acceleration_and_accuracy']._serialized_options = b'\210\265\030\001'
  _MOVABLEOBJECT.fields_by_name['covariance_matrix']._options = None
  _MOVABLEOBJECT.fields_by_name['covariance_matrix']._serialized_options = b'\210\265\030\001'
  _STATICOBJECT_CONEANDACCURACY.fields_by_name['lower_diameter_and_accuracy']._options = None
  _STATICOBJECT_CONEANDACCURACY.fields_by_name['lower_diameter_and_accuracy']._serialized_options = b'\210\265\030\000'
  _STATICOBJECT_CONEANDACCURACY.fields_by_name['upper_diameter_and_accuracy']._options = None
  _STATICOBJECT_CONEANDACCURACY.fields_by_name['upper_diameter_and_accuracy']._serialized_options = b'\210\265\030\000'
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE.fields_by_name['reflectivity_and_accuracy']._options = None
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE.fields_by_name['reflectivity_and_accuracy']._serialized_options = b'\210\265\030\000'
  _MOVABLEOBJECT._serialized_start=236
  _MOVABLEOBJECT._serialized_end=1383
  _MOVABLEOBJECT_TYPEANDCONFIDENCE._serialized_start=968
  _MOVABLEOBJECT_TYPEANDCONFIDENCE._serialized_end=1383
  _MOVABLEOBJECT_TYPEANDCONFIDENCE_TYPE._serialized_start=1150
  _MOVABLEOBJECT_TYPEANDCONFIDENCE_TYPE._serialized_end=1383
  _STATICOBJECT._serialized_start=1386
  _STATICOBJECT._serialized_end=4419
  _STATICOBJECT_TYPEANDCONFIDENCE._serialized_start=2353
  _STATICOBJECT_TYPEANDCONFIDENCE._serialized_end=2971
  _STATICOBJECT_TYPEANDCONFIDENCE_TYPE._serialized_start=2534
  _STATICOBJECT_TYPEANDCONFIDENCE_TYPE._serialized_end=2971
  _STATICOBJECT_CONEANDACCURACY._serialized_start=2974
  _STATICOBJECT_CONEANDACCURACY._serialized_end=3406
  _STATICOBJECT_SURFACETYPEANDCONFIDENCE._serialized_start=3409
  _STATICOBJECT_SURFACETYPEANDCONFIDENCE._serialized_end=3648
  _STATICOBJECT_SURFACETYPEANDCONFIDENCE_TYPE._serialized_start=3603
  _STATICOBJECT_SURFACETYPEANDCONFIDENCE_TYPE._serialized_end=3648
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE._serialized_start=3651
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE._serialized_end=4056
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE_TYPE._serialized_start=3947
  _STATICOBJECT_SURFACEMATERIALANDCONFIDENCE_TYPE._serialized_end=4056
  _STATICOBJECT_SURFACECOLORANDCONFIDENCE._serialized_start=4059
  _STATICOBJECT_SURFACECOLORANDCONFIDENCE._serialized_end=4407
  _STATICOBJECT_SURFACECOLORANDCONFIDENCE_TYPE._serialized_start=4256
  _STATICOBJECT_SURFACECOLORANDCONFIDENCE_TYPE._serialized_end=4407
  _OBJECTDETECTIONCATEGORY._serialized_start=4422
  _OBJECTDETECTIONCATEGORY._serialized_end=4681
# @@protoc_insertion_point(module_scope)
