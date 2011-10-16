def a(*args, **kwargs):
	for i in args:
		print i

	for key,val in kwargs.iteritems():
		print "{0} => {1}".format(key, val)

a('Should be for args', force=True, dean='person')
