import sys
import json

try:
    from pymongo.bson import BSON
except ImportError:
    from bson import BSON

def get_doc_size(doc):
    """
    Get document size in bytes

    :Parameters:
        - `doc`: string or dict

    """
    if not isinstance(doc, dict):
        doc = json.loads(doc)

    return len(BSON.encode(doc))


def main():
    document = sys.stdin.read()
    size = get_doc_size(document)

    print
    print "Document size: %d" % size


if __name__ == "__main__":
    sys.exit(main())
