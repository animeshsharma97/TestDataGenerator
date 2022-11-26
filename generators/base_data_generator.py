from abc import ABC, abstractmethod

class BaseDataGenerator(ABC):

    @abstractmethod
    def setup(self, meta):
        pass

    @abstractmethod
    def generate_data(self, num_records, meta):
        pass

    @abstractmethod
    def cleanup(self):
        pass
    