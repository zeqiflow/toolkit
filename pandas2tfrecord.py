import pandas as pd
import tensorflow as tf


class Array2serialize(object):
    def __init__(self, 
                 header,
                 dtypes):

        self._header = header
        self._dtypes = dtypes
        
    def __repr__(self):
        return 'Serilizer initializing...'
    
    def serialize_example(self, example):
        feature = {}
        for i in range(len(example)):
            col = self._header[i]
            dtype = self._dtypes[i]
            value = example[i]
            if dtype == 'int64':
                feature[col] = self._int64_feature(int(value))
            elif dtype == 'float64' or dtype == 'float32':
                feature[col] = self._float_feature(value)
            elif dtype == 'object':
                feature[col] = self._bytes_feature(value)

        example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
        return example_proto.SerializeToString()

    def _bytes_feature(self, value):
        """Returns a bytes_list from a string / byte."""
        if isinstance(value, type(tf.constant(0))):
            value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value.encode('utf-8')]))

    def _int64_feature(self, value):
        """Returns an int64_list from a bool / enum / int / uint."""
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

    def _float_feature(self, value):
        """Returns a float_list from a float / double."""
        return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))
    
    
class Compresser(object):
    def __init__():
        pass
    

class TFRWriter(object):
    '''Use for transfer processed DataFrame to TFRecord file
    '''
    def __init__(self):
        print('TFRecord writer initializing...')

    def _load_data(self, data):
        header = data.columns
        dtypes = data.dtypes
        data = iter(data.values)
        return header, dtypes, data

    def write(self, data, file_name, save_dir):
        header, dtypes, data = self._load_data(data)
        serializer = Array2serialize(header, dtypes)
        file_path = ''.join([save_dir, file_name])
        with tf.io.TFRecordWriter(path='{}.tfrecord'.format(file_path)) as w:
            while True:
                try:
                    bi_res = serializer.serialize_example(next(data))
                    w.write(bi_res)
                except StopIteration:
                    print('Writing {} done, writing to {} .'.format(file_name, save_dir))
                    break