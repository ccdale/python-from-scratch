"""Script to download hub logs from S3 when they are ready."""

import os
import re
import sys

import boto3

from hublogs.wait import waitForFiles


def testValidHubId(hubid):
    try:
        pattern = b"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        xre = re.compile(pattern)
        m = xre.match(bytes(hubid, "utf-8"))
        if m is None:
            raise Exception(f"hubid: {hubid} does not match pattern: {pattern}")
        if hubid != m[0].decode("utf-8"):
            raise Exception(f"hubid: {hubid} does not matched entity: {m[0]}")
        return True
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def testUserInput():
    try:
        if len(sys.argv) != 2:
            raise Exception("Please supply hub id.")
        if testValidHubId(sys.argv[1]):
            return sys.argv[1]
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def copyS3Data(bucket, fn):
    try:
        ofn = os.path.basename(fn)
        s3 = boto3.client("s3")
        # print(f"downloading {fn} to {ofn}")
        resp = s3.download_file(bucket, fn, ofn)
        # print(f"resp is {resp}")
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def getHubLogs():
    try:
        hubid = testUserInput()
        bucket = "hub-debug-log"
        fns = waitForFiles(bucket, hubid)
        # print(f"fns are {fns}")
        # sys.exit(0)
        if fns is None:
            raise Exception(f"No files found for hubid: {hubid}")
        for fn in fns:
            if not fn.endswith("/"):
                copyS3Data(bucket, fn)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


if __name__ == "__main__":
    getHubLogs()
