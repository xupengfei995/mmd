#!/user/bin/env python
#-*- coding:utf-8 -*-
import tensorflow as tf
t = tf.constant('Hello tensorflow!!')
sess = tf.Session()

print(sess.run(t))