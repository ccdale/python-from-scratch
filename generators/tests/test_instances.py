import generators.instances as GI

import boto3


def test_getInstances():
    insts = GI.getInstances()
    assert type(insts) is list


def test_getInstances_not_zero():
    insts = GI.getInstances()
    assert len(insts) > 0


def test_iterInstances():
    ec2 = boto3.client("ec2")
    inst = GI.iterInstances(ec2)
    assert type(inst) is dict
