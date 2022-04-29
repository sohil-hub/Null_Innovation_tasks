class ETL:
    def __init__(self, input_file_path, output_file_path) -> None:
        self.input_path = input_file_path
        self.output_path = output_file_path

    def writer(self, data):
        with open(self.output_path, 'w') as f:
            f.write(data)

    def transformer(self, data):
        self.writer(data.upper())

    def reader(self):
        with open(self.input_path, 'r') as f:
            data = f.read()
        self.transformer(data)
   
    def run(self):
        self.reader()

if __name__ == '__main__':
    etl = ETL('Task-1/Input_dir/input.txt', 'Task-1/output_dir/output_upper.txt')
    etl.run()
