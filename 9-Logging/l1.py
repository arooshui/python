
# DEBUG	Detailed info for developers
# INFO	Normal events
# WARNING	Something might be wrong
# ERROR	Something failed
# CRITICAL	Big failure, app may stop
import logging
print("User logging in")
logging.basicConfig(level = logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

