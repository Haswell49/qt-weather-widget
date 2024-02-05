import abc


# Abstract Base Class (ABC)


class Observer:
    @abc.abstractmethod
    def update_state(self, data):
        pass


class Observable:
    @abc.abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def _notify(self, data):
        pass
