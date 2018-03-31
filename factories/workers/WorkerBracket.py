from .WorkerRunException import WorkerRunException

class WorkerBracket:
    def __init__(self, workers):
        self.workers = workers

    def run_workers(self):
        for worker in self.workers:
            try:
                worker.run()
            except Exception as error:
                raise WorkerRunException(
                    'Worker ' + worker.getName() + ' has failed to run ', worker.getIssue(), worker
                )
