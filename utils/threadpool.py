from concurrent.futures import ThreadPoolExecutor

class ThreadPool:

    def execute_parallel_tasks(self, func, num_records, num_threads, meta):
        executor = ThreadPoolExecutor(max_workers=num_threads)
        async_calls = [executor.submit(func, num_records=int(num_records / num_threads), meta=meta) for _ in range(num_threads)] if num_records > 100000 else [executor.submit(func, num_records=num_records, meta=meta)]
        executor.shutdown(wait=True)
        for call in async_calls:
            call.result()
