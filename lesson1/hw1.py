from abc import ABCMeta, abstractmethod
import csv
import json
import os
import pickle


class Meta(ABCMeta):
    number_created_class = 0

    def __new__(cls, namespace, bases, param):
        if bases:
            cls.number_created_class += 1
        print(namespace, " - ", cls.number_created_class)
        return ABCMeta.__new__(cls, namespace, bases, param)

    def __call__(cls, *arg, **kwarg):
        return ABCMeta.__call__(cls, *arg, **kwarg)


class SerializationInterface(metaclass=Meta):
    @ abstractmethod
    def save():
        pass

    @ abstractmethod
    def load():
        pass


def main():
    print("Hello, user!")
    while True:
        print("number created class", " - ", Meta.number_created_class)
        my_format = input("I need to save new data in format: ")
        if my_format == "json":
            class SerializationJSON(SerializationInterface):
                data = ""
                destination = f"{os.getcwd()}/my.json"

                def save(self, data):
                    self.data = data
                    with open(self.destination, "w") as fh:
                        json.dump(self.data, fh)

                def load(self):
                    with open(self.destination, "r") as fh:
                        self.data = json.load(fh)
                    return self.data
            MyJSON = SerializationJSON()
            MyJSON.save("Save new data in format JSON")
            print(MyJSON.load())
        elif my_format == "bin":
            class SerializationBIN(SerializationInterface):
                data = ""
                destination = f"{os.getcwd()}/my.bin"

                def save(self, data):
                    self.data = data
                    with open(self.destination, "wb") as fh:
                        pickle.dump(self.data, fh)

                def load(self):
                    with open(self.destination, "rb") as fh:
                        self.data = pickle.load(fh)
                    return self.data
            MyPickle = SerializationBIN()
            MyPickle.save("Save new data in format Pickle")
            print(MyPickle.load())
        elif my_format == "csv":
            class SerializationCSV(SerializationInterface):
                data = ""
                destination = f"{os.getcwd()}/my.csv"

                def save(self, data):
                    self.data = data
                    with open(self.destination, "w") as fh:
                        csv_writer = csv.writer(fh)
                        csv_writer.writerow(self.data)

                def load(self):
                    with open(self.destination, "r") as fh:
                        csv_reader = csv.reader(fh)
                        for row in csv_reader:
                            self.data = row
                    return self.data
            MyCSV = SerializationCSV()
            MyCSV.save("Save first data in format CSV")
            print(MyCSV.load())
        else:
            break
        print("number created class", " - ", Meta.number_created_class)


if __name__ == "__main__":
    main()
