<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.8.3-Wien" minimumScale="5000" maximumScale="1e+08" simplifyDrawingHints="0" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
  <edittypes>
    <edittype widgetv2type="Hidden" name="row_number">
      <widgetv2config fieldEditable="1" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="Hidden" name="vegetationid">
      <widgetv2config fieldEditable="1" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="botanicalid">
      <widgetv2config fieldEditable="1" labelOnTop="0">
        <value key="Almond" value="5242"/>
        <value key="Apple" value="4053"/>
        <value key="Apricot" value="5214"/>
        <value key="Avocado" value="7413"/>
        <value key="Black chokeberry" value="673"/>
        <value key="Black locust" value="5736"/>
        <value key="Black mulberry" value="4267"/>
        <value key="Black walnut" value="3477"/>
        <value key="Blackberry" value="5861"/>
        <value key="Blackcurrant" value="5695"/>
        <value key="Blackwood" value="51"/>
        <value key="Boldu" value="4713"/>
        <value key="Brown Barrel" value="7408"/>
        <value key="Burr oak" value="5487"/>
        <value key="Cherry ballart" value="7403"/>
        <value key="Chilean hazel" value="3019"/>
        <value key="Chinese cedar" value="6830"/>
        <value key="Coast grey box" value="7401"/>
        <value key="Comfrey" value="6673"/>
        <value key="Cork oak" value="5510"/>
        <value key="Cornelian cherry" value="1955"/>
        <value key="Creeping Lantana" value="7406"/>
        <value key="Custard Apple" value="7418"/>
        <value key="Dwarf banana" value="4280"/>
        <value key="Elaeagnus" value="2488"/>
        <value key="Fig" value="2811"/>
        <value key="Grapefruit" value="7412"/>
        <value key="Hazel" value="1993"/>
        <value key="Hedge bamboo" value="973"/>
        <value key="High-bush blueberry" value="7040"/>
        <value key="Holly oak" value="5474"/>
        <value key="Holm oak" value="5475"/>
        <value key="Indian bean tree" value="1485"/>
        <value key="Italian alder" value="378"/>
        <value key="Italian stone pine" value="4908"/>
        <value key="Lemon" value="1761"/>
        <value key="Lightwood" value="7404"/>
        <value key="Loquat" value="2598"/>
        <value key="Macadamia" value="4002"/>
        <value key="Mandarin" value="1762"/>
        <value key="Manna gum" value="2697"/>
        <value key="New Zealand flax" value="4745"/>
        <value key="Olive" value="4396"/>
        <value key="Osage orange" value="4005"/>
        <value key="Peach" value="5286"/>
        <value key="Pear" value="5421"/>
        <value key="Pecan" value="1445"/>
        <value key="Pedunculate oak" value="5505"/>
        <value key="Pin oak" value="5497"/>
        <value key="Pistachio" value="4937"/>
        <value key="Plum" value="5241"/>
        <value key="Pomegranate" value="5387"/>
        <value key="Pomelo" value="7415"/>
        <value key="Raspberry" value="5874"/>
        <value key="Red gum" value="7398"/>
        <value key="Redcurrant" value="5714"/>
        <value key="Ryoku-chiku" value="974"/>
        <value key="Stinging nettle" value="7007"/>
        <value key="Sweet alyssum" value="3876"/>
        <value key="Sweet chestnut" value="1466"/>
        <value key="Sweet orange" value="1763"/>
        <value key="Tangelo" value="7417"/>
        <value key="Walnut" value="3478"/>
        <value key="White Stringybark" value="7402"/>
        <value key="White clover" value="6886"/>
        <value key="White mulberry" value="4259"/>
        <value key="Wild daffodil" value="4326"/>
        <value key="Wild leek" value="295"/>
        <value key="Yarrow" value="95"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="legacy_pfaf_latin_name">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="family">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="genus">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="species">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="ssp">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="common_name">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="type">
      <widgetv2config fieldEditable="1" labelOnTop="0">
        <value key="Fibre Plants" value="3"/>
        <value key="Fruit" value="1"/>
        <value key="Groundcovers" value="7"/>
        <value key="Leaf Crops" value="5"/>
        <value key="Lumber Trees" value="4"/>
        <value key="Native Species" value="8"/>
        <value key="Nitrogen Fixers" value="6"/>
        <value key="Nuts" value="2"/>
        <value key="Weed Species" value="9"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="dripline_radius">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="comment">
      <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
    </edittype>
  </edittypes>
  <renderer-v2 attr="genus" symbollevels="0" type="categorizedSymbol">
    <categories>
      <category render="true" symbol="0" value="" label=""/>
      <category render="true" symbol="1" value="Acacia" label="Acacia"/>
      <category render="true" symbol="2" value="Achillea" label="Achillea"/>
      <category render="true" symbol="3" value="Allium" label="Allium"/>
      <category render="true" symbol="4" value="Alnus" label="Alnus"/>
      <category render="true" symbol="5" value="Aronia" label="Aronia"/>
      <category render="true" symbol="6" value="Bambusa" label="Bambusa"/>
      <category render="true" symbol="7" value="Carya" label="Carya"/>
      <category render="true" symbol="8" value="Catalpa" label="Catalpa"/>
      <category render="true" symbol="9" value="Citrus" label="Citrus"/>
      <category render="true" symbol="10" value="Corylus" label="Corylus"/>
      <category render="true" symbol="11" value="Elaeagnus" label="Elaeagnus"/>
      <category render="true" symbol="12" value="Eucalyptus" label="Eucalyptus"/>
      <category render="true" symbol="13" value="Exocarpos" label="Exocarpos"/>
      <category render="true" symbol="14" value="Ficus" label="Ficus"/>
      <category render="true" symbol="15" value="Juglans" label="Juglans"/>
      <category render="true" symbol="16" value="Lantana" label="Lantana"/>
      <category render="true" symbol="17" value="Lobularia" label="Lobularia"/>
      <category render="true" symbol="18" value="Macadamia" label="Macadamia"/>
      <category render="true" symbol="19" value="Maclura" label="Maclura"/>
      <category render="true" symbol="20" value="Malus" label="Malus"/>
      <category render="true" symbol="21" value="Morus" label="Morus"/>
      <category render="true" symbol="22" value="Narcissus" label="Narcissus"/>
      <category render="true" symbol="23" value="Olea" label="Olea"/>
      <category render="true" symbol="24" value="Persea" label="Persea"/>
      <category render="true" symbol="25" value="Peumus" label="Peumus"/>
      <category render="true" symbol="26" value="Phormium" label="Phormium"/>
      <category render="true" symbol="27" value="Pinus" label="Pinus"/>
      <category render="true" symbol="28" value="Pistacia" label="Pistacia"/>
      <category render="true" symbol="29" value="Prunus" label="Prunus"/>
      <category render="true" symbol="30" value="Punica" label="Punica"/>
      <category render="true" symbol="31" value="Pyrus" label="Pyrus"/>
      <category render="true" symbol="32" value="Quercus" label="Quercus"/>
      <category render="true" symbol="33" value="Robinia" label="Robinia"/>
      <category render="true" symbol="34" value="Rubus" label="Rubus"/>
      <category render="true" symbol="35" value="Symphytum" label="Symphytum"/>
      <category render="true" symbol="36" value="Toona" label="Toona"/>
      <category render="true" symbol="37" value="Trifolium" label="Trifolium"/>
      <category render="true" symbol="38" value="Urtica" label="Urtica"/>
      <category render="true" symbol="39" value="Vaccinium" label="Vaccinium"/>
    </categories>
    <symbols>
      <symbol alpha="1" type="marker" name="0">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/test_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="1">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Acacia_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#36ba52"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="10">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#42e836"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="11">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Elaeagnus.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="12">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Quercus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#b2df8a"/>
          <prop k="outline_width" v="1.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="13">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="14">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="0.1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="15">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#36ba52"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="16">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/test_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="17">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/SweetAlyssum_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#42e836"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="18">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Citrus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#65b910"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="19">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/OsageOrange_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#61fd59"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="2">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Yarrow_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00a900"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="20">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#00ff00"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Malus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="21">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Citrus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="22">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Dafodil_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="23">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Olive_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#b2df8a"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="24">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#65b910"/>
          <prop k="outline_width" v="0.1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="25">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Boldo_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#36ba52"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="26">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/test_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="27">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Pinus.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="28">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="29">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#00ff00"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Malus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.6"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="3">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/WildLeek_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00a900"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="30">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Pomegranite_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#36ba52"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="31">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#00ff00"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Malus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#95ff00"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="32">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#6f4816"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./Quercus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="33">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="34">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Rubus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00a900"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="35">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Symphytum_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#33a02c"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="36">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/test_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="37">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Clover_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#42e836"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="38">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/test_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="39">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Citrus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#b2df8a"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="4">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Citrus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#42e836"/>
          <prop k="outline_width" v="0.5"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="5">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#ffffff"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Ficus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#36ba52"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="6">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Bambusa.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="7">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#33a02c"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Quercus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#65b910"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="8">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#895418"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Quercus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#42e836"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="9">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v="./symbols/Citrus_param.svg"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#61fd59"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol alpha="1" type="marker" name="0">
        <layer pass="0" class="SvgMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="#000000"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="name" v=""/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0"/>
          <prop k="offset_unit" v="MapUnit"/>
          <prop k="outline_color" v="#00ff00"/>
          <prop k="outline_width" v="1"/>
          <prop k="outline_width_map_unit_scale" v="0,0"/>
          <prop k="outline_width_unit" v="MapUnit"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="0,0"/>
          <prop k="size_unit" v="MapUnit"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp type="gradient" name="[source]">
      <prop k="color1" v="255,245,235,255"/>
      <prop k="color2" v="127,39,4,255"/>
      <prop k="discrete" v="0"/>
      <prop k="stops" v="0.13;254,230,206,255:0.26;253,208,162,255:0.39;253,174,107,255:0.52;253,141,60,255:0.65;241,105,19,255:0.78;217,72,1,255:0.9;166,54,3,255"/>
    </colorramp>
    <invertedcolorramp value="0"/>
    <rotation/>
    <sizescale field="dripline_radius / 250" scalemethod="diameter"/>
  </renderer-v2>
  <customproperties>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="false"/>
    <property key="labeling/bufferJoinStyle" value="64"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/distMapUnitMaxScale" value="0"/>
    <property key="labeling/distMapUnitMinScale" value="0"/>
    <property key="labeling/enabled" value="true"/>
    <property key="labeling/fieldName" value=" concat ( &quot;common_name&quot; ,' (', &quot;genus&quot; ,' ', &quot;species&quot; ,' ', &quot;ssp&quot; ,')')"/>
    <property key="labeling/fontBold" value="true"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="Ubuntu"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="12"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="63"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="20"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="0"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Medium"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="0"/>
    <property key="labeling/placementFlags" value="0"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
    <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="500"/>
    <property key="labeling/scaleMin" value="50"/>
    <property key="labeling/scaleVisibility" value="true"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="true"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
    <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>4</featureBlendMode>
  <layerTransparency>46</layerTransparency>
  <displayfield>legacy_pfaf_latin_name</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Label"/>
    <family fieldname="" name="Ubuntu"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <editform>.</editform>
  <editforminit/>
  <featformsuppress>0</featformsuppress>
  <annotationform>.</annotationform>
  <editorlayout>generatedlayout</editorlayout>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions>
    <actionsetting action="from PyQt4.QtCore import QUrl; from PyQt4.QtWebKit import QWebView;  myWV=QWebView(None);myWV.setWindowTitle('Local Wiki Link');myWV.load(QUrl('http://localhost/[% &quot;genus&quot; %][% &quot;species&quot; %]')); myWV.show()" icon="" capture="0" type="1" name="Link"/>
    <actionsetting action="from PyQt4.QtCore import QUrl; from PyQt4.QtWebKit import QWebView;  myWV=QWebView(None);myWV.setWindowTitle('Wikipedia Link');myWV.load(QUrl('https://en.wikipedia.org/wiki/[% &quot;genus&quot; %]_[% &quot;species&quot; %]')); myWV.show()" icon="" capture="0" type="1" name="Wikipedia Page"/>
    <actionsetting action="from PyQt4.QtCore import QUrl; from PyQt4.QtWebKit import QWebView;  myWV=QWebView(None);myWV.setWindowTitle('Practical Plants Link');myWV.load(QUrl('http://practicalplants.org/wiki/[% &quot;genus&quot; %]_[% &quot;species&quot; %]')); myWV.show()" icon="" capture="0" type="1" name="Practical Plants Page"/>
  </attributeactions>
</qgis>
