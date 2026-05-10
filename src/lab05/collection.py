from lab3.base import Server
from lab3.collection2 import ExtendedServerCluster

class FunctionalServerCluster(ExtendedServerCluster):
    
    def sort_by(self, key_func):
        result = FunctionalServerCluster()
        sorted_list = sorted(self._servers, key=key_func)
        for s in sorted_list:
            result.add(s)
        return result

    def filter_by(self, predicate):
        result = FunctionalServerCluster()
        filtered_list = list(filter(predicate, self._servers))
        for s in filtered_list:
            result.add(s)
        return result

    def apply(self, func):
        for s in self._servers:
            func(s)
        return self