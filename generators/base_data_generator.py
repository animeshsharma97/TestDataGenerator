from abc import ABC, abstractmethod

class BaseDataGenerator(ABC):

    @abstractmethod
    def generate_data(self, num_records, meta):
        pass
    