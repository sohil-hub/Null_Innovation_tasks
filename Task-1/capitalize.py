class ETL:
    def __init__(self, input_file_path, output_file_path) -> None:
        self.input_path = input_file_path
        self.output_path = output_file_path

    def writer(self, data):
        with open(self.output_path, 'w') as f:
            f.write(data)

    def transformer(self, data):
        sentences = data.split('.')[:-1]
        # print(sentences)
        sentences = [sentence.capitalize() for sentence in sentences]
        # print(sentences)
        transformed_data = '.'.join(sentences)
        # print(transformed_data)
        self.writer(transformed_data)

    def reader(self):
        with open(self.input_path, 'r') as f:
            data = f.read()
        self.transformer(data)
   
    def run(self):
        self.reader()

if __name__ == '__main__':
    etl = ETL('Task-1/Input_dir/input.txt', 'Task-1/output_dir/output.txt')
    etl.run()
