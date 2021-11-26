import unittest

from Unittests.HoekClass import HoekClass


class TestStringMethods(unittest.TestCase):
    # test_ prependen
    def test_berekenHoek(self):
        # arrange    
        hoekClass = HoekClass()

        # act
        berekendeHoek0 = hoekClass.berekenHoek(0)
        berekendeHoek180 = hoekClass.berekenHoek(180)
        berekendeHoek240 = hoekClass.berekenHoek(240)

        # assert
        self.assertEqual(0, berekendeHoek0)
        self.assertEqual(180, berekendeHoek180)
        self.assertEqual(-120, berekendeHoek240)


if __name__ == '__main__':
    unittest.main()
