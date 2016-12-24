"""Core module for interacting with LEPD"""
__author__    = "Copyright (c) 2016, Mac Xu <shinyxxn@hotmail.com>"
__copyright__ = "Licensed under GPLv2 or later."


from backend.MemoryMonitor import MemoryMonitor

from backend.tests.UnitTester import UnitTester

class GetProcMeminfoTester(UnitTester):

    def __init__(self):

        UnitTester.__init__(self, 'GetProcMeminfo')
        self.loadJson()
    
    def test(self):
        for sampleData in self.sampleDatas:
            self.report(sampleData)
            
            resultLines = self.getResultList(sampleData)
            # for line in resultLines:
            #     print(line)

            monitor = MemoryMonitor('XXX')
            
            parsedData = monitor.getCapacity(resultLines)
            self.pp.pprint(parsedData)

        

if( __name__ =='__main__' ):

    tester = GetProcMeminfoTester()
    tester.test()
    
    