import json
import os.path


class email_address_service:
    """email address service"""
    def __init__(self):
        self.doc_path = self.__get_addresses_path()
        self.addresses = self.__load_addresses()

    def add_address(self, address):
        """add an email address"""
        if address not in self.addresses['addresses']:
            self.addresses['addresses'].append(address)
            self.__commit_change()

    def remove_address(self, address):
        """remove an email address"""
        new_addresses = []
        for adrs in self.addresses['addresses']:
            if adrs != address:
                new_addresses.append(adrs)

        self.addresses['addresses'] = new_addresses
        self.__commit_change()

    def get(self):
        return self.addresses['addresses']

    def __commit_change(self):
        with open(self.doc_path, 'w') as address_file:
            json.dump(self.addresses, address_file)

    def __load_addresses(self):
        with open(self.doc_path) as address_file:
            data = json.load(address_file)
            return data

    @staticmethod
    def __get_addresses_path():
        parent_dir = os.path.dirname(__file__)
        doc_path = os.path.join(parent_dir, 'addresses.json')
        return doc_path
