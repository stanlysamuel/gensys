# Runs a GenSys-LTL specification inside Pyodide the same way `python3 spec.py <mode>` runs it natively.
import runpy
import sys
import traceback

WORKDIR = "/home/pyodide"
if WORKDIR not in sys.path:
    sys.path.insert(0, WORKDIR)


def run_spec(path, argv):
    """Execute the script at `path` as __main__ with sys.argv[1:] = argv and return its exit code."""
    sys.argv = [path] + [str(a) for a in argv]
    try:
        runpy.run_path(path, run_name="__main__")
        return 0
    except SystemExit as e:
        if e.code is None:
            return 0
        if isinstance(e.code, int):
            return e.code
        print(e.code, file=sys.stderr)
        return 1
    except BaseException:
        etype, value, tb = sys.exc_info()
        # Hide the harness and runpy frames so the traceback starts at the user's script.
        while tb is not None and tb.tb_frame.f_code.co_filename != path:
            tb = tb.tb_next
        traceback.print_exception(etype, value, tb)
        return 1
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
