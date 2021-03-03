"""Async functions for downloading hublogs from S3"""

# import datetime
from datetime import datetime
import sys
import time

from hublogs.s3 import getMatchingS3Keys

# 02d4d881-02ff-4848-acfa-b5c053a7d96d/20200608T085743/4f94dc04-a107-4d9b-8cb2-0c334f6eb9b1.zip
# in the hub-debug-log bucket files are ordered as above:
#     hub guid / date + time (as a string) / hub guid.zip
def convertTimeStringToTimeStamp(timestr):
    """Converts 20200608T085743 to a unix timestamp (integer)"""
    try:
        fmt = "%Y%m%dT%H%M%S"
        dt = datetime.strptime(timestr, fmt)
        ts = dt.timestamp()
        its = int(ts)
        return its
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def getHubListing(bucket, hubid):
    """Retrieve matching files from S3"""
    try:
        fns = [key for key in getMatchingS3Keys(bucket, prefix=hubid)]
        return fns
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


# TODO we will need a timeout to cancel this wait should the files not appear
# after timeout seconds.
def waitForFiles(bucket, hubid, timeout=600):
    """Wait for files to appear in the bucket that are dated within the last hour."""
    try:
        now = int(time.time())
        now = now - 3600
        sleeptime = 10
        found = False
        cn = 0
        print()
        while not found:
            cn += 1
            tcn = (cn * sleeptime) - sleeptime
            if tcn > timeout:
                raise Exception("Timeout triggered - file did not appear.")
            print(". ", end="", flush=True)
            # print(f"Iteration {cn}")
            fns = getHubListing(bucket, hubid)
            for fn in fns:
                tmp = fn.split("/")
                datestr = tmp[1]
                if len(datestr) > 0:
                    idate = convertTimeStringToTimeStamp(datestr)
                    if idate > now:
                        found = True
                        break
            time.sleep(sleeptime)
        print()
        print(fn)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


if __name__ == "__main__":
    if len(sys.argv) == 3:
        waitForFiles(sys.argv[1], sys.argv[2])
        # its = convertTimeStringToTimeStamp(sys.argv[1])
        # print(its)
    else:
        print("Hub ID not supplied (or too many hub ids supplied)")
        sys.exit()
