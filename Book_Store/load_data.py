import csv
from Book_Store import session_factory
from Book_Store.models import Book

class LoadCSVData:
    
    def __init__(self) -> None:
        self.book_csv_file_path = 'Book_Store/Books.csv'
        self.file_data = None
        self.instance_list = []

    #read csv
    def _read_csv_data(self):
        with open(self.book_csv_file_path) as file:
            self.file_data = csv.DictReader(file)
            self._create_table_instances_list()

    #create table instances list
    def _create_table_instances_list(self):
        print(self.file_data)
        self.instance_list = []
        self.instance_list = [Book(**row) for row in self.file_data]

    #write data to db
    def _write_to_db(self):
        with session_factory() as session:
            session.add_all(self.instance_list)
            session.commit()

    #load data from CSV
    def load_data_from_csv(self):
        self._read_csv_data()
        self._write_to_db()
