import pandas, re, numpy as np

def load_file(filename, num_cols, delimiter='\t'):
    data = None
    try:
        data = np.load(filename + '.npy')
    except:
        splitter = re.compile(delimiter)

        def items(infile):
            for line in infile:
                for item in splitter.split(line):
                    yield item

        with open(filename, 'r') as infile:
            data = np.fromiter(items(infile), np.float64, -1)
            data = data.reshape((-1, num_cols))
            np.save(filename, data)

    return pandas.DataFrame(data)
