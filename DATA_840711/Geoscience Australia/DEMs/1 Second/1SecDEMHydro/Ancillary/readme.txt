
1 second SRTM Level 2 Derived Digital Elevation Models (DEM, DEM-S, DSM) Version 1.0

ANZLIC metadata:  ANZCW0703013336 (DSM)
ANZLIC metadata:	ANZCW0703013355 (DEM)
ANZLIC metadata:  ANZCW0703014016 (DEM-S)

****Volume Label****

1secSRTM2_DSM_DEM_DEM-Sv1.0

****Root Directory****

1secSRTM2_DSM_DEM_DEM-Sv1.0             <DIR>
    
    DEM				   <DIR>

	Mosaic			   <DIR>
	   dem1sv1_0		   ESRI GRID - national DEM mosaic (may not be included on drive due to limited file space).

	Tiles				   <DIR>
         e113s22dem1_0           Continuous 32 bit Floating Point ESRI GRIDs representing 1 degree tiles for the DEM - Grids are named per the latitude and longitude of the south west corner 
         e113s23dem1_0
         .
         .
         .
         e153s32dem1_0

    DEM-S				   <DIR>

	Mosaic			   <DIR>
	   dems1sv1_0		   ESRI GRID - national smoothed DEM mosaic.

	Tiles				   <DIR>
         e113s22dems             Continuous 32 bit Floating Point ESRI GRIDs representing 1 degree tiles for the smoothed DEM - Grids are named per the latitude and longitude of the south west corner 
         e113s23dems
         .
         .
         .
         e153s32dems

    DSM				   <DIR>
	
	Mosaic			   <DIR>
	   dsm1sv1_0		   ESRI GRID - national DSM mosaic (may not be included on drive due to limited file space).

	Tiles				   <DIR>
         e113s22dsm1_0           Continuous 32 bit Floating Point ESRI GRIDs representing 1 degree tiles for the DSM - Grids are named per the latitude and longitude of the south west corner 
         e113s23dsm1_0
         .
         .
         .
         e153s32dsm1_0

    
    ReferenceData
	Masks                      <DIR>
    
        DestripedTiles           <DIR>
            ds_tiles             ESRI GRID - A de-stripe mask indicating which ¼ x ¼ degree tiles have been affected by de-striping and which have not been de-striped 
        
        MaxDestripe              <DIR>
            max_destripe         ESRI GRID - A striping magnitude layer showing the amplitude of the striping at 1 km resolution
        
        Voids                    <DIR>
            voids                ESRI GRID - A void mask showing cells that were no-data in the raw SRTM and have been filled using the void filling algorithm
        
        Water                    <DIR>
            water                ESRI GRID - A water mask at 1 second resolution showing the cells that are part of the flattened water bodies

	TileIndexes			   <DIR>
	  DEM_TileIndex		   ESRI Shape - Index of DEM tiles
	  DEMS_TileIndex		   ESRI Shape - Index of DEM-S tiles
	  DSM_TileIndex		   ESRI Shape - Index of DSM tiles
  
    	VegetationInfo		   <DIR>
	  VegOffsetRemoved	   <DIR>
		e113s22vor		   ESRI GRIDs - difference surface showing the vegetation offset that has been removed (from DEM tiles only)
		e113s23vor		   
		.
		.
		e153232vor

	  QAVegPoly			   ESRI Shape - Polygons identifying specific areas of imperfection in the vegetation offset removal
	  VegEdgeLines		   ESRI Shape - Lines identifying where discontinuities are visible at the edge of tiles
	  VegRemoval		   ESRI Shape - Polygons forming a 1/8 x 1/8 degree grid recording where vegetation effects were removed and where imperfections in that removal were noted

    availability.txt         	   				Standard Geoscience Australia availability statement
    copyright.txt            	   				Standard Geoscience Australia copyright statement
    publication.txt          	  				Standard Geoscience Australia publication statement
    quality.txt              	   				Standard Geoscience Australia quality statement
    readme.txt               	   				This file
    1secSRTM2_DEMs_UserGuide.pdf  				1 second SRTM Derived Digital Elevation Models v1.0 User Guide (also contains ANZLIC metadata and 3 second derived products)
    1secSRTM2_CoverLetter&Licence.pdf			1 second SRTM Cover Letter and Licence (restricted to government use only)


