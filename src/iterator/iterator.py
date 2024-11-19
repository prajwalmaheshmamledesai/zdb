import gzip
import json
import os


class ZDBIterator:

    def __init__(self, folder):
        self.folder = folder

    # file has 2 formats metas and the data
    # metas is a json file
    def read_file(self, file):
        metas = []
        with gzip.open(file, 'rb') as f:
            # read each file
            # first line is the number of metas
            line = f.readline()
            num_of_metas = int(line)
            for i in range(num_of_metas):
                line = f.readline()
                metas.append(line)

            # read the data
            byte_size_of_data = f.readline()
            f.readline()  # skip the individual size
            for meta in metas:
                rokud_id = meta.split(',')[0]
                data = json.loads(f.readline())
                assert rokud_id == data['rokuId']

    def iterate(self):
        for file in os.listdir(self.folder):
            self.read_file(file)


if __name__ == '__main__':
    zdb = ZDBIterator('folder')
    zdb.iterate()
