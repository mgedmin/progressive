# -*- coding: utf-8 -*-
from abc import abstractproperty, ABCMeta


class Block(object):
    """Building block for a progress view"""
    __metaclass__ = ABCMeta

    @abstractproperty
    def view(self):
        """Returns a unicode string representing the block

        :rtype: unicode|str
        """
        raise NotImplementedError

    @abstractproperty
    def len(self):
        """A more accurate ``len(self.view)`` if ``self.view``
        has custom formatting for which ``len`` gives incorrect output.

        :rtype: list|int
        """
        raise NotImplementedError

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, self.view)
