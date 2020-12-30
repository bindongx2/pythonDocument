#데이터 마크업하는 방식에는 XML, JSON이 있습니다.
#하지만 XML을 더 많이 사용
import xml.etree.ElementTree as ET

data ='''
<person>
    <name>Chuch</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromString(data)

print("Name:", tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))
