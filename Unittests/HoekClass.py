class HoekClass:
    def berekenHoek(self, param):
        if param > 180:
            return param - 360
        return param