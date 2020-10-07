import unittest
import Lab2_XXXXXXX as test
# You must import your script name (ex: Lab2_12345678), no file extension,
# followed by 'as test'
# example: import Lab1_12345678 as test
# You must also add sample_input_lab2.txt AND sample_output_lab2.txt
# in the same folder as your running script


class Lab1StudentTest(unittest.TestCase):
    def test1(self):
        self.assertEqual( test.validWord('aloha'), True)
    def test2(self):
        self.assertEqual( test.validWord('guava'), False)
    def test3(self):
        self.assertEqual( test.pronunciate('E komo mai'), 'Eh Koh-moh Meye')
    def test4(self):
        self.assertEqual( test.pronunciate('maika\'i mahalo'), 'Meye-kah\'ee Mah-hah-loh')
    def test5(self):
        test.createGuide( 'sample_input_lab2.txt', 'LAB2_OUTPUT.txt')
        xFile = open('LAB2_OUTPUT.txt', 'r')
        yFile = open('sample_output_lab2.txt')
        for line in xFile:
            self.assertEqual( yFile.readline(), line)
        xFile.close()
        yFile.close()
   
if __name__ == "__main__":
    unittest.main()

