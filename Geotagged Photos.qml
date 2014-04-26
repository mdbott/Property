<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="0.10.0-Io" >
  <maplayer minScale="1" maxScale="1e+08" scaleBasedVisibilityFlag="0" geometry="Point" type="vector" >
    <id>_public___geotagged_photos___the_geom__sql_20080524132829509</id>
    <datasource>dbname='testgis' host=localhost port=5432 user='postgres' password='postgres' table="geotagged_photos" (the_geom) sql=</datasource>
    <layername>geotagged_photos</layername>
    <srs>
      <spatialrefsys>
        <proj4>+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs </proj4>
        <srsid>2585</srsid>
        <srid>4326</srid>
        <epsg>4326</epsg>
        <description>WGS 84</description>
        <projectionacronym>longlat</projectionacronym>
        <ellipsoidacronym>WGS84</ellipsoidacronym>
        <geographicflag>false</geographicflag>
      </spatialrefsys>
    </srs>
    <transparencyLevelInt>255</transparencyLevelInt>
    <provider>postgres</provider>
    <encoding>System</encoding>
    <displayfield>photo_id</displayfield>
    <label>0</label>
    <attributeactions>
      <actionsetting action="open /Applications/Preview.app &quot;%file_path&quot;" capture="1" name="View Image" />
    </attributeactions>
    <singlesymbol>
      <symbol>
        <lowervalue></lowervalue>
        <uppervalue></uppervalue>
        <label></label>
        <pointsymbol>svg:/Applications/qgis0.10.0.app/Contents/MacOS/share/qgis/svg/gpsicons/camera.svg</pointsymbol>
        <pointsize>14</pointsize>
        <rotationclassificationfield>-1</rotationclassificationfield>
        <scaleclassificationfield>-1</scaleclassificationfield>
        <outlinecolor red="0" blue="0" green="0" />
        <outlinestyle>SolidLine</outlinestyle>
        <outlinewidth>1</outlinewidth>
        <fillcolor red="222" blue="188" green="161" />
        <fillpattern>SolidPattern</fillpattern>
        <texturepath></texturepath>
      </symbol>
    </singlesymbol>
    <labelattributes>
      <label field="" text="Label" />
      <family field="" name="Lucida Grande" />
      <size field="" units="pt" value="12" />
      <bold field="" on="0" />
      <italic field="" on="0" />
      <underline field="" on="0" />
      <color field="" red="0" blue="0" green="0" />
      <x field="" />
      <y field="" />
      <offset x="0" y="0" yfield="-1" xfield="-1" units="pt" />
      <angle field="" value="0" />
      <alignment field="-1" value="center" />
      <buffercolor field="" red="255" blue="255" green="255" />
      <buffersize field="" units="pt" value="1" />
      <bufferenabled field="" on="" />
    </labelattributes>
  </maplayer>
</qgis>
