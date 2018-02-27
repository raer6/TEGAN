def defaultFlags():
    Flags = tf.app.flags

    # The system parameter
    Flags.DEFINE_string('output_dir', None, 'The output directory of the checkpoint')
    Flags.DEFINE_string('summary_dir', None, 'The dirctory to output the summary')
    Flags.DEFINE_string('mode', 'train', 'The mode of the model train, test.')
    Flags.DEFINE_string('checkpoint', None, 'If provided, the weight will be restored from the provided checkpoint')
    Flags.DEFINE_boolean('pre_trained_model', False, 'If set True, the weight will be loaded but the global_step will still '
                     'be 0. If set False, you are going to continue the training. That is, '
                     'the global_step will be initiallized from the checkpoint, too')
    Flags.DEFINE_string('pre_trained_model_type', 'SRResnet', 'The type of pretrained model (SRGAN or SRResnet)')
    Flags.DEFINE_boolean('is_training', True, 'Training => True, Testing => False')
    Flags.DEFINE_string('task', None, 'The task: SRGAN, SRResnet')

    # The data preparing operation
    Flags.DEFINE_integer('batch_size', 16, 'Batch size of the input batch')
    Flags.DEFINE_string('input_dir_LR', None, 'The directory of the input resolution input data')
    Flags.DEFINE_string('input_dir_HR', None, 'The directory of the high resolution input data')
    Flags.DEFINE_integer('name_queue_capacity', 2048, 'The capacity of the filename queue (suggest large to ensure'
                         'enough random shuffle.')
    Flags.DEFINE_integer('image_queue_capacity', 2048, 'The capacity of the image queue (suggest large to ensure'
                     'enough random shuffle')
    Flags.DEFINE_integer('queue_thread', 10, 'The threads of the queue (More threads can speedup the training process.')

    # Generator configuration
    Flags.DEFINE_integer('num_resblock', 4, 'How many residual blocks are there in the generator')

    # The training parameters
    Flags.DEFINE_float('learning_rate', 0.0001, 'The learning rate for the network')
    Flags.DEFINE_integer('decay_step', 500000, 'The steps needed to decay the learning rate')
    Flags.DEFINE_float('decay_rate', 0.1, 'The decay rate of each decay step')
    Flags.DEFINE_boolean('stair', False, 'Whether perform staircase decay. True => decay in discrete interval.')
    Flags.DEFINE_float('beta', 0.9, 'The beta1 parameter for the Adam optimizer')
    Flags.DEFINE_integer('max_epoch', None, 'The max epoch for the training')
    Flags.DEFINE_integer('max_iter', 1000000, 'The max iteration of the training')
    Flags.DEFINE_integer('display_freq', 20, 'The diplay frequency of the training process')
    Flags.DEFINE_integer('summary_freq', 100, 'The frequency of writing summary')
    Flags.DEFINE_integer('save_freq', 10000, 'The frequency of saving images')

    
    FLAGS = Flags.FLAGS
    
    return FLAGS
