from __future__ import print_function

import logging

import grpc
from relations.v0 import relation_tuples_pb2 
from relations.v0 import relation_tuples_pb2_grpc
from relations.v0 import common_pb2

from relations.v0 import check_pb2
from relations.v0 import check_pb2_grpc

from relations.v0 import lookup_pb2
from relations.v0 import lookup_pb2_grpc


relation_api_gRPC_server = "localhost:9000"
CHECK_ALLOWED = 1


def run():
    print("--Start of CreateTuples--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relation_tuples_pb2_grpc.KesselTupleServiceStub(channel)

        request = relation_tuples_pb2.CreateTuplesRequest(
            upsert=True,
            tuples=[
                common_pb2.Relationship(
                    resource=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="group"), id="bob_club"),
                    relation="member",
                    subject=common_pb2.SubjectReference(
                        subject=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="user"), id="bob")
                    )
                )
            ]
        )

        responses = stub.CreateTuples(request)
        print(responses)

    print("--End of CreateTuples--")
    print()

    print("--Start of ReadTuples--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = relation_tuples_pb2_grpc.KesselTupleServiceStub(channel)

        request = relation_tuples_pb2.ReadTuplesRequest(
            filter=relation_tuples_pb2.RelationTupleFilter(
                resource_type="group",
                resource_id="bob_club",
                relation="member"
            )
        )

        responses = stub.ReadTuples(request)
        for r in responses:
            print("Resource ID: %s" % r.tuple.resource.id)
            print("Resource Type: %s" % r.tuple.resource.type.name)
            print("Relation: %s" % r.tuple.relation)
            print("Subject Type: %s" % r.tuple.subject.subject.type.name)
            print("Subject Type: %s" % r.tuple.subject.subject.id)

    print("--End of ReadTuples--")
    print()

    print("--Start of Check request--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = check_pb2_grpc.KesselCheckServiceStub(channel)
        request = check_pb2.CheckRequest(
            resource=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="group"), id="bob_club"),
            relation="member",
            subject=common_pb2.SubjectReference(
                subject=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="user"), id="bob")
            )
        )

        response = stub.Check(request)

        if response.allowed == CHECK_ALLOWED:
            print("allowed")
        else:
            print("NOT allowed")

    print("--End of Check request--")
    print()

    print("--Start of LookupService--")
    with grpc.insecure_channel(relation_api_gRPC_server) as channel:
        stub = lookup_pb2_grpc.KesselLookupServiceStub(channel)
        request = lookup_pb2.LookupSubjectsRequest(
            resource=common_pb2.ObjectReference(type=common_pb2.ObjectType(name="group"), id="bob_club"),
            relation="member",
            subject_type=common_pb2.ObjectType(name="user"),
        )
        responses = stub.LookupSubjects(request)
        for r in responses:
            print("Subject ID: %s" % r.subject.subject.id)
            print("Resource Type: %s" % r.subject.subject.type.name)

        print("--End of LookupService--")
        print()


if __name__ == "__main__":
    logging.basicConfig()
    run()

