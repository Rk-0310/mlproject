import sys

def error_message_details(error,error_details:sys):
    # exc_info : is the execution info
    _,_,exc_tb = error_details.exc_info()
    # exc_tb : TraceBack Object of the exception
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message ="Error Occured in Python Script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message =error_message_details(error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
    


# For checking if the Exception is working.
# if __name__=='__main__':
#     try:
#         1/0
#     except Exception as e:
#         raise CustomException(e,sys)