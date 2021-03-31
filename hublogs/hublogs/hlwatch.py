"""Watches the clipboard for hub ids and then transfers the hublogs for that hub."""

import os
import sys

import boto3
import pyperclip

# from pyperclip import waitForNewPaste

from hublogs.wait import waitForFiles
from hublogs.hlogs import testValidHubId


def copyS3Data(bucket, fn):
    try:
        ofn = os.path.basename(fn)
        s3 = boto3.client("s3")
        print(f"downloading {fn} to {ofn}")
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


def getHubLogs(hubid):
    try:
        bucket = "hub-debug-log"
        fns = waitForFiles(bucket, hubid)
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


def watchClipboard():
    try:
        while True:
            txt = pyperclip.waitForNewPaste(timeout=600)
            if testValidHubId(txt):
                getHubLogs(txt)
                break
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        sys.exit(1)
