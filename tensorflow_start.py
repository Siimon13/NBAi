import tensorflow as tf

filename = "scrapped_withRuns.csv"
filename_queue = tf.train.string_input_producer([filename])

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
            return i + 1
def prediction_model(n=1, log_progress=False):
    with tf.Session() as session:
        hp = tf.placeholder(tf.float32, [n], name=’home_pts’)
        vp = tf.placeholder(tf.float32, [n], name=’visitor_pts’)
       	hp = tf.string_to_number(hp)
       	vp = tf.string_to_number(vp)
        hp_t= tf.Variable([1.0], trainable=True) # training variable: slope
        vp_t = tf.Variable([1.0], trainable=True) # training variable: intercept
        y = tf.add(tf.mul(m, x), b) # fit y_i = m * x_i + b

        # actual values (for training)
        y_act = tf.placeholder(tf.float32, [n], name=’y_’)

        # minimize sum of squared error between trained and actual.
        error = tf.sqrt((y – y_act) * (y – y_act))
        # train_step = tf.train.GradientDescentOptimizer(0.01).minimize(error)
        train_step = tf.train.AdamOptimizer(0.05).minimize(error)

        # generate input and output data with a little random noise.
        x_in, y_star = make_data(n)

        init = tf.initialize_all_variables()
        session.run(init)
        feed_dict = {x: x_in, y_act: y_star}
        for i in range(30 * n):
            y_i, m_i, b_i, _ = session.run([y, m, b, train_step], feed_dict)
            err = np.linalg.norm(y_i – y_star, 2)
            if log_progress:
                print(“%3d | %.4f %.4f %.4e” % (i, m_i, b_i, err))

        print(“Done! m = %f, b = %f, err = %e, iterations = %d”
              % (m_i, b_i, err, i))
        print(”      x: %s” % x_in)
        print(“Trained: %s” % y_i)
        print(” Actual: %s” % y_star)

def main():
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
	        example, label = sess.run([features, col25])
	        print("Example:", example)
	        print("Label:", label)
	            
	    coord.request_stop()
	    coord.join(threads)
	    print("done loading")
main()
