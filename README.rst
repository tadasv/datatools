Data Tools
==========

This repo contains various utilities for working with data

bsonsize.py
-----------

Get size of a MongoDB document or any other dict stored as BSON

Usage::

  $ python bsonsize.py << EOF
  > {"menu": {
  >   "id": "file",
  >   "value": "File",
  >   "popup": {
  >     "menuitem": [
  >       {"value": "New", "onclick": "CreateNewDoc()"},
  >       {"value": "Open", "onclick": "OpenDoc()"},
  >       {"value": "Close", "onclick": "CloseDoc()"}
  >     ]
  >   }
  > }}
  > EOF

  Document size: 219