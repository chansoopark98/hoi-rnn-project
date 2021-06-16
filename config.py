import os
import time

hyper_params = {
                "epoch": 1,
                "lr": 0.0001,
                "batch_size": 32
                }

class GetConfig:
    def __init__(self,
                 data_dir='datasets/',
                 result_dir='checkpoints/'):

        # set dir
        self.data_dir = data_dir
        self.result_dir = result_dir
        self.time = self.get_current_time()
        self.train_dir = os.path.join(data_dir + 't_class5/')
        self.valid_dir = os.path.join(data_dir + 'v_class5/')
        self.test_dir = os.path.join(data_dir + 'v_class5/')
        self.result_dir = result_dir + self.time
        self.tensorboard_dir = result_dir + self.time + '/tensorboard'

        # save file dir
        self.save_weight = os.path.join(self.result_dir + '/save_weights/')
        self.save_backup = os.path.join(self.result_dir + '/back_weights/')
        self.test_result = os.path.join(self.result_dir + '/test/')

        # create dir
        self.create_directory()

        # train params
        self.args = hyper_params



    def create_directory(self):
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.result_dir, exist_ok=True)
        os.makedirs(self.result_dir + self.time, exist_ok=True)

        os.makedirs(self.save_weight, exist_ok=True)
        os.makedirs(self.save_backup, exist_ok=True)
        os.makedirs(self.test_result, exist_ok=True)

    def get_current_time(self):
        return str(time.strftime('%m%d', time.localtime(time.time())))

    def get_dir_path(self):
        return {
            "train": self.train_dir,
            "validation": self.valid_dir,
            "test": self.test_dir,
            "result": self.result_dir,
            "tensorboard": self.tensorboard_dir
        }

    def get_hyperParams(self):
        return self.args






