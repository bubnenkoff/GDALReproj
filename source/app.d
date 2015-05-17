import std.stdio;
import std.file;
import std.string;
import std.algorithm;
import std.path;
import std.file;
import std.regex;
import std.conv;
import core.stdc.stdlib;

import gdal;

pragma(lib, "libgdal-1");

void main(string [] args)
{
  string inputImage = getcwd ~ `\imgs\201409241332_NGT.jpg`;
  if (!inputImage.exists)
  {
    writeln("File Do not Exist");
    return;
  }
  openTiff(inputImage);


}


void openTiff(string inputImage)
{

  string outputImage = getcwd ~ `\imgs\out.tif`;

  GDALDatasetH  hSrcDS, hDstDS;
  GDALAllRegister();

  hSrcDS = GDALOpen( toStringz(inputImage), GDALAccess.GA_ReadOnly );
  hDstDS = GDALOpen( toStringz(outputImage), GDALAccess.GA_Update );
 
  GDALWarpOperation.GDALWarpOptions psWarpOptions = GDALCreateWarpOptions();
  
  //writeln(inputImage.baseName, " has ", num_bands, " bands and is [", x_size, "square_in_km2", y_size, "]");
  //GDALClose( hDataset );


}