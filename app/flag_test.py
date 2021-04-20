import tensorflow as tf
import argparse

def initialize():
    flags = tf.flags
    FLAGS = flags.FLAGS
    parser = argparse.ArgumentParser()
    ## Required parameters
    flags.DEFINE_string(
        "bert_config_file", None,
        "The config json file corresponding to the pre-trained BERT model. "
        "This specifies the model architecture.")

    flags.DEFINE_string("vocab_file", None,
                        "The vocabulary file that the BERT model was trained on.")

    parser.add_argument("--no_cuda", action='store_true',
                        help="Whether not to use CUDA when available")
    parser.add_argument('--seed', type=int, default=42,
                        help="random seed for initialization")

    args = parser.parse_args([])
    return FLAGS, args
