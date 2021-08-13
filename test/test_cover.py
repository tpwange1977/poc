from src.cau import cau

class Test_cover:
    #test case 1
    def test_add(self):
        a = cau(1, 2, 3)
        assert a == 5
    
    #test case 2
    def test_minus(self):
        a = cau(2, 2, 3)
        assert a == -1

    #test case 3
    def test_multiple(self):
        a = cau(3, 2, 3)
        assert a == 2
