import tensorflow as tf

def batch_norm(x, train_phase, name='bn_layer'):
    #with tf.compat.v1.variable_scope(name) as scope:
    batch_norm = tf.compat.v1.layers.batch_normalization(
            inputs=x,
            momentum=0.9, epsilon=1e-5,
            center=True, scale=True,
            training = train_phase,
            name=name
    )
    return batch_norm
    
def cnn_blk(inputs, filters, kernel_size, phase_train, name = 'cnn_blk'):
    with tf.compat.v1.variable_scope(name) as scope:
        cnn = tf.compat.v1.layers.conv2d(inputs=inputs, filters=filters, kernel_size=kernel_size, padding="same", activation=None, use_bias=False, name="cnn")
        act = tf.nn.relu(cnn, name= "act")
        ret = batch_norm(act, phase_train)
        return ret

def dnn_blk(inputs, nodes, name = 'dnn_blk'):
    with tf.compat.v1.variable_scope(name) as scope:
        dnn = tf.compat.v1.layers.dense(inputs=inputs, units=nodes, activation=None, name="dnn")
        ret = tf.nn.relu(dnn, name= "act")
        return ret