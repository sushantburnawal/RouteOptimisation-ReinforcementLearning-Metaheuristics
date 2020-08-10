# -*- coding: utf-8 -*-
# sample_R101.py

import random
from vrptwga.core import gaVRPTW


def main():
    random.seed(42)

    instName = 'R201'

    unitCost = 8.0
    initCost = 60.0
    waitCost = 0.5
    delayCost = 1.5

    individualSize = 100
    populationSize = 400
    crossoverRate = 0.85
    mutationRate = 0.01
    NumberOfGenerations = 400

    exportCSV = False

    gaVRPTW(
        instName=instName,
        unitCost=unitCost,
        initCost=initCost,
        waitCost=waitCost,
        delayCost=delayCost,
        indSize=individualSize,
        popSize=populationSize,
        cxPb=crossoverRate,
        mutPb= mutationRate,
        NGen=NumberOfGenerations,
        exportCSV=exportCSV
    )


if __name__ == '__main__':
    main()
