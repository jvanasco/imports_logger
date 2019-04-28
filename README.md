Import Logger
=============

This is a terrible, quickly slapped together, package that is... nevertheless... very useful.

## what this does

This package is used to override calls to `import`, wrapping every import in a call to psutil for measuring memory.  

The outputs are written to a versioned file as `csv` compatible text files -- one for successful imports, another for failures.

The output files are written to an `__imports_parser` directory and stored under an incremental `__imports_parser/runs` subfolder.

This is rough and can be customized.  This should NEVER NEVER NEVER be used on production code.  This is a quick debugging tool.

### DANGER DANGER DANGER

DO NOT RUN THIS IN PRODUCTION

### DANGER DANGER DANGER

SERIOUSLY, DO NOT RUN THIS IN PRODUCTION


## so why would I use this?

There are two main use-cases:

1. The outputs can be processed and analyzed (even imported to excel!) to determine where the biggest imports are, and what causes them.

2. knowing import errors is useful in two situations: refactoring your own code, and finding what libraries are conditionally importing other 3rd party tools.





## requirements

* `psutil`

## usage

try running the demo.py script

it is just...

	# at the top of your script
    import import_logger
    import_logger.setup_logger()

	# your code here    
	import re

	# this should have created a folder named `__imports_parser/runs/001`

the text in runs 001 should look like

	import|re.None,demo.py,0,12664832,12664832
