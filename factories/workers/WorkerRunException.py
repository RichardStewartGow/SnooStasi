class WorkerRunException(Exception):
    def __init__(self, message, errors, worker):
        super(WorkerRunException, self).__init__(message)

        self.errors = errors
        self.worker = worker