from tstarbot.data.queue.command_queue_base import CommandQueueBase

class BuildCommandQueue(CommandQueueBase):
    def __init__(self):
        super(CommandQueueBase, self).__init__()

    def update(self, timestep):
        pass