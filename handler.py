from .generators.data_generator_factory import DataGeneratorFactory
from .constants.source_types import SourceTypes
from .utils.threadpool import ThreadPool

class GenerateDataHandler:

    def generate_data(self, data):    
        dataGeneratorClass = DataGeneratorFactory().get_data_generator_class(SourceTypes.value_of(data.get("source_type")))
        dataGeneratorInstance = dataGeneratorClass()
        dataGeneratorInstance.setup(data.get("meta"))
        ThreadPool().execute_parallel_tasks(dataGeneratorInstance.generate_data, data.get("num_records"), data.get("num_threads", 10), data.get("meta"))
        return {"message": "Data generated successfully"}, 200
