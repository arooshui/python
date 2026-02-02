import logging
logging.basicConfig(
    filename = 'app.log',
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a,b):
    logging.info(f"dividing a{a} by b{b}")
    try:
        res = a/b
        logging.info(f"result = {res}")
        return res
    except ZeroDivisionError:
        logging.error("Division by zero")
        return None
print(divide(10,2))
print(divide(10,0))
