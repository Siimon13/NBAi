import tensorflow as tf

filename = "scrapped_withRuns.csv"
filename_queue = tf.train.string_input_producer([filename])

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
            return i + 1


reader = tf.TextLineReader(skip_header_lines=1)
key, value = reader.read(filename_queue)
file_length = file_len(filename)
############For Sample File test##############
#record_defaults = [["home_team"],["home_team2"],["home_team3"],["home_team4"],["home_team5"]]
#col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults)
#features = tf.stack([col1, col2, col3, col4, col5])
############END OF SAMPLE FILE TEST###########
# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [["home_team"], ["home_team_abbrv"], ["away_team"], ["away_team_abbrv"], ["period"], ["play_clock_time"], ["team_committing_action"], ["p1"], ["p2"], ["p3"],["p4"], ["p5"], ["p6"], ["p7"], ["p8"],["p9"], ["p10"],\
                   ["gen_desc"], ["shot_value"], ["rebound_designation"],["overall_desc"], ["home_pts"], ["visitor_pts"],["run?"],["in run"]]
col1, col2, col3, col4, col5, col6, col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19, col20, col21, col22, col23, col24, col25 = tf.decode_csv(value, record_defaults)

print(record_defaults)

features = tf.stack([col1, col2, col3, col4, col5, col6, col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19, col20, col21, col22, col23, col24, col25])

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
