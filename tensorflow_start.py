import tensorflow as tf

filename = "SalesJan2009.csv"
filename_queue = tf.train.string_input_producer([filename])

def file_len(fname):
  with open(fname) as f:
      for i, l in enumerate(f):
          pass
  return i + 1


reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
file_length = file_len(filename)

record_defaults = [[1],[1],[1],[1],[1]]
col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults)
features = tf.stack([col1, col2, col3, col4, col5])
# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
#record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1],[1], [1], [1], [1], [1],[1], [1],\
#                   [1], [1], [1],[1], [1], [1]]
#col1, col2, col3, col4, col5, col6, col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19, col20, col21, col22, col23 = \
#      tf.decode_csv(value, record_defaults)
#features = tf.stack([col1, col2, col3, col4, col5, col6, col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19, \
#                     col20, col21, col22, col23])

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(file_length):
    # Retrieve a single instance:
    example, label = sess.run([features, col5])
    print("Example:", example)
  print("Label:", label)

  coord.request_stop()
  coord.join(threads)
  print("done loading")

