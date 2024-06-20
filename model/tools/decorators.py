# from tools.log import Logger
# from logging import Logger


# def exception_handling(function):
#     def inner(*args, **kwargs):
#         try:
#             output = function(*args, **kwargs)
#             if not "find" in function.__name__ :
#                 Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output[1]}")
#             else:
#                 Logger.info(f"{function.__qualname__}{args[1:]}")
#             return output
#         except Exception as e:
#             e.with_traceback()
#             Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : {e}")
#             return False, str(e)

#     return inner


def exception_handling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            return False, None
    return wrapper