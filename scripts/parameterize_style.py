#!/usr/bin/python

import os
import codecs
import argparse
from lxml import etree
 
NS = {'svg': "http://www.w3.org/2000/svg"}
 
parser = argparse.ArgumentParser(description="My first Inkscape effect")
parser.add_argument('--id', action="append", help="id(s) of selected elements")
parser.add_argument('path', help="path of svg file to open")
 
args = parser.parse_args()

path, filename = os.path.split(args.path)
filename = os.path.splitext(filename)[0]
newfilename = '%s_param.svg' % filename
newpath = os.path.join(path, newfilename)
 
# Open the file & parse to a "etree" object
f = codecs.open(args.path, encoding="utf-8")
t = etree.parse(f)
 
# I. Select and alter existing elements
#
# Loop over all svg:path elements
for path in t.xpath("//svg:path ", namespaces=NS):
    style = path.get("style")
    if style:
        try:
            del path.attrib["style"]
        except:
            pass
        path.set("fill", "param(fill) none")
        path.set("stroke", "param(outline) #00ff00")
        path.set("stroke-width", "param(outline-width) 1")
# Loop over all svg:g elements
for path in t.xpath("//svg:g ", namespaces=NS):
    style = path.get("style")
    if style:
        try:
            del path.attrib["style"]
        except:
            pass
        path.set("fill", "param(fill) none")
        path.set("stroke", "param(outline) #00ff00")
        path.set("stroke-width", "param(outline-width) 1")
# Loop over all svg:polyline elements
for path in t.xpath("//svg:polyline ", namespaces=NS):
    style = path.get("style")
    if style:
        # try:
        #     del path.attrib["style"]
        # except:
        #     pass
        path.set("fill", "param(fill) none")
        path.set("stroke", "param(outline) #00ff00")
        path.set("stroke-width", "param(outline-width) 1")

# Output the (modified) tree

f = open(newpath, 'w')
f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
f.write(etree.tostring(t, pretty_print=True, encoding="utf-8", xml_declaration=True))
f.close()
