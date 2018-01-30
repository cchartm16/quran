import xml.etree.ElementTree as ET




if __name__ == "__main__":
    with open(r'/home/nasr/PycharmProjects/quran/quran-uthmani.txt', 'r') as quran:
        mushaf = quran.read()
        main_text = ET.ElementTree(file="quran-uthmani.xml")
        metadata = ET.ElementTree(file="quran-data.xml")

        root = metadata.getroot()

        lookup_method = "suras"

        chapter = 'the opening'


        suras = iter(root.find(lookup_method))

        print(suras.__next__().attrib)
            # if child.attrib['ename'] == chapter.title():
            #     print(mushaf.split('\n')[int(child.attrib['start'])])
            #     break


