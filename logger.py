import logging

# logging.warning('Stay Calm!')
# logging.debug("This is a debug message")

# logging.info("This is an info message")

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is in the debugging Mode!")

# Formatting the Output
# By default, logs contain the log level, the logger’s name, and the log message. That’s good for a start. But you can enhance your logs with additional data by leveraging the format parameter of basicConfig().

# The format parameter accepts a string that can contain a number of predefined attributes. You can think of these attributes as placeholders that you format into the string. The default value of format looks like this:


logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
logging.warning("Hello, Warning!")
logging.basicConfig(
format="{asctime} - {levelname} - {message}",
style="{",
datefmt="%Y-%m-%d %H:%M",
)
logging.error("Something went wrong!")


# Logging into a file

# logging.basicConfig(
#     filename='app.log',
#     encoding='utf-8',
#     filemode='w',
#     format="{asctime}-{levelname}-{message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
# )
# logging.warning("Save Me!")



import logging
logging.basicConfig(
filename="app.log",
encoding="utf-8",
filemode="a",
format="{asctime} - {levelname} - {message}",
style="{",
datefmt="%Y-%m-%d %H:%M",
)
donuts = 5
guests = 0
try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.error("DonutCalculationError", exc_info=True)
