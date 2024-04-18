import sys

def main() -> dict[any, any]:
    fName = sys.argv[1]
    cMap = {}
    with open(fName) as file:
        for contentLine in file:
            content = contentLine.strip()
            contentList = content.split(" ")
            city1 = contentList[0]
            city2 = contentList[1]
            drivingDist = contentList[2]
            straightDist = contentList[3]
            if cMap.get(city1):
                c1_list = cMap.get(city1)
                c1_list.append((city2, int(drivingDist), int(straightDist)))
                cMap.update({city1: c1_list})
            else:
                cMap.update({city1: [(city2, int(drivingDist), int(straightDist))]})

            if cMap.get(city2):
                c2_list = cMap.get(city2)
                c2_list.append((city1, int(drivingDist), int(straightDist)))
                cMap.update({city2: c2_list})
            else:
                cMap.update({city2: [(city1, int(drivingDist), int(straightDist))]})

    return cMap


if __name__ == "__main__":
    print(main())
