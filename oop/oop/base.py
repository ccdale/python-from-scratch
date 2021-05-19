"""base class"""


class Base:
    def output(self, xstr=""):
        try:
            print(xstr)
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise
