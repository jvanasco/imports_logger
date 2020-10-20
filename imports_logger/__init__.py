from __future__ import print_function

# released under the MIT license https://opensource.org/licenses/MIT
__VERSION__ = "1.0.0"


def setup_logger(log_vsize=False):
    print("===> installing imports_logger_override")
    import os
    import psutil

    # import pdb
    # import pprint
    # import logging
    import sys

    from six.moves import builtins

    # setup the memory vars
    # the call is different on other versions of psutil.
    # i've seen these 2, hopefully this will work in your case
    _this_process = psutil.Process(os.getpid())
    try:
        _this_process.memory_info()
        _f_memory = _this_process.memory_info
    except:
        _this_process.get_memory_info()
        _f_memory = _this_process.get_memory_info
    GET_MEMORY_R = lambda: _f_memory()[0]
    GET_MEMORY_V = lambda: _f_memory()[1]

    # set up the dirs
    # we'll lot go `{CWD}/imports_parser/runs/{VERSION}` in which `VERSION` is 001, 002, etc
    REPORTS_DIR_BASE = os.path.join("__imports_logged", "runs")
    if not os.path.exists(REPORTS_DIR_BASE):
        os.makedirs(REPORTS_DIR_BASE)
    dirs = [
        i
        for i in os.listdir(REPORTS_DIR_BASE)
        if os.path.isdir(os.path.join(REPORTS_DIR_BASE, i))
    ]
    max_dirs = len(dirs)
    REPORTS_DIR_RUN = os.path.join(REPORTS_DIR_BASE, "%03d" % max_dirs)
    print("===-  Logging to `%s`" % REPORTS_DIR_RUN)
    os.makedirs(REPORTS_DIR_RUN)
    writer_success = open(os.path.join(REPORTS_DIR_RUN, "imports.txt"), "a")
    writer_error = open(os.path.join(REPORTS_DIR_RUN, "errors.txt"), "a")

    # we need this still
    # PY3 -     __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module
    # PY2 -     __import__(name, globals={}, locals={}, fromlist=[], level=-1) -> module
    realimport = builtins.__import__

    # our override
    def imports_logger_override(name, *args, **kwargs):
        _mem_start = GET_MEMORY_R()
        _mem_startv = GET_MEMORY_V()
        _package_name = name
        if len(args) == 4:
            _package_name = "%s.%s" % (name, str(args[2]).replace(",", "|"))
        # use sys._getframe, because the `inspect` module leaves a circular reference that won't clean up (even with an explicit delete)
        _frame = sys._getframe(1)
        try:
            _caller_file = _frame.f_locals["__file__"]
        except:
            _caller_file = "<>"
        try:
            try:
                _imported = realimport(name, *args, **kwargs)
            except (ImportError, AttributeError) as exc:
                raise ImportError(str(exc))
            _mem_finish = GET_MEMORY_R()
            _mem_growth = _mem_finish - _mem_start
            if log_vsize:
                _mem_finishv = GET_MEMORY_V()
                _mem_growthv = _mem_finishv - _mem_startv
                _line = "import|%s,%s,%s,%s,%s,%s,%s,%s\n" % (
                    _package_name,
                    _caller_file,
                    _mem_growth,
                    _mem_start,
                    _mem_finish,
                    _mem_growthv,
                    _mem_startv,
                    _mem_finishv,
                )
            else:
                _line = "import|%s,%s,%s,%s,%s\n" % (
                    _package_name,
                    _caller_file,
                    _mem_growth,
                    _mem_start,
                    _mem_finish,
                )
            writer_success.write(_line)
            return _imported
        except Exception as e:
            _message = e.args[0]
            if isinstance(e, ImportError) and _message.startswith("No module named"):
                # print("ImportError: %s | via <%s> in <%s>" % (e, _package_name, _caller_file))
                _mem_finish = GET_MEMORY_R()
                _mem_growth = _mem_finish - _mem_start
                if log_vsize:
                    _mem_finishv = GET_MEMORY_V()
                    _mem_growthv = _mem_finishv - _mem_startv
                    _line = "import|%s,%s,%s,%s,%s,%s,%s,%s\n" % (
                        _package_name,
                        _caller_file,
                        _mem_growth,
                        _mem_start,
                        _mem_finish,
                        _mem_growthv,
                        _mem_startv,
                        _mem_finishv,
                    )
                else:
                    _line = "import|%s,%s,%s,%s,%s\n" % (
                        _package_name,
                        _caller_file,
                        _mem_growth,
                        _mem_start,
                        _mem_finish,
                    )
                writer_error.write(_line)
            raise
        finally:
            del _caller_file
            del _frame

    # install the override
    builtins.__import__ = imports_logger_override
    print("<=== imports_logger_override installed")
