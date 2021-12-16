import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from random import randint
import csv

from tqdm import tqdm

rename = {
   'salary': 'salary',
   'educationType': 'educationType',
   'workExperienceList/workExperience[1]/jobTitle': 'jobTitle',
   "educationList/educationType[1]/qualification": 'qualification',
   'gender': 'gender',
   'innerInfo/dateModify': 'dateModify',
   "skills": "skills",
   "otherInfo": "otherInfo"
}

class ReadByChunk():
   def __init__(self, file, tag="cv", bufsize=1):
        self.tag = tag
        self._buf = ""
        self.file = open(file, encoding="utf8")
        self.bufsize = bufsize

   def tags(self):
        while True:
            pos = self._buf.find(f'<{self.tag} ')
            if pos == -1:
                self._buf += self.file.read(self.bufsize * 1024 * 1024)
                pos = self._buf.find(f'<{self.tag} ')
                if pos == -1:
                    raise StopIteration
            self._buf = self._buf[pos:]

            end_pos = self._buf.find(f'</{self.tag}>')
            if end_pos == -1:
                self._buf += self.file.read(self.bufsize * 1024 * 1024)
                end_pos = self._buf.find(f'</{self.tag}>')
                if end_pos == -1:
                    raise StopIteration

            xml_tag = self._buf[:end_pos+len(f'</{self.tag}>')]
            self._buf = self._buf[end_pos+len(f'</{self.tag}>'):]
            try:
                root = ET.fromstring(xml_tag)
            except ParseError as e:
                pass
            yield root


reader = ReadByChunk("cv.xml", bufsize=1)

with open('works.csv', 'w', newline='') as csvfile:
    fieldnames = list(rename.values())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for tag in tqdm(reader.tags()):
        props = {}
        for k, v in rename.items():
            try:
                props[v] = tag.find(k).text
            except:
                props[v] = ""

        if randint(0, 100) == 0:
            writer.writerow(props)

