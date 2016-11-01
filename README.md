Import Logger
=============

This is a terrible, quickly slapped together, package that is... nevertheless... very useful.

## what this does

This package is used to override calls to `import`, wrapping every import in a call to psutil for measuring memory.  

The outputs are written to a versioned file as `csv` compatible text files -- one for successful imports, another for failures.

This is rough and can be customized.  This should not be used on production code.  It is a quick debugging tool.

## why would I use this?

There are two main use-cases:

1. The outputs can be processed and analyzed (even imported to excel!) to determine where the biggest imports are, and what causes them.

2. knowing import errors is useful in two situations: refactoring your own code, and finding what libraries are conditionally importing other 3rd party tools.

 




## requirements

* `psutil`

## usage

	# at the top of your script
    import import_logger
    import_logger.setup_logger()

	# your code here    
