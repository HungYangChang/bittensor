# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bittensor/_proto/bittensor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bittensor/_proto/bittensor.proto\"[\n\x19\x46orwardTextToImageRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x86\x01\n\x1a\x46orwardTextToImageResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\x0c\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"_\n\x1d\x46orwardTextToEmbeddingRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x03(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x97\x01\n\x1e\x46orwardTextToEmbeddingResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x1a\n\tembedding\x18\x03 \x01(\x0b\x32\x07.Tensor\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"\\\n\x19\x46orwardImageToTextRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x85\x01\n\x1a\x46orwardImageToTextResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"\\\n\x1a\x46orwardTextToSpeechRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x88\x01\n\x1b\x46orwardTextToSpeechResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0e\n\x06speech\x18\x03 \x01(\x0c\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"^\n\x1a\x46orwardSpeechToTextRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0e\n\x06speech\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x86\x01\n\x1b\x46orwardSpeechToTextResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"a\n\x1b\x46orwardTextPromptingRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x10\n\x08messages\x18\x03 \x03(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x8b\x01\n\x1c\x46orwardTextPromptingResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x10\n\x08response\x18\x03 \x01(\t\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"f\n MultiForwardTextPromptingRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x10\n\x08messages\x18\x03 \x03(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x02\"\x99\x01\n!MultiForwardTextPromptingResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x19\n\x11multi_completions\x18\x03 \x03(\t\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"\x85\x01\n\x1c\x42\x61\x63kwardTextPromptingRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x0f\n\x07rewards\x18\x03 \x03(\x02\x12\x10\n\x08messages\x18\x04 \x03(\t\x12\x10\n\x08response\x18\x05 \x01(\t\x12\x0f\n\x07timeout\x18\x06 \x01(\x02\"z\n\x1d\x42\x61\x63kwardTextPromptingResponse\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06hotkey\x18\x02 \x01(\t\x12\x16\n\x0ereturn_message\x18\x04 \x01(\t\x12 \n\x0breturn_code\x18\x05 \x01(\x0e\x32\x0b.ReturnCode\"\xac\x01\n\x06Tensor\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0e\n\x06\x62uffer\x18\x02 \x01(\x0c\x12\r\n\x05shape\x18\x03 \x03(\x03\x12\x1f\n\nserializer\x18\x04 \x01(\x0e\x32\x0b.Serializer\x12 \n\x0btensor_type\x18\x05 \x01(\x0e\x32\x0b.TensorType\x12\x18\n\x05\x64type\x18\x06 \x01(\x0e\x32\t.DataType\x12\x15\n\rrequires_grad\x18\x08 \x01(\x08*\xda\x04\n\nReturnCode\x12\x0c\n\x08NoReturn\x10\x00\x12\x0b\n\x07Success\x10\x01\x12\x0b\n\x07Timeout\x10\x02\x12\x0b\n\x07\x42\x61\x63koff\x10\x03\x12\x0f\n\x0bUnavailable\x10\x04\x12\x12\n\x0eNotImplemented\x10\x05\x12\x10\n\x0c\x45mptyRequest\x10\x06\x12\x11\n\rEmptyResponse\x10\x07\x12\x13\n\x0fInvalidResponse\x10\x08\x12\x12\n\x0eInvalidRequest\x10\t\x12\x19\n\x15RequestShapeException\x10\n\x12\x1a\n\x16ResponseShapeException\x10\x0b\x12!\n\x1dRequestSerializationException\x10\x0c\x12\"\n\x1eResponseSerializationException\x10\r\x12#\n\x1fRequestDeserializationException\x10\x0e\x12$\n ResponseDeserializationException\x10\x0f\x12\x15\n\x11NotServingNucleus\x10\x10\x12\x12\n\x0eNucleusTimeout\x10\x11\x12\x0f\n\x0bNucleusFull\x10\x12\x12\x1e\n\x1aRequestIncompatibleVersion\x10\x13\x12\x1f\n\x1bResponseIncompatibleVersion\x10\x14\x12\x11\n\rSenderUnknown\x10\x15\x12\x14\n\x10UnknownException\x10\x16\x12\x13\n\x0fUnauthenticated\x10\x17\x12\x0f\n\x0b\x42\x61\x64\x45ndpoint\x10\x18\x12\x0f\n\x0b\x42lacklisted\x10\x19*&\n\nSerializer\x12\x0b\n\x07MSGPACK\x10\x00\x12\x0b\n\x07\x43MPPACK\x10\x01*2\n\nTensorType\x12\t\n\x05TORCH\x10\x00\x12\x0e\n\nTENSORFLOW\x10\x01\x12\t\n\x05NUMPY\x10\x02*h\n\x08\x44\x61taType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x46LOAT32\x10\x01\x12\x0b\n\x07\x46LOAT64\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\x08\n\x04UTF8\x10\x05\x12\x0b\n\x07\x46LOAT16\x10\x06\x12\x08\n\x04\x42OOL\x10\x07\x32S\n\x0bTextToImage\x12\x44\n\x07\x46orward\x12\x1a.ForwardTextToImageRequest\x1a\x1b.ForwardTextToImageResponse\"\x00\x32_\n\x0fTextToEmbedding\x12L\n\x07\x46orward\x12\x1e.ForwardTextToEmbeddingRequest\x1a\x1f.ForwardTextToEmbeddingResponse\"\x00\x32S\n\x0bImageToText\x12\x44\n\x07\x46orward\x12\x1a.ForwardImageToTextRequest\x1a\x1b.ForwardImageToTextResponse\"\x00\x32V\n\x0cTextToSpeech\x12\x46\n\x07\x46orward\x12\x1b.ForwardTextToSpeechRequest\x1a\x1c.ForwardTextToSpeechResponse\"\x00\x32V\n\x0cSpeechToText\x12\x46\n\x07\x46orward\x12\x1b.ForwardSpeechToTextRequest\x1a\x1c.ForwardSpeechToTextResponse\"\x00\x32\xff\x01\n\rTextPrompting\x12H\n\x07\x46orward\x12\x1c.ForwardTextPromptingRequest\x1a\x1d.ForwardTextPromptingResponse\"\x00\x12W\n\x0cMultiForward\x12!.MultiForwardTextPromptingRequest\x1a\".MultiForwardTextPromptingResponse\"\x00\x12K\n\x08\x42\x61\x63kward\x12\x1d.BackwardTextPromptingRequest\x1a\x1e.BackwardTextPromptingResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bittensor._proto.bittensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RETURNCODE._serialized_start=2150
  _RETURNCODE._serialized_end=2752
  _SERIALIZER._serialized_start=2754
  _SERIALIZER._serialized_end=2792
  _TENSORTYPE._serialized_start=2794
  _TENSORTYPE._serialized_end=2844
  _DATATYPE._serialized_start=2846
  _DATATYPE._serialized_end=2950
  _FORWARDTEXTTOIMAGEREQUEST._serialized_start=36
  _FORWARDTEXTTOIMAGEREQUEST._serialized_end=127
  _FORWARDTEXTTOIMAGERESPONSE._serialized_start=130
  _FORWARDTEXTTOIMAGERESPONSE._serialized_end=264
  _FORWARDTEXTTOEMBEDDINGREQUEST._serialized_start=266
  _FORWARDTEXTTOEMBEDDINGREQUEST._serialized_end=361
  _FORWARDTEXTTOEMBEDDINGRESPONSE._serialized_start=364
  _FORWARDTEXTTOEMBEDDINGRESPONSE._serialized_end=515
  _FORWARDIMAGETOTEXTREQUEST._serialized_start=517
  _FORWARDIMAGETOTEXTREQUEST._serialized_end=609
  _FORWARDIMAGETOTEXTRESPONSE._serialized_start=612
  _FORWARDIMAGETOTEXTRESPONSE._serialized_end=745
  _FORWARDTEXTTOSPEECHREQUEST._serialized_start=747
  _FORWARDTEXTTOSPEECHREQUEST._serialized_end=839
  _FORWARDTEXTTOSPEECHRESPONSE._serialized_start=842
  _FORWARDTEXTTOSPEECHRESPONSE._serialized_end=978
  _FORWARDSPEECHTOTEXTREQUEST._serialized_start=980
  _FORWARDSPEECHTOTEXTREQUEST._serialized_end=1074
  _FORWARDSPEECHTOTEXTRESPONSE._serialized_start=1077
  _FORWARDSPEECHTOTEXTRESPONSE._serialized_end=1211
  _FORWARDTEXTPROMPTINGREQUEST._serialized_start=1213
  _FORWARDTEXTPROMPTINGREQUEST._serialized_end=1310
  _FORWARDTEXTPROMPTINGRESPONSE._serialized_start=1313
  _FORWARDTEXTPROMPTINGRESPONSE._serialized_end=1452
  _MULTIFORWARDTEXTPROMPTINGREQUEST._serialized_start=1454
  _MULTIFORWARDTEXTPROMPTINGREQUEST._serialized_end=1556
  _MULTIFORWARDTEXTPROMPTINGRESPONSE._serialized_start=1559
  _MULTIFORWARDTEXTPROMPTINGRESPONSE._serialized_end=1712
  _BACKWARDTEXTPROMPTINGREQUEST._serialized_start=1715
  _BACKWARDTEXTPROMPTINGREQUEST._serialized_end=1848
  _BACKWARDTEXTPROMPTINGRESPONSE._serialized_start=1850
  _BACKWARDTEXTPROMPTINGRESPONSE._serialized_end=1972
  _TENSOR._serialized_start=1975
  _TENSOR._serialized_end=2147
  _TEXTTOIMAGE._serialized_start=2952
  _TEXTTOIMAGE._serialized_end=3035
  _TEXTTOEMBEDDING._serialized_start=3037
  _TEXTTOEMBEDDING._serialized_end=3132
  _IMAGETOTEXT._serialized_start=3134
  _IMAGETOTEXT._serialized_end=3217
  _TEXTTOSPEECH._serialized_start=3219
  _TEXTTOSPEECH._serialized_end=3305
  _SPEECHTOTEXT._serialized_start=3307
  _SPEECHTOTEXT._serialized_end=3393
  _TEXTPROMPTING._serialized_start=3396
  _TEXTPROMPTING._serialized_end=3651
# @@protoc_insertion_point(module_scope)
