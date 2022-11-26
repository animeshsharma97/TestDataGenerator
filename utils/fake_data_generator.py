from faker import Faker

class FakeDataGenerator:

    def __init__(self):
        self.faker = Faker(use_weighting=False)
        Faker.seed(0)
        self.data_type_faker_func_map = {
            "VARCHAR": self.faker.pystr,
            "TEXT": self.faker.pystr,
            "INT": self.faker.pyint,
            "FLOAT": self.faker.pyfloat,
            "DECIMAL": self.faker.pydecimal,
            "BIGINT": self.faker.pyint,
            "BOOLEAN": self.faker.pybool,
        }

    def generate_fake_data(self, num_records, column_type_list):
        data = [] 
        for _ in range(num_records):
            data_tuple = tuple([
                self.data_type_faker_func_map.get(column_type)()
                for column_type in column_type_list
            ])
            data.append(data_tuple)
        return data
