from phoenix.Observation.ObservationStrategy import ObservationStrategy


class OManager():
    def __init__(self, observationStrategy: ObservationStrategy):
        self.__observationStrategy: ObservationStrategy = observationStrategy

    def getObservationStrategy(self):
        return self.__observationStrategy
    
    def setObservationStrategy(self, observationStrategy: ObservationStrategy):
        self.__observationStrategy = observationStrategy

    def start(self, *args, **kwargs):
        return self.__observationStrategy.start(*args, **kwargs)
    
    def stop(self):
        return self.__observationStrategy.stop()