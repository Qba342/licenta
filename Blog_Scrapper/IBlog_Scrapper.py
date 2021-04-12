from abc import ABC,ABCMeta,abstractmethod


class IBlog_Scrapper(ABC):
    __metaclass__=ABCMeta


    @abstractmethod
    def DownloadResources(self):
        raise NotImplementedError

