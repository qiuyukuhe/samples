class PricingCalculator:
    def __init__(self):
        pass

    def Calculate(self, source, destination, pax):
        if source == 'Bergen':
            return 200
        else:
            return 100