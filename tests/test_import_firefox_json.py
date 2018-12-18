import json
from buku import import_firefox_json 


def test_load_from_empty():
    """test method."""
    # Arrange
    data = json.loads("{}")

    # Act
    items = import_firefox_json(data)

    # Assert
    count = sum(1 for _ in items)
    assert 0 == count


def test_load_no_typecode():
    """test method."""
    # Arrange
    data = json.loads("""
        {
            "title" : "title",
            "children": [
                { 
                    "title" : "title1",
                    "uri" : "http://uri1",
                    "annos" : [{
                         "name": "bookmarkProperties/description", 
                         "value": "desc"
                     }]
                }]
        }
     """
    )

    # Act
    items = import_firefox_json(data)

    # Assert
    result = []
    for item in items:
        result.append(item)

    assert 0 == len(result)


def test_load_invalid_typecode():
    """test method."""
    # Arrange
    data = json.loads("""
        {
            "title" : "title",
            "children": [
                { 
                    "title" : "title1",
                    "typeCode" : 99,
                    "uri" : "http://uri1",
                    "annos" : [{
                         "name": "bookmarkProperties/description", 
                         "value": "desc"
                     }]
                }]
        }
     """
    )

    # Act
    items = import_firefox_json(data)

    # Assert
    result = []
    for item in items:
        result.append(item)

    assert 0 == len(result)


def test_load_one_child():
    """test method."""

    # Arrange
    data = json.loads("""
        {
            "title" : "title",
            "typeCode" : 2,
            "children": [
                { 
                    "title" : "title1",
                    "typeCode" : 1,
                    "uri" : "http://uri1",
                    "annos" : [{
                         "name": "bookmarkProperties/description", 
                         "value": "desc"
                     }]
                }]
        }
     """
    )

    # Act
    items = import_firefox_json(data)

    # Assert
    result = []
    for item in items:
        result.append(item)

    assert 1 == len(result)
    assert 'http://uri1' == result[0][0]
    assert 'title1' == result[0][1]
    assert ',' == result[0][2]
    assert 'desc' == result[0][3]



def test_load_one_container_child():
    """test method."""

    # Arrange
    data = json.loads("""
        {
            "title" : "title",
            "typeCode" : 2,
            "children": [
                {
                    "guid":"mobile______",
                    "title":"Mobile Lesezeichen",
                    "index":4,
                    "dateAdded":1489602681463000,
                    "lastModified":1519334403977000,
                    "id":330524,
                    "typeCode":2,
                    "annos":[
                        {
                            "name":"mobile/bookmarksRoot",
                            "value":"1",
                            "expires":4,
                            "flags":0
                        }],
                    "type":"text/x-moz-place-container",
                    "root":"mobileFolder"
                } ]
         }""")


    # Act
    items = import_firefox_json(data)

    # Assert
    result = []
    for item in items:
        result.append(item)

    assert 0 == len(result)


def test_load_many_children():
    """test method."""

    # Arrange
    data = json.loads("""
            {
                "guid":"unfiled_____",
                "title":"Weitere Lesezeichen",
                "index":3,
                "dateAdded":1305446109028000,"lastModified":1544905385223000,
                "id":5,
                "typeCode":2,
                "type":"text/x-moz-place-container",
                "root":"unfiledBookmarksFolder",
                "children": [
                    {"guid":"_0yvSg7JN7WD","title":"title1","index":0,"dateAdded":1287656058186000,"lastModified":1305978155312000,"id":169,"typeCode":1,"charset":"UTF-8","annos":[{"name":"bookmarkProperties/description","value":"desc3","expires":4,"flags":0}],"type":"text/x-moz-place","uri":"http://uri1.com/#more-74"},
                    {"guid":"YI8BEgRJ1Hio","title":"title2","index":1,"dateAdded":1232202012000000,"lastModified":1305978155291000,"id":157,"typeCode":1,"charset":"ISO-8859-1","annos":[{"name":"bookmarkProperties/description","value":"desc2","expires":4,"flags":0}],"type":"text/x-moz-place","uri":"http://uri2.com/xyz"},
                    {"guid":"XYewkZ6jVnOt","title":"title3","index":2,"dateAdded":1236767103079000,"lastModified":1305978155293000,"id":158,"typeCode":1,"charset":"ISO-8859-1","type":"text/x-moz-place","uri":"http://uri3.com"}
                ]
            } """)

    # Act
    items = import_firefox_json(data)

    # Assert
    result = []
    for item in items:
        result.append(item)

    assert 3 == len(result)


# Tests TODO:
# separator type code
# multiple tags
# hierarchic folders
# utf-8 encoded titles
# non-generic url
# tags with comma(?), UTF chars, ...
# endurance test (>200 entries)

if __name__ == '__main__':
    main()
