class SortedDict:
    def __init__(self, keyfunc, **kwargs):
        self.dict_ = dict(sorted(kwargs.items(), key=keyfunc))

    def __repr__(self) -> str:
        return self.dict_.__repr__()

    def to_dict(self):
        return self.dict_
