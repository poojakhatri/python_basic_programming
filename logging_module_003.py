import logging
import math

# Create and Configure logger
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename ="Lumberjack_quadratic.log",level = logging.DEBUG, format=LOG_FORMAT, filemode ='w')
logger = logging.getLogger()

def quadratic_formuala(a,b,c):
	"""Return the solution to th equation ax^2+bx+c =0 """
	logger.info("quadratic_formuala({0}, {1}, {2})".format(a,b,c))

	# Compute the discriminant
	logger.debug("# Compute the discriminant")
	disc = b**2 -4*a*c

	# Compute the two roots
	logger.debug("# Compute the two roots")
	root1 = (-b + math.sqrt(disc))/(2*a)
	root2 = (-b - math.sqrt(disc))/(2*a)

	# Return the roots
	logger.debug("# Return the two roots")
	return (root1, root2)

roots = quadratic_formuala(1,0,-1)

print(roots)