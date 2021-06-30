import sys

import boto3


def iterInstances(ec2):
    try:
        kwargs = {}
        while True:
            res = ec2.describe_instances(**kwargs)
            try:
                for res in res["Reservations"]:
                    for inst in res["Instances"]:
                        yield (inst)
            except KeyError:
                return
            try:
                kwargs["NextToken"] = res["NextToken"]
            except KeyError:
                break
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def getInstances():
    try:
        ec2 = boto3.client("ec2")
        insts = [inst for inst in iterInstances(ec2)]
        return insts
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise
