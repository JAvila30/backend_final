
class BusinessException(Exception):
    def __init__(self, code,description,httpstatus, cause):
        self.code = code
        self.description = description
        self.httpstatus = httpstatus
        self.cause = cause
        super().__init__(f"{self.code} - {self.description}")
        
        def __str__(self):
            return f"BusinessException -> code: {self.code} - message: {self.description} - cause: {type(self.cause)}, {self.cause}"