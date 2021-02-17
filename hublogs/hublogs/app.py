"""Function to execise the s3 routines in s3.py"""

from hublogs.s3 import getMatchingS3Keys

cn = 0
for key in getMatchingS3Keys("hub-debug-logz"):
    print(key)
    cn += 1

print("end of loop")
print(cn)
