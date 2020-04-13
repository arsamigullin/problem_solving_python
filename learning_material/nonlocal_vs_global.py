class NonLocalVsGlobal:
    def testNonLocal(self):
        # this works
        res = []
        var = 0
        for i in range(5):
            var+=1
            res.append(var)
        print(var,res)

        def helper():
            #nonlocal var, res # without nonlocal this code throws an error
            if var == 10:
                return
            print(var)
            #res+=[108]
            res.append(var)

        helper()
        print(var,res)
if __name__ == "__main__":
    s=NonLocalVsGlobal()
    s.testNonLocal()