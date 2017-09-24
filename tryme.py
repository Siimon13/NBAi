import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

tf.global_variables_initializer()
filename = "scrapped_withRuns.csv"

# X_train = np.array ([[1.,-1.,2.], [2.,0.,0.], [0.,1.,-1.]])
# X_scaled = preprocessing.scale(X_train)
# print(X_scaled)

def get_run_value():
    df_nba = pd.read_csv(filename)
    return df_nba['Run'] # returns 0 or 1 based on DATA -- if there is a run going on or not




def make_data(n):
    np.random.seed(42) # To ensure same data for multiple runs
    x = 2.0 * np.array(range(n))
    y = 1.0 + 3.0 * (np.array(range(n)) + 0.1 * (np.random.rand(n) - 0.5))
    return x, y

def fit_line(n=1, log_progress=False):
    with tf.Session() as session:
        df_nba = pd.read_csv(filename)
        x = tf.placeholder(tf.float32, [n], name='x')
        y = tf.placeholder(tf.float32, [n], name='y')
        m = tf.Variable([1.0], trainable=True) # training variable: slope
        b = tf.Variable([1.0], trainable=True) # training variable: intercept
        y = tf.add(tf.multiply(m, x), b) # fit y_i = m * x_i + b

        # actual values (for training)
        y_act = tf.placeholder(tf.float32, [n], name='y_')

        # minimize sum of squared error between trained and actual.
        error = tf.sqrt((y - y_act) * (y - y_act))
        # train_step = tf.train.GradientDescentOptimizer(0.01).minimize(error)
        train_step = tf.train.AdamOptimizer(0.05).minimize(error)

        # generate input and output data with a little random noise.
        #x_in, y_star = make_data(n)
        x_in = get_run_value()
        y_star = df_nba['Play_Clock_Time']
        init = tf.initialize_all_variables()
        session.run(init)
        feed_dict = {x: x_in, y_act: y_star}
        for i in range(30 * n):
            y_i, m_i, b_i, _ = session.run([y, m, b, train_step], feed_dict)
            err = np.linalg.norm(y_i - y_star, 2)
            if log_progress:
                print("%3d | %.4f %.4f %.4e" % (i, m_i, b_i, err))
        run_val = get_run_value()

        print("Done! m = %f, b = %f, err = %e, iterations = %d"
              % (m_i, b_i, err, i))
        print("      x: %s" % x_in)
        print("Trained: %s" % y_i)
        print(" Actual: %s" % y_star)

fit_line()
print("done")



