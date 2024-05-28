from __future__ import print_function

import logging

import grpc
from grpc_client_kessel import relationships_pb2
from grpc_client_kessel import relationships_pb2_grpc

relation_api_gRPC_server = "localhost:9000"


def run():
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relationships_pb2_grpc.RelationshipsStub(channel)

        request = relationships_pb2.CreateRelationshipsRequest(
            touch=True,
            relationships=[
                relationships_pb2.Relationship(
                    object=relationships_pb2.ObjectReference(type="group", id="bob_club"),
                    relation="member",
                    subject=relationships_pb2.SubjectReference(
                        object=relationships_pb2.ObjectReference(type="user", id="bob")
                    )
                )
            ]
        )

        response = stub.CreateRelationships(request)
    print(response.SerializeToString())
    print("End of CreateRelationshipsRequest")

    print("Start of ReadRelationshipsRequest")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relationships_pb2_grpc.RelationshipsStub(channel)

        request = relationships_pb2.ReadRelationshipsRequest(filter=relationships_pb2.RelationshipFilter(
            object_type="group",
            object_id="bob_club",
            relation="member"
        ))

        response = stub.ReadRelationships(request)
    print(response)
    print("End of ReadRelationshipsRequest")


if __name__ == "__main__":
    logging.basicConfig()
    run()

