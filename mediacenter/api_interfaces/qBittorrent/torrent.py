class Torrent:
    def __init__(self, data):
        self.added_on = None
        self.amount_left = None
        self.auto_tmm = None
        self.category = None
        self.completed = None
        self.completion_on = None
        self.dl_limit = None
        self.dlspeed = None
        self.downloaded = None
        self.downloaded_session = None
        self.eta = None
        self.f_l_piece_prio = None
        self.force_start = None
        self.hash = None
        self.last_activity = None
        self.magnet_uri = None
        self.max_ratio = None
        self.max_seeding_time = None
        self.name = None
        self.num_complete = None
        self.num_incomplete = None
        self.num_leechs = None
        self.num_seeds = None
        self.priority = None
        self.progress = None
        self.ratio = None
        self.ratio_limit = None
        self.save_path = None
        self.seeding_time_limit = None
        self.seen_complete = None
        self.seq_dl = None
        self.size = None
        self.state = None
        self.super_seeding = None
        self.tags = None
        self.time_active = None
        self.total_size = None
        self.tracker = None
        self.up_limit = None
        self.uploaded = None
        self.uploaded_session = None
        self.upspeed = None

        self.__load(data)

    def __load(self, data):
        """
        Achieves the same thing as setting them one by one like before
        :param data:
        :return:
        """
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self):
        return f"{self.name}"
