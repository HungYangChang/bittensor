# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bittensor._proto import bittensor_pb2 as bittensor_dot___proto_dot_bittensor__pb2


class TextToImageStub(object):
    """///////////////////////
    Text-to-Image //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextToImage/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageResponse.FromString,
                )


class TextToImageServicer(object):
    """///////////////////////
    Text-to-Image //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToImageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextToImage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToImage(object):
    """///////////////////////
    Text-to-Image //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextToImage/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextToMusicStub(object):
    """///////////////////////
    Text-to-Music //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextToMusic/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicResponse.FromString,
                )


class TextToMusicServicer(object):
    """///////////////////////
    Text-to-Music //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToMusicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextToMusic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToMusic(object):
    """///////////////////////
    Text-to-Music //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextToMusic/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToMusicResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextToEmbeddingStub(object):
    """///////////////////////
    Text-to-Embedding  //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextToEmbedding/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.FromString,
                )


class TextToEmbeddingServicer(object):
    """///////////////////////
    Text-to-Embedding  //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToEmbeddingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextToEmbedding', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToEmbedding(object):
    """///////////////////////
    Text-to-Embedding  //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextToEmbedding/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextToVideoStub(object):
    """///////////////////////
    Text to Video //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextToVideo/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.FromString,
                )


class TextToVideoServicer(object):
    """///////////////////////
    Text to Video //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToVideoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextToVideo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToVideo(object):
    """///////////////////////
    Text to Video //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextToVideo/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToEmbeddingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ImageToTextStub(object):
    """///////////////////////
    Image to Text //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/ImageToText/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextResponse.FromString,
                )


class ImageToTextServicer(object):
    """///////////////////////
    Image to Text //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageToTextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageToText', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageToText(object):
    """///////////////////////
    Image to Text //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageToText/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardImageToTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextToSpeechStub(object):
    """///////////////////////
    Text to Speech //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextToSpeech/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechResponse.FromString,
                )


class TextToSpeechServicer(object):
    """///////////////////////
    Text to Speech //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToSpeechServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextToSpeech', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToSpeech(object):
    """///////////////////////
    Text to Speech //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextToSpeech/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextToSpeechResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SpeechToTextStub(object):
    """///////////////////////
    Speech to Text //
    ///////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/SpeechToText/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextResponse.FromString,
                )


class SpeechToTextServicer(object):
    """///////////////////////
    Speech to Text //
    ///////////////////////

    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechToTextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SpeechToText', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeechToText(object):
    """///////////////////////
    Speech to Text //
    ///////////////////////

    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SpeechToText/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardSpeechToTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextPromptingStub(object):
    """///////////////////////
    TextPrompting //
    ///////////////////////
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/TextPrompting/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingResponse.FromString,
                )
        self.MultiForward = channel.unary_unary(
                '/TextPrompting/MultiForward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingResponse.FromString,
                )
        self.Backward = channel.unary_unary(
                '/TextPrompting/Backward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingRequest.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingResponse.FromString,
                )


class TextPromptingServicer(object):
    """///////////////////////
    TextPrompting //
    ///////////////////////
    """

    def Forward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiForward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Backward(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextPromptingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingResponse.SerializeToString,
            ),
            'MultiForward': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiForward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingResponse.SerializeToString,
            ),
            'Backward': grpc.unary_unary_rpc_method_handler(
                    servicer.Backward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingRequest.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextPrompting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextPrompting(object):
    """///////////////////////
    TextPrompting //
    ///////////////////////
    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextPrompting/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.ForwardTextPromptingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiForward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextPrompting/MultiForward',
            bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.MultiForwardTextPromptingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Backward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextPrompting/Backward',
            bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingRequest.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.BackwardTextPromptingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
