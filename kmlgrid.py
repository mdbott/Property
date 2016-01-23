#!/usr/bin/python
"""
kmlgrid - Generate a grid pattern in KML

Usage: kmlgrid [-h | -c "RGBHEX"][-w linewidth][-s scale] ul_lat ul_lon lr_lat lr_lon ny nx 

"""

from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
import sys
import getopt
import os.path, os
import string, re
from numpy import *
from pykml.parser import Schema
from pykml import parser

def makekml(args,dparams):
    stylename="sn_color_line"
    pointstylename="sn_point"
    fld=KML.Folder()
    [ul_lat,ul_lon,lr_lat,lr_lon,nx,ny]=[float(i) for i in args]
    min_lon=min(lr_lon,ul_lon)
    max_lon=max(lr_lon,ul_lon)
    min_lat=min(lr_lat,ul_lat)
    max_lat=max(lr_lat,ul_lat)
    dx=(max_lon-min_lon)/nx
    dy=(max_lat-min_lat)/ny
    for x in arange(min_lon,max_lon+(dx/2.),dx):
        line=KML.Placemark(
            KML.name("Parallel {0}-0".format(x)),
            KML.styleUrl('#{0}'.format(stylename)),
            KML.LineString(
                KML.altitudeMode("clampToGround"),
                KML.coordinates(
                    "{0},{1},{2}\n".format(x,min_lat,0),
                    "{0},{1},{2}".format(x,max_lat,0)
                ),
            ),
        )
        fld.append(line)
    for y in arange(min_lat,max_lat+(dy/2.),dy):
        line=KML.Placemark(
            KML.name("Meridian 0-{0}".format(y)),
            KML.styleUrl('#{0}'.format(stylename)),
            KML.LineString(
                KML.altitudeMode("clampToGround"),
                KML.coordinates(
                    "{0},{1},{2}\n".format(min_lon,y,0),
                    "{0},{1},{2}".format(max_lon,y,0)
                ),
            ),
        )
        fld.append(line)
    i=0
    for x in arange(min_lon,max_lon+(dx/2.),dx):
        for y in arange(min_lat,max_lat+(dy/2.),dy):
            i=i+1
            point=KML.Placemark(
                KML.styleUrl("#{0}".format(pointstylename)),
                KML.ExtendedData(
                    KML.Data(
                        KML.value("Point {0}".format(i)),
                        name="point_number",
                    ),
                ),
                KML.Point(
                    KML.coordinates(
                        "{0},{1},{2}\n".format(x,y,0)
                    ),
                ),
            )
            fld.append(point)

    stl=KML.Style(
        KML.LineStyle(
            KML.color("{0}".format(dparams['color'])),
            KML.width("{0}".format(dparams['width'])),
        ),
        id=stylename,
    )
    pstl=KML.Style(
        KML.IconStyle(
            KML.color("{0}".format(dparams['color'])),
            KML.scale(dparams['symbol-scale']),
            KML.Icon(
                KML.href(dparams['symbol']),
            ),
        ),
        KML.BalloonStyle(
            KML.text('<h1>$[point_number]</h1>'),
        ),
        id=pointstylename,
    )
    doc=KML.kml(
        KML.Document(
            etree.Comment("Produced with {0}".format(sys.argv)),
            stl,
            pstl,
            fld,
        )
    )
    if dparams['browser']==True:
    	print 'application/vnd.google-earth.kml+xml'
    print etree.tostring(doc, pretty_print=True)

def readinit(shortargs,longargs,dparams,expr):
    share_home=os.environ['HOME']+"/share/kmlgrid.ini"
    try:
        fi=open("kmlgrid.ini",'rU')
    except:
        print>>sys.stderr, "No kmlgrid.ini found in current directory."
        try:
            fi=open(share_home,'rU')
        except:
            print>>sys.stderr, "No kmlgrid.ini found in %s."%(share_home)
            try:
                fi=open("/usr/share/kmlgrid.ini",'rU')
            except:
                print>>sys.stderr, 'Cannot find kmlgrid.ini in /usr/share.'
                raise
    for line in fi:
        # line: shortarg longarg default [expr]
        # dict key is base of longarg
        # parsing arguments will evaluate expr
        ll=re.split('\s+',line)
        shortargs.append(ll[0])
        longargs.append(ll[1])
        k=re.sub(r'=',r'',ll[1])
        dparams[k]=ll[2]
        if len(ll)>2:
            expr[k]=ll[3]
                
def main(argv=None):
    if argv is None:
        argv = sys.argv
    dparams=dict()
    shortargs=[]
    longargs=[]
    expr=dict()
    readinit(shortargs,longargs,dparams,expr)
    try:
        opts, args = getopt.getopt(sys.argv[1:], string.join(shortargs), longargs)
    except getopt.error, msg:
        print >>sys.stderr, msg
        print >>sys.stderr, "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        for pair in zip(shortargs, longargs):
            pair=list(pair)
            k=re.sub(r'=',r'',pair[1])
            pair[0]="-"+re.sub(r':',r'',pair[0])
            pair[1]="--"+k
            if o in pair:
                try:
                    dparams[k]=eval(expr[k])
                except:
                    dparams[k]=True
    # process arguments
    makekml(args,dparams) # process() is defined elsewhere

if __name__ == "__main__":
    sys.exit(main())
