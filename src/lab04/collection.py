from lab3.collection2 import ExtendedServerCluster as BaseCluster
from lab4.interface import IMonitorable, IComparable

class InterfaceServerCluster(BaseCluster):

    def get_monitorables(self):
        result = InterfaceServerCluster()
        for s in self._servers:
            if isinstance(s, IMonitorable):
                result.add(s)
        return result

    def get_comparables(self):
        result = InterfaceServerCluster()
        for s in self._servers:
            if isinstance(s, IComparable):
                result.add(s)
        return result

    def print_all_metrics(self):
        for s in self._servers:
            if isinstance(s, IMonitorable):
                print(s.get_metrics())

    def sort_by_compare(self):
        count = len(self._servers)
        for i in range(count):
            for j in range(0, count - i - 1):
                if self._servers[j].compare(self._servers[j + 1]) > 0:
                    temp = self._servers[j]
                    self._servers[j] = self._servers[j + 1]
                    self._servers[j + 1] = temp