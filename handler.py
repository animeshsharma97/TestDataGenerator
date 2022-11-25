from .generators.data_generator_factory import DataGeneratorFactory
from .constants.source_types import SourceTypes
from .utils.threadpool import ThreadPool

class GenerateDataHandler:

    def generate_data(self, data):    
        dataGeneratorClass = DataGeneratorFactory().get_data_generator_class(SourceTypes.value_of(data.get("source_type")))
        ThreadPool().execute_parallel_tasks(dataGeneratorClass().generate_data, data.get("num_records"), data.get("meta"))
        return {"message": "Data generated successfully"}, 200
