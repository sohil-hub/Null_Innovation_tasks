import json

class ETL:
    def __init__(self, input_file_path, output_file_path) -> None:
        self.input_path = input_file_path
        self.output_path = output_file_path

    def writer(self, data):
        with open(self.output_path, 'w') as f:
            f.write(data)

    def transformer(self, data):
        words = data.split()
        unique_words = set(words)
        transformed_data = dict()
        for word in unique_words:
            transformed_data[word] = data.count(word)
        transformed_data = json.dumps(transformed_data, indent = 4) 
        self.writer(transformed_data)

    def reader(self):
        with open(self.input_path, 'r') as f:
            data = f.read()
        self.transformer(data)
   
    def run(self):
        self.reader()

if __name__ == '__main__':
    etl = ETL('Task-2/Input_dir/input.txt', 'Task-2/output_dir/output.json')
    etl.run()
