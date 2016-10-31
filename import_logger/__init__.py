# released under the MIT license https://opensource.org/licenses/MIT

def setup_logger():
    print("===> installing import_logger_orverride")
    import os
    import psutil
    import pdb
    import pprint
    import __builtin__
    import logging
    import sys

    # setup the memory vars
    # the call is different on other versions of psutil.
    # i've seen these 2, hopefully this will work in your case
    _this_process = psutil.Process(os.getpid())
    try:
        _this_process.memory_info()
        _f_get_memory_info = _this_process.memory_info
    except:
        _this_process.get_memory_info()
        _f_get_memory_info = _this_process.get_memory_info
    GET_MEMORY = lambda: _f_get_memory_info()[0]

    # set up the dirs
    # we'll lot go `{CWD}/imports_parser/runs/{VERSION}` in which `VERSION` is 001, 002, etc
    REPORTS_DIR_BASE = os.path.join("__imports_parser", "runs")
    if not os.path.exists(REPORTS_DIR_BASE):
        os.makedirs(REPORTS_DIR_BASE)
    dirs = [i for i in os.listdir(REPORTS_DIR_BASE)
            if os.path.isdir(os.path.join(REPORTS_DIR_BASE, i))
            ]
    max_dirs = len(dirs)
    REPORTS_DIR_RUN = os.path.join(REPORTS_DIR_BASE, "%03d" % max_dirs)
    print("===-  Logging to %s" % REPORTS_DIR_RUN)
    os.makedirs(REPORTS_DIR_RUN)
    writer_success = open(os.path.join(REPORTS_DIR_RUN, 'imports.txt'), 'a')
    writer_error = open(os.path.join(REPORTS_DIR_RUN, 'errors.txt'), 'a')

    # we need this still
    realimport = __builtin__.__import__

    # our override
    def import_logger_orverride(name, *args, **kwargs):
        _mem_start = GET_MEMORY()
        _package_name = name
        if len(args) == 4:
            _package_name = "%s.%s" % (name,
                                       str(args[2]).replace(',', '|'))
        # use sys._getframe, because the `inspect` module leaves a circular reference that won't clean up (even with an explicit delete)
        _frame = sys._getframe(1)
        try:
            _caller_file = _frame.f_locals['__file__']
        except:
            _caller_file = "<>"
        try:
            _imported = realimport(name, *args, **kwargs)
            _mem_finish = GET_MEMORY()
            _mem_growth = _mem_finish - _mem_start
            _line = "import|%s,%s,%s,%s,%s\n" % (_package_name, _caller_file, _mem_growth, _mem_start, _mem_finish)
            writer_success.write(_line)
            return _imported
        except Exception as e:
            if isinstance(e, ImportError) and e.message.startswith("No module named"):
                _mem_finish = GET_MEMORY()
                _mem_growth = _mem_finish - _mem_start
                _line = "import|%s,%s,%s,%s,%s\n" % (_package_name, _caller_file, _mem_growth, _mem_start, _mem_finish)
                writer_error.write(_line)
            raise
        finally:
            del _caller_file
            del _frame

    # install the override
    __builtin__.__import__ = import_logger_orverride
    print("<=== import_logger_orverride installed")
