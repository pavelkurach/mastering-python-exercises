class SortedDict:
    def __init__(self, keyfunc, **kwargs):
        self.dict_ = dict(sorted(kwargs.items(), key=keyfunc))

    def __repr__(self) -> str:
        return self.dict_.__repr__()


def main():
    sd = SortedDict(keyfunc=lambda x: x[1], c=3, d=4, a=1, b=2)
    print(sd)


if __name__ == "__main__":
    main()
