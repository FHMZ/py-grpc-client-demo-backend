# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import users_pb2 as users__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in users_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUsers = channel.unary_unary(
                '/users.Users/GetUsers',
                request_serializer=users__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=users__pb2.GetUsersResponse.FromString,
                _registered_method=True)
        self.CreateUser = channel.unary_unary(
                '/users.Users/CreateUser',
                request_serializer=users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUserResponse.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/users.Users/DeleteUser',
                request_serializer=users__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=users__pb2.DeleteUserResponse.FromString,
                _registered_method=True)


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=users__pb2.GetUsersRequest.FromString,
                    response_serializer=users__pb2.GetUsersResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users__pb2.CreateUserRequest.FromString,
                    response_serializer=users__pb2.CreateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=users__pb2.DeleteUserRequest.FromString,
                    response_serializer=users__pb2.DeleteUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('users.Users', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/users.Users/GetUsers',
            users__pb2.GetUsersRequest.SerializeToString,
            users__pb2.GetUsersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/users.Users/CreateUser',
            users__pb2.CreateUserRequest.SerializeToString,
            users__pb2.CreateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/users.Users/DeleteUser',
            users__pb2.DeleteUserRequest.SerializeToString,
            users__pb2.DeleteUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
