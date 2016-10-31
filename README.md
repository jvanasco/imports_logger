Import Logger
=============

This is a terrible, quickly slapped together, package.

## what this does

This package is used to override calls to `import`, wrapping every import in a call to psutil for measuring memory.  

The outputs are written to a versioned file as `csv` compatible text files (one for successful imports, another for failures)

The outputs can then be processed and analyzed to determine where the biggest imports are, and what causes them.

This is rough and can be customized.  This should not be used on production code.  It is a quick debugging tool.

## requirements

* `psutil`

## usage

	# at the top of your script
    import import_logger
    import_logger.setup_logger()

	# your code here    
