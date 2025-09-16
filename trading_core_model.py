from abc import ABC,abstractmethod

class TradingSystemModel(ABC):
    """
    A complete Trading System
    """
    @abstractmethod
    def market(self, data):
        """what to bug or sell"""
        pass
    @abstractmethod
    def position_sizing(self,data):
        """how much to buy or sell"""
        pass
    @abstractmethod
    def entries(self,data):
        pass
    @abstractmethod
    def stops(self,data):
        """when to get out of a losing position"""
        pass
    @abstractmethod
    def exits(self,data):
        """when to get out of a wining position"""
        pass
    @abstractmethod
    def tactics(self,data):
        """how to buy or sell"""
        pass


