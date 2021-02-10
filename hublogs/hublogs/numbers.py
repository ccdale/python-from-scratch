"""Number routines"""

import sys


def makeSizeStr(size, human=True):
    """
    function to return the file size in either bytes
    or human readable form.
    set in a field width of 12 chars
    """
    try:
        if human:
            szstr = humanReadableSize(size)
        else:
            szstr = str(size)
        return szstr.rjust(12, " ")
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def humanReadableSize(value):
    """Convert a size in bytes into a human readable format.
    https://github.com/aws/aws-cli/blob/develop/awscli/customizations/s3/utils.py#L47
    For example::
        >>> human_readable_size(1)
        '1'
        >>> human_readable_size(10)
        '10'
        >>> human_readable_size(1024)
        '1.0 KB'
        >>> human_readable_size(1024 * 1024)
        '1.0 MB'
    :param value: The size in bytes
    :return: The size in a human readable format based on base-2 units.
    """
    try:
        HUMANIZE_SUFFIXES = ("KB", "MB", "GB", "TB", "PB", "EB")
        one_decimal_point = "%.1f"
        base = 1024
        bytes_int = float(value)

        if bytes_int < base:
            sz = str(bytes_int)
            if sz.endswith(".0"):
                sz = sz[:-2]
            return f"{sz} B"

        for i, suffix in enumerate(HUMANIZE_SUFFIXES):
            unit = base ** (i + 2)
            if round((bytes_int / unit) * base) < base:
                sz = "%.1f" % (base * bytes_int / unit)
                if sz.endswith(".0"):
                    sz = sz[:-2]
                return f"{sz} {suffix}"
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise
