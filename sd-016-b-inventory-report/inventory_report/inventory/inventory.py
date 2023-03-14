import csv
import json
import xml.etree.ElementTree as ET

from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def check_file_type(cls, file):
        with open(file) as data:
            if file.endswith("csv"):
                return list(csv.DictReader(data))
            elif file.endswith(".json"):
                return json.load(data)
            elif file.endswith(".xml"):
                arq = ET.parse(file)
                paste = arq.getroot()
            return list({item.tag: item.text for item in row} for row in paste)

    @classmethod
    def import_data(cls, file, type):
        inventory = cls.check_file_type(file)
        if type == "simples":
            return SimpleReport.generate(inventory)
        elif type == "completo":
            return CompleteReport.generate(inventory)
