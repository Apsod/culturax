import itertools
import pathlib
import json
from huggingface_hub import HfFileSystem

fs = HfFileSystem()

with open('langs.json') as langfile:
    langs = json.load(langfile)

valid = set()
codemap = {}
types = ['iso639_1', 'iso639_3']
for k, v in langs.items():
    for c in [v[t] for t in types if t in v]:
        valid.add(c)
        codemap[c] = k



root = 'datasets/uonlp/CulturaX'

for de in fs.ls(root):
    lang = de['name'].split('/')[-1]
    if lang in valid and (de['type'] == 'directory'):
        for file in fs.ls(de['name']):
            file = file['name'].split('/')[-1]
            print('/'.join([
                'https://huggingface.co',
                root , 'resolve' , 'main' , lang , file
                ]))

