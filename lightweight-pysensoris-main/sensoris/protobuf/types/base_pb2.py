# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensoris/protobuf/types/base.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"sensoris/protobuf/types/base.proto\x12\x1csensoris.protobuf.types.base\x1a\x19google/protobuf/any.proto\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb9\x01\n\x07Version\x12*\n\x05major\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x05minor\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x05patch\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8a\x01\n\x0cVersionRange\x12<\n\rmin_inclusive\x18\x01 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\x12<\n\rmax_exclusive\x18\x02 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\"\xc5\x02\n\x06\x45ntity\x12\x30\n\nprimary_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0csecondary_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04type\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12?\n\x10software_version\x18\x04 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\x12?\n\x10hardware_version\x18\x05 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\x12\'\n\textension\x18\x0f \x03(\x0b\x32\x14.google.protobuf.Any\"|\n\tTimestamp\x12/\n\nposix_time\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x13posix_time_fraction\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x04\x88\xb5\x18\x00\"\x95\x01\n\x11TimestampInterval\x12@\n\x0fstart_inclusive\x18\x01 \x01(\x0b\x32\'.sensoris.protobuf.types.base.Timestamp\x12>\n\rend_exclusive\x18\x02 \x01(\x0b\x32\'.sensoris.protobuf.types.base.Timestamp\"\x1c\n\x04Path\x12\x14\n\x0c\x66ield_number\x18\x01 \x03(\x03\"\x8c\x01\n\x10\x45xtensionTypeUrl\x12>\n\x16google_type_url_suffix\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12\x30\n\x08type_url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x42\x06\n\x04type\"\xc5\x01\n\rExtensionPath\x12\x38\n\x0cto_extension\x18\x01 \x01(\x0b\x32\".sensoris.protobuf.types.base.Path\x12@\n\x08type_url\x18\x02 \x01(\x0b\x32..sensoris.protobuf.types.base.ExtensionTypeUrl\x12\x38\n\x0cin_extension\x18\x03 \x01(\x0b\x32\".sensoris.protobuf.types.base.Path\"\x9b\x01\n\x17\x41\x62soluteOrExtensionPath\x12\x36\n\x08\x61\x62solute\x18\x01 \x01(\x0b\x32\".sensoris.protobuf.types.base.PathH\x00\x12@\n\textension\x18\x02 \x01(\x0b\x32+.sensoris.protobuf.types.base.ExtensionPathH\x00\x42\x06\n\x04path\"_\n\x18\x41\x62soluteOrExtensionPaths\x12\x43\n\x04path\x18\x01 \x03(\x0b\x32\x35.sensoris.protobuf.types.base.AbsoluteOrExtensionPath\"\x96\x01\n\x1a\x45xtensionTypeUrlAndVersion\x12@\n\x08type_url\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.ExtensionTypeUrl\x12\x36\n\x07version\x18\x02 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\"\xa7\x01\n ExtensionTypeUrlAndVersionRanges\x12@\n\x08type_url\x18\x01 \x01(\x0b\x32..sensoris.protobuf.types.base.ExtensionTypeUrl\x12\x41\n\rversion_range\x18\x02 \x03(\x0b\x32*.sensoris.protobuf.types.base.VersionRange\"\x8b\x04\n\rEventEnvelope\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\ttimestamp\x18\x02 \x01(\x0b\x32\'.sensoris.protobuf.types.base.Timestamp\x12Q\n\x0e\x64\x65tection_type\x18\x03 \x01(\x0b\x32\x39.sensoris.protobuf.types.base.EventEnvelope.DetectionType\x12\'\n\textension\x18\x0f \x03(\x0b\x32\x14.google.protobuf.Any\x1a\x98\x02\n\rDetectionType\x12L\n\x04type\x18\x01 \x01(\x0e\x32>.sensoris.protobuf.types.base.EventEnvelope.DetectionType.Type\"\xb8\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x16\n\x12TRIGGERED_MANUALLY\x10\x01\x12\x1f\n\x1bTRIGGERED_AUTOMATED_REGULAR\x10\x02\x12\x1c\n\x18TRIGGERED_AUTOMATED_RARE\x10\x03\x12\x12\n\x0eREADING_SINGLE\x10\x04\x12\x12\n\x0eREADING_SIMPLE\x10\x05\x12\x12\n\x0eREADING_FUSION\x10\x06\x12\x0b\n\x07\x43OMPLEX\x10\x07\"\xed\x02\n\x14\x45ventDetectionStatus\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32\x37.sensoris.protobuf.types.base.EventDetectionStatus.Type\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\xcf\x01\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x19\n\x15\x45XPECTED_AND_DETECTED\x10\x01\x12\x1d\n\x19\x45XPECTED_AND_NOT_DETECTED\x10\x02\x12,\n(EXPECTED_AND_NOT_DETECTED_ACCESS_BLOCKED\x10\x03\x12.\n*EXPECTED_AND_NOT_DETECTED_ACCESS_AVAILABLE\x10\x04\x12\x1d\n\x19NOT_EXPECTED_AND_DETECTED\x10\x05\";\n\x10\x43\x61tegoryEnvelope\x12\'\n\textension\x18\x0f \x03(\x0b\x32\x14.google.protobuf.Any\"\x8e\x02\n\x10MessagesEnvelope\x12\x36\n\x07version\x18\x01 \x01(\x0b\x32%.sensoris.protobuf.types.base.Version\x12\x37\n\tsubmitter\x18\x02 \x03(\x0b\x32$.sensoris.protobuf.types.base.Entity\x12`\n\x1e\x65xtension_type_url_and_version\x18\x03 \x03(\x0b\x32\x38.sensoris.protobuf.types.base.ExtensionTypeUrlAndVersion\x12\'\n\textension\x18\x0f \x03(\x0b\x32\x14.google.protobuf.Any\"w\n\rInt64Interval\x12\x32\n\rmin_inclusive\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\rmax_exclusive\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xb5\x01\n\x15Int64StatisticMeasure\x12K\n\x12timestamp_interval\x18\x01 \x01(\x0b\x32/.sensoris.protobuf.types.base.TimestampInterval\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.sensoris.protobuf.types.base.StatisticMeasureType\x12\r\n\x05value\x18\x03 \x01(\x03\"\xef\x01\n Int64StatisticMeasureAndAccuracy\x12K\n\x12timestamp_interval\x18\x01 \x01(\x0b\x32/.sensoris.protobuf.types.base.TimestampInterval\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.sensoris.protobuf.types.base.StatisticMeasureType\x12\r\n\x05value\x18\x03 \x01(\x03\x12-\n\x08\x61\x63\x63uracy\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x96\x03\n\x16\x41\x62soluteInt64Histogram\x12K\n\x12timestamp_interval\x18\x01 \x01(\x0b\x32/.sensoris.protobuf.types.base.TimestampInterval\x12\x33\n\x0etotal_elements\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x45\n\x03\x62in\x18\x03 \x03(\x0b\x32\x38.sensoris.protobuf.types.base.AbsoluteInt64Histogram.Bin\x12=\n\x18upper_endpoint_inclusive\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1at\n\x03\x42in\x12=\n\x18lower_endpoint_inclusive\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12.\n\tfrequency\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xa6\x03\n\x16RelativeInt64Histogram\x12K\n\x12timestamp_interval\x18\x01 \x01(\x0b\x32/.sensoris.protobuf.types.base.TimestampInterval\x12\x33\n\x0etotal_elements\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x45\n\x03\x62in\x18\x03 \x03(\x0b\x32\x38.sensoris.protobuf.types.base.RelativeInt64Histogram.Bin\x12=\n\x18upper_endpoint_inclusive\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1a\x83\x01\n\x03\x42in\x12=\n\x18lower_endpoint_inclusive\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12=\n\x12relative_frequency\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x04\x88\xb5\x18\x01\"\xc2\x01\n\x19Int64GaussianDistribution\x12K\n\x12timestamp_interval\x18\x01 \x01(\x0b\x32/.sensoris.protobuf.types.base.TimestampInterval\x12)\n\x04mean\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08variance\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"8\n\x15Int64ValueAndExponent\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x10\n\x08\x65xponent\x18\x02 \x01(\x03\"\x80\x03\n\nInt64Value\x12\x0f\n\x05value\x18\x01 \x01(\x03H\x00\x12P\n\x11statistic_measure\x18\x02 \x01(\x0b\x32\x33.sensoris.protobuf.types.base.Int64StatisticMeasureH\x00\x12R\n\x12\x61\x62solute_histogram\x18\x03 \x01(\x0b\x32\x34.sensoris.protobuf.types.base.AbsoluteInt64HistogramH\x00\x12R\n\x12relative_histogram\x18\x04 \x01(\x0b\x32\x34.sensoris.protobuf.types.base.RelativeInt64HistogramH\x00\x12X\n\x15gaussian_distribution\x18\x05 \x01(\x0b\x32\x37.sensoris.protobuf.types.base.Int64GaussianDistributionH\x00\x42\r\n\x0bvalue_oneof\"\xc8\x04\n\x15Int64ValueAndAccuracy\x12\x62\n\x12value_and_accuracy\x18\x01 \x01(\x0b\x32\x44.sensoris.protobuf.types.base.Int64ValueAndAccuracy.ValueAndAccuracyH\x00\x12h\n\x1estatistic_measure_and_accuracy\x18\x02 \x01(\x0b\x32>.sensoris.protobuf.types.base.Int64StatisticMeasureAndAccuracyH\x00\x12R\n\x12\x61\x62solute_histogram\x18\x03 \x01(\x0b\x32\x34.sensoris.protobuf.types.base.AbsoluteInt64HistogramH\x00\x12R\n\x12relative_histogram\x18\x04 \x01(\x0b\x32\x34.sensoris.protobuf.types.base.RelativeInt64HistogramH\x00\x12X\n\x15gaussian_distribution\x18\x05 \x01(\x0b\x32\x37.sensoris.protobuf.types.base.Int64GaussianDistributionH\x00\x1aP\n\x10ValueAndAccuracy\x12\r\n\x05value\x18\x01 \x01(\x03\x12-\n\x08\x61\x63\x63uracy\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\n\x0bvalue_oneof\"!\n\nConfidence\x12\x13\n\x05value\x18\x01 \x01(\x03\x42\x04\x88\xb5\x18\x00\"~\n\x12\x43ountAndConfidence\x12*\n\x05\x63ount\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\nconfidence\x18\x02 \x01(\x0b\x32(.sensoris.protobuf.types.base.Confidence\"\x8a\x03\n\x0eInt64Matrix3x3\x12(\n\x03\x61\x31\x31\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x31\x32\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x31\x33\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x32\x31\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x32\x32\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x32\x33\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x33\x31\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x33\x32\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x03\x61\x33\x33\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\x14\n\x03Urn\x12\r\n\x05value\x18\x01 \x01(\t*z\n\x07Weekday\x12\x13\n\x0fUNKNOWN_WEEKDAY\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06\x46RIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06\x12\n\n\x06SUNDAY\x10\x07*|\n\x08TimeUnit\x12\x15\n\x11UNKNOWN_TIME_UNIT\x10\x00\x12\x0f\n\x0bMILLISECOND\x10\x01\x12\n\n\x06SECOND\x10\x02\x12\n\n\x06MINUTE\x10\x03\x12\x08\n\x04HOUR\x10\x04\x12\x07\n\x03\x44\x41Y\x10\x05\x12\x08\n\x04WEEK\x10\x06\x12\t\n\x05MONTH\x10\x07\x12\x08\n\x04YEAR\x10\x08*m\n\x14StatisticMeasureType\x12\"\n\x1eUNKNOWN_STATISTIC_MEASURE_TYPE\x10\x00\x12\x0b\n\x07MINIMUM\x10\x01\x12\x0b\n\x07MAXIMUM\x10\x02\x12\x0b\n\x07\x41VERAGE\x10\x03\x12\n\n\x06MEDIAN\x10\x04*Q\n\x0cSystemStatus\x12\x19\n\x15UNKNOWN_SYSTEM_STATUS\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03:1\n\x08\x65xponent\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x03\x42X\n\x17org.sensoris.types.baseB\x11SensorisBaseTypesP\x01Z%sensoris.org/specification/types/base\xf8\x01\x01\x62\x06proto3')

_WEEKDAY = DESCRIPTOR.enum_types_by_name['Weekday']
Weekday = enum_type_wrapper.EnumTypeWrapper(_WEEKDAY)
_TIMEUNIT = DESCRIPTOR.enum_types_by_name['TimeUnit']
TimeUnit = enum_type_wrapper.EnumTypeWrapper(_TIMEUNIT)
_STATISTICMEASURETYPE = DESCRIPTOR.enum_types_by_name['StatisticMeasureType']
StatisticMeasureType = enum_type_wrapper.EnumTypeWrapper(_STATISTICMEASURETYPE)
_SYSTEMSTATUS = DESCRIPTOR.enum_types_by_name['SystemStatus']
SystemStatus = enum_type_wrapper.EnumTypeWrapper(_SYSTEMSTATUS)
UNKNOWN_WEEKDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7
UNKNOWN_TIME_UNIT = 0
MILLISECOND = 1
SECOND = 2
MINUTE = 3
HOUR = 4
DAY = 5
WEEK = 6
MONTH = 7
YEAR = 8
UNKNOWN_STATISTIC_MEASURE_TYPE = 0
MINIMUM = 1
MAXIMUM = 2
AVERAGE = 3
MEDIAN = 4
UNKNOWN_SYSTEM_STATUS = 0
ACTIVE = 1
INACTIVE = 2
DISABLED = 3

EXPONENT_FIELD_NUMBER = 50001
exponent = DESCRIPTOR.extensions_by_name['exponent']

_VERSION = DESCRIPTOR.message_types_by_name['Version']
_VERSIONRANGE = DESCRIPTOR.message_types_by_name['VersionRange']
_ENTITY = DESCRIPTOR.message_types_by_name['Entity']
_TIMESTAMP = DESCRIPTOR.message_types_by_name['Timestamp']
_TIMESTAMPINTERVAL = DESCRIPTOR.message_types_by_name['TimestampInterval']
_PATH = DESCRIPTOR.message_types_by_name['Path']
_EXTENSIONTYPEURL = DESCRIPTOR.message_types_by_name['ExtensionTypeUrl']
_EXTENSIONPATH = DESCRIPTOR.message_types_by_name['ExtensionPath']
_ABSOLUTEOREXTENSIONPATH = DESCRIPTOR.message_types_by_name['AbsoluteOrExtensionPath']
_ABSOLUTEOREXTENSIONPATHS = DESCRIPTOR.message_types_by_name['AbsoluteOrExtensionPaths']
_EXTENSIONTYPEURLANDVERSION = DESCRIPTOR.message_types_by_name['ExtensionTypeUrlAndVersion']
_EXTENSIONTYPEURLANDVERSIONRANGES = DESCRIPTOR.message_types_by_name['ExtensionTypeUrlAndVersionRanges']
_EVENTENVELOPE = DESCRIPTOR.message_types_by_name['EventEnvelope']
_EVENTENVELOPE_DETECTIONTYPE = _EVENTENVELOPE.nested_types_by_name['DetectionType']
_EVENTDETECTIONSTATUS = DESCRIPTOR.message_types_by_name['EventDetectionStatus']
_CATEGORYENVELOPE = DESCRIPTOR.message_types_by_name['CategoryEnvelope']
_MESSAGESENVELOPE = DESCRIPTOR.message_types_by_name['MessagesEnvelope']
_INT64INTERVAL = DESCRIPTOR.message_types_by_name['Int64Interval']
_INT64STATISTICMEASURE = DESCRIPTOR.message_types_by_name['Int64StatisticMeasure']
_INT64STATISTICMEASUREANDACCURACY = DESCRIPTOR.message_types_by_name['Int64StatisticMeasureAndAccuracy']
_ABSOLUTEINT64HISTOGRAM = DESCRIPTOR.message_types_by_name['AbsoluteInt64Histogram']
_ABSOLUTEINT64HISTOGRAM_BIN = _ABSOLUTEINT64HISTOGRAM.nested_types_by_name['Bin']
_RELATIVEINT64HISTOGRAM = DESCRIPTOR.message_types_by_name['RelativeInt64Histogram']
_RELATIVEINT64HISTOGRAM_BIN = _RELATIVEINT64HISTOGRAM.nested_types_by_name['Bin']
_INT64GAUSSIANDISTRIBUTION = DESCRIPTOR.message_types_by_name['Int64GaussianDistribution']
_INT64VALUEANDEXPONENT = DESCRIPTOR.message_types_by_name['Int64ValueAndExponent']
_INT64VALUE = DESCRIPTOR.message_types_by_name['Int64Value']
_INT64VALUEANDACCURACY = DESCRIPTOR.message_types_by_name['Int64ValueAndAccuracy']
_INT64VALUEANDACCURACY_VALUEANDACCURACY = _INT64VALUEANDACCURACY.nested_types_by_name['ValueAndAccuracy']
_CONFIDENCE = DESCRIPTOR.message_types_by_name['Confidence']
_COUNTANDCONFIDENCE = DESCRIPTOR.message_types_by_name['CountAndConfidence']
_INT64MATRIX3X3 = DESCRIPTOR.message_types_by_name['Int64Matrix3x3']
_URN = DESCRIPTOR.message_types_by_name['Urn']
_EVENTENVELOPE_DETECTIONTYPE_TYPE = _EVENTENVELOPE_DETECTIONTYPE.enum_types_by_name['Type']
_EVENTDETECTIONSTATUS_TYPE = _EVENTDETECTIONSTATUS.enum_types_by_name['Type']
Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Version)
  })
_sym_db.RegisterMessage(Version)

VersionRange = _reflection.GeneratedProtocolMessageType('VersionRange', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONRANGE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.VersionRange)
  })
_sym_db.RegisterMessage(VersionRange)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Entity)
  })
_sym_db.RegisterMessage(Entity)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

TimestampInterval = _reflection.GeneratedProtocolMessageType('TimestampInterval', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPINTERVAL,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.TimestampInterval)
  })
_sym_db.RegisterMessage(TimestampInterval)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Path)
  })
_sym_db.RegisterMessage(Path)

ExtensionTypeUrl = _reflection.GeneratedProtocolMessageType('ExtensionTypeUrl', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONTYPEURL,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.ExtensionTypeUrl)
  })
_sym_db.RegisterMessage(ExtensionTypeUrl)

ExtensionPath = _reflection.GeneratedProtocolMessageType('ExtensionPath', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONPATH,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.ExtensionPath)
  })
_sym_db.RegisterMessage(ExtensionPath)

AbsoluteOrExtensionPath = _reflection.GeneratedProtocolMessageType('AbsoluteOrExtensionPath', (_message.Message,), {
  'DESCRIPTOR' : _ABSOLUTEOREXTENSIONPATH,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.AbsoluteOrExtensionPath)
  })
_sym_db.RegisterMessage(AbsoluteOrExtensionPath)

AbsoluteOrExtensionPaths = _reflection.GeneratedProtocolMessageType('AbsoluteOrExtensionPaths', (_message.Message,), {
  'DESCRIPTOR' : _ABSOLUTEOREXTENSIONPATHS,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.AbsoluteOrExtensionPaths)
  })
_sym_db.RegisterMessage(AbsoluteOrExtensionPaths)

ExtensionTypeUrlAndVersion = _reflection.GeneratedProtocolMessageType('ExtensionTypeUrlAndVersion', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONTYPEURLANDVERSION,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.ExtensionTypeUrlAndVersion)
  })
_sym_db.RegisterMessage(ExtensionTypeUrlAndVersion)

ExtensionTypeUrlAndVersionRanges = _reflection.GeneratedProtocolMessageType('ExtensionTypeUrlAndVersionRanges', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONTYPEURLANDVERSIONRANGES,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.ExtensionTypeUrlAndVersionRanges)
  })
_sym_db.RegisterMessage(ExtensionTypeUrlAndVersionRanges)

EventEnvelope = _reflection.GeneratedProtocolMessageType('EventEnvelope', (_message.Message,), {

  'DetectionType' : _reflection.GeneratedProtocolMessageType('DetectionType', (_message.Message,), {
    'DESCRIPTOR' : _EVENTENVELOPE_DETECTIONTYPE,
    '__module__' : 'sensoris.protobuf.types.base_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.EventEnvelope.DetectionType)
    })
  ,
  'DESCRIPTOR' : _EVENTENVELOPE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.EventEnvelope)
  })
_sym_db.RegisterMessage(EventEnvelope)
_sym_db.RegisterMessage(EventEnvelope.DetectionType)

EventDetectionStatus = _reflection.GeneratedProtocolMessageType('EventDetectionStatus', (_message.Message,), {
  'DESCRIPTOR' : _EVENTDETECTIONSTATUS,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.EventDetectionStatus)
  })
_sym_db.RegisterMessage(EventDetectionStatus)

CategoryEnvelope = _reflection.GeneratedProtocolMessageType('CategoryEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYENVELOPE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.CategoryEnvelope)
  })
_sym_db.RegisterMessage(CategoryEnvelope)

MessagesEnvelope = _reflection.GeneratedProtocolMessageType('MessagesEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGESENVELOPE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.MessagesEnvelope)
  })
_sym_db.RegisterMessage(MessagesEnvelope)

Int64Interval = _reflection.GeneratedProtocolMessageType('Int64Interval', (_message.Message,), {
  'DESCRIPTOR' : _INT64INTERVAL,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64Interval)
  })
_sym_db.RegisterMessage(Int64Interval)

Int64StatisticMeasure = _reflection.GeneratedProtocolMessageType('Int64StatisticMeasure', (_message.Message,), {
  'DESCRIPTOR' : _INT64STATISTICMEASURE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64StatisticMeasure)
  })
_sym_db.RegisterMessage(Int64StatisticMeasure)

Int64StatisticMeasureAndAccuracy = _reflection.GeneratedProtocolMessageType('Int64StatisticMeasureAndAccuracy', (_message.Message,), {
  'DESCRIPTOR' : _INT64STATISTICMEASUREANDACCURACY,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64StatisticMeasureAndAccuracy)
  })
_sym_db.RegisterMessage(Int64StatisticMeasureAndAccuracy)

AbsoluteInt64Histogram = _reflection.GeneratedProtocolMessageType('AbsoluteInt64Histogram', (_message.Message,), {

  'Bin' : _reflection.GeneratedProtocolMessageType('Bin', (_message.Message,), {
    'DESCRIPTOR' : _ABSOLUTEINT64HISTOGRAM_BIN,
    '__module__' : 'sensoris.protobuf.types.base_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.AbsoluteInt64Histogram.Bin)
    })
  ,
  'DESCRIPTOR' : _ABSOLUTEINT64HISTOGRAM,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.AbsoluteInt64Histogram)
  })
_sym_db.RegisterMessage(AbsoluteInt64Histogram)
_sym_db.RegisterMessage(AbsoluteInt64Histogram.Bin)

RelativeInt64Histogram = _reflection.GeneratedProtocolMessageType('RelativeInt64Histogram', (_message.Message,), {

  'Bin' : _reflection.GeneratedProtocolMessageType('Bin', (_message.Message,), {
    'DESCRIPTOR' : _RELATIVEINT64HISTOGRAM_BIN,
    '__module__' : 'sensoris.protobuf.types.base_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.RelativeInt64Histogram.Bin)
    })
  ,
  'DESCRIPTOR' : _RELATIVEINT64HISTOGRAM,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.RelativeInt64Histogram)
  })
_sym_db.RegisterMessage(RelativeInt64Histogram)
_sym_db.RegisterMessage(RelativeInt64Histogram.Bin)

Int64GaussianDistribution = _reflection.GeneratedProtocolMessageType('Int64GaussianDistribution', (_message.Message,), {
  'DESCRIPTOR' : _INT64GAUSSIANDISTRIBUTION,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64GaussianDistribution)
  })
_sym_db.RegisterMessage(Int64GaussianDistribution)

Int64ValueAndExponent = _reflection.GeneratedProtocolMessageType('Int64ValueAndExponent', (_message.Message,), {
  'DESCRIPTOR' : _INT64VALUEANDEXPONENT,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64ValueAndExponent)
  })
_sym_db.RegisterMessage(Int64ValueAndExponent)

Int64Value = _reflection.GeneratedProtocolMessageType('Int64Value', (_message.Message,), {
  'DESCRIPTOR' : _INT64VALUE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64Value)
  })
_sym_db.RegisterMessage(Int64Value)

Int64ValueAndAccuracy = _reflection.GeneratedProtocolMessageType('Int64ValueAndAccuracy', (_message.Message,), {

  'ValueAndAccuracy' : _reflection.GeneratedProtocolMessageType('ValueAndAccuracy', (_message.Message,), {
    'DESCRIPTOR' : _INT64VALUEANDACCURACY_VALUEANDACCURACY,
    '__module__' : 'sensoris.protobuf.types.base_pb2'
    # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64ValueAndAccuracy.ValueAndAccuracy)
    })
  ,
  'DESCRIPTOR' : _INT64VALUEANDACCURACY,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64ValueAndAccuracy)
  })
_sym_db.RegisterMessage(Int64ValueAndAccuracy)
_sym_db.RegisterMessage(Int64ValueAndAccuracy.ValueAndAccuracy)

Confidence = _reflection.GeneratedProtocolMessageType('Confidence', (_message.Message,), {
  'DESCRIPTOR' : _CONFIDENCE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Confidence)
  })
_sym_db.RegisterMessage(Confidence)

CountAndConfidence = _reflection.GeneratedProtocolMessageType('CountAndConfidence', (_message.Message,), {
  'DESCRIPTOR' : _COUNTANDCONFIDENCE,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.CountAndConfidence)
  })
_sym_db.RegisterMessage(CountAndConfidence)

Int64Matrix3x3 = _reflection.GeneratedProtocolMessageType('Int64Matrix3x3', (_message.Message,), {
  'DESCRIPTOR' : _INT64MATRIX3X3,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Int64Matrix3x3)
  })
_sym_db.RegisterMessage(Int64Matrix3x3)

Urn = _reflection.GeneratedProtocolMessageType('Urn', (_message.Message,), {
  'DESCRIPTOR' : _URN,
  '__module__' : 'sensoris.protobuf.types.base_pb2'
  # @@protoc_insertion_point(class_scope:sensoris.protobuf.types.base.Urn)
  })
_sym_db.RegisterMessage(Urn)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(exponent)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027org.sensoris.types.baseB\021SensorisBaseTypesP\001Z%sensoris.org/specification/types/base\370\001\001'
  _TIMESTAMP.fields_by_name['posix_time_fraction']._options = None
  _TIMESTAMP.fields_by_name['posix_time_fraction']._serialized_options = b'\210\265\030\000'
  _RELATIVEINT64HISTOGRAM_BIN.fields_by_name['relative_frequency']._options = None
  _RELATIVEINT64HISTOGRAM_BIN.fields_by_name['relative_frequency']._serialized_options = b'\210\265\030\001'
  _CONFIDENCE.fields_by_name['value']._options = None
  _CONFIDENCE.fields_by_name['value']._serialized_options = b'\210\265\030\000'
  _WEEKDAY._serialized_start=6467
  _WEEKDAY._serialized_end=6589
  _TIMEUNIT._serialized_start=6591
  _TIMEUNIT._serialized_end=6715
  _STATISTICMEASURETYPE._serialized_start=6717
  _STATISTICMEASURETYPE._serialized_end=6826
  _SYSTEMSTATUS._serialized_start=6828
  _SYSTEMSTATUS._serialized_end=6909
  _VERSION._serialized_start=162
  _VERSION._serialized_end=347
  _VERSIONRANGE._serialized_start=350
  _VERSIONRANGE._serialized_end=488
  _ENTITY._serialized_start=491
  _ENTITY._serialized_end=816
  _TIMESTAMP._serialized_start=818
  _TIMESTAMP._serialized_end=942
  _TIMESTAMPINTERVAL._serialized_start=945
  _TIMESTAMPINTERVAL._serialized_end=1094
  _PATH._serialized_start=1096
  _PATH._serialized_end=1124
  _EXTENSIONTYPEURL._serialized_start=1127
  _EXTENSIONTYPEURL._serialized_end=1267
  _EXTENSIONPATH._serialized_start=1270
  _EXTENSIONPATH._serialized_end=1467
  _ABSOLUTEOREXTENSIONPATH._serialized_start=1470
  _ABSOLUTEOREXTENSIONPATH._serialized_end=1625
  _ABSOLUTEOREXTENSIONPATHS._serialized_start=1627
  _ABSOLUTEOREXTENSIONPATHS._serialized_end=1722
  _EXTENSIONTYPEURLANDVERSION._serialized_start=1725
  _EXTENSIONTYPEURLANDVERSION._serialized_end=1875
  _EXTENSIONTYPEURLANDVERSIONRANGES._serialized_start=1878
  _EXTENSIONTYPEURLANDVERSIONRANGES._serialized_end=2045
  _EVENTENVELOPE._serialized_start=2048
  _EVENTENVELOPE._serialized_end=2571
  _EVENTENVELOPE_DETECTIONTYPE._serialized_start=2291
  _EVENTENVELOPE_DETECTIONTYPE._serialized_end=2571
  _EVENTENVELOPE_DETECTIONTYPE_TYPE._serialized_start=2387
  _EVENTENVELOPE_DETECTIONTYPE_TYPE._serialized_end=2571
  _EVENTDETECTIONSTATUS._serialized_start=2574
  _EVENTDETECTIONSTATUS._serialized_end=2939
  _EVENTDETECTIONSTATUS_TYPE._serialized_start=2732
  _EVENTDETECTIONSTATUS_TYPE._serialized_end=2939
  _CATEGORYENVELOPE._serialized_start=2941
  _CATEGORYENVELOPE._serialized_end=3000
  _MESSAGESENVELOPE._serialized_start=3003
  _MESSAGESENVELOPE._serialized_end=3273
  _INT64INTERVAL._serialized_start=3275
  _INT64INTERVAL._serialized_end=3394
  _INT64STATISTICMEASURE._serialized_start=3397
  _INT64STATISTICMEASURE._serialized_end=3578
  _INT64STATISTICMEASUREANDACCURACY._serialized_start=3581
  _INT64STATISTICMEASUREANDACCURACY._serialized_end=3820
  _ABSOLUTEINT64HISTOGRAM._serialized_start=3823
  _ABSOLUTEINT64HISTOGRAM._serialized_end=4229
  _ABSOLUTEINT64HISTOGRAM_BIN._serialized_start=4113
  _ABSOLUTEINT64HISTOGRAM_BIN._serialized_end=4229
  _RELATIVEINT64HISTOGRAM._serialized_start=4232
  _RELATIVEINT64HISTOGRAM._serialized_end=4654
  _RELATIVEINT64HISTOGRAM_BIN._serialized_start=4523
  _RELATIVEINT64HISTOGRAM_BIN._serialized_end=4654
  _INT64GAUSSIANDISTRIBUTION._serialized_start=4657
  _INT64GAUSSIANDISTRIBUTION._serialized_end=4851
  _INT64VALUEANDEXPONENT._serialized_start=4853
  _INT64VALUEANDEXPONENT._serialized_end=4909
  _INT64VALUE._serialized_start=4912
  _INT64VALUE._serialized_end=5296
  _INT64VALUEANDACCURACY._serialized_start=5299
  _INT64VALUEANDACCURACY._serialized_end=5883
  _INT64VALUEANDACCURACY_VALUEANDACCURACY._serialized_start=5788
  _INT64VALUEANDACCURACY_VALUEANDACCURACY._serialized_end=5868
  _CONFIDENCE._serialized_start=5885
  _CONFIDENCE._serialized_end=5918
  _COUNTANDCONFIDENCE._serialized_start=5920
  _COUNTANDCONFIDENCE._serialized_end=6046
  _INT64MATRIX3X3._serialized_start=6049
  _INT64MATRIX3X3._serialized_end=6443
  _URN._serialized_start=6445
  _URN._serialized_end=6465
# @@protoc_insertion_point(module_scope)