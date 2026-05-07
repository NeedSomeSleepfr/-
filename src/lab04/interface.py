from abc import ABC, abstractmethod

class IMonitorable(ABC): 
    @abstractmethod
    def get_metrics(self):
        pass
    
class IComparable(ABC):
    @abstractmethod
    def compare(self, other):
        pass