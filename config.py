GENERATED_DIR = "generated"

MAX_ENC_VOCABULARY = 20000
MAX_DEC_VOCABULARY = MAX_ENC_VOCABULARY

NUM_LAYERS = 3
LAYER_SIZE = 256
BATCH_SIZE = 64
STEPS_PER_CHECKPIOHT = 500
LEARNING_RATE = 0.5
LEARNING_RATE_DECAY_FACTOR = 0.99
MAX_GRADIENT_NORM = 5.0

TWEETS_TRAIN_ENC_IDX_TXT = "{0}/tweets_train_enc_idx.txt".format(GENERATED_DIR)
TWEETS_TRAIN_DEC_IDX_TXT = "{0}/tweets_train_dec_idx.txt".format(GENERATED_DIR)
TWEETS_VAL_ENC_IDX_TXT = "{0}/tweets_val_enc_idx.txt".format(GENERATED_DIR)
TWEETS_VAL_DEC_IDX_TXT = "{0}/tweets_val_dec_idx.txt".format(GENERATED_DIR)
