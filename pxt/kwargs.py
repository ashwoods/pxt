class KwArgs(dict):
    """
    Keyword argument helper class.
    """

    def __init__(self, kwargs: dict):
        """
        Constructor.

        Parameters
        ----------
        kwargs
            Keyword arguments of a function or method.
        """
        super().__init__(kwargs)

    def try_get(self, key, default=None):
        return self[key] if key in self else default

    def extract(self, *keys):
        """
        Extract the specified key(s) from the keyword arguments (`kwargs`).
        The function will not raise an error if a key does not exist.

        Parameters
        ----------
        keys : str
            One or more string keys that should be removed from the
            keyword arguments `kwargs` and returned by the function.

        Returns
        -------
        dict
            Returns all key value pairs as a dictionary that could
            be found in the `kwargs` input argument.
        """
        result = dict()
        # search for all specified keys in the kwargs
        for key in keys:
            # if the key exists put it into the result
            # dictionary and remove it from the kwargs
            if key in self:
                result[key] = self[key]
                del self[key]

        # return the result no matter if
        # a key was found or not
        return result

    def append(self, key, value):
        """
        Add or append the specified key-value pair.

        Returns
        -------
        new_value
            Returns the updated value.
        """
        # if the key already exists, we need to make sure
        # that the current value is appended correctly
        if key in self:
            # get the current value
            new_value = self.__getitem__(key)

            # because we need to append the current
            # value, it needs to be a list
            if not isinstance(new_value, list):
                new_value = [new_value]

            # if the value to append is also a list
            # we merge them, otherwise we only add it
            if isinstance(value, list):
                new_value = new_value + value
            else:
                new_value.append(value)
        else:
            # the key does not yet exist so
            # we simply add the key-value pair
            new_value = value

        self.__setitem__(key, new_value)
        return new_value
