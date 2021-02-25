"""Function to execise the s3 routines in s3.py"""

from hublogs.s3 import getMatchingS3Keys

cn = 0
for key in getMatchingS3Keys(
    "hub-debug-log", prefix="02d4d881-02ff-4848-acfa-b5c053a7d96d"
):
    print(key)
    cn += 1

print("end of loop")
print(cn)
