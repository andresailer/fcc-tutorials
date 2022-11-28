#!/bin/env python
import sys, ROOT
from histoprint import print_hist

ROOT.gROOT.SetBatch(True)

if len(sys.argv) < 2:
    print("Please specify input file"); sys.exit(1)
inputFile = sys.argv[1]; print("Reading:", inputFile)

tfile = ROOT.TFile.Open(inputFile)
myTree = tfile.Get("events")
myTree.Draw("ECalEndcapCollection.position.z>>zHist(100, 2300, 2510)",
            "ECalEndcapCollection.position.z > 0")
myTree.Draw("ECalEndcapCollection.energy>>eHist(30, 0, 0.002)")

print_hist(tfile.Get("zHist"), title="Hits per Layer")
print_hist(tfile.Get("eHist"), title="Energy per Hit")
