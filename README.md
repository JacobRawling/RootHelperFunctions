# RootHelperFunctions

A set of tools designed to make working in PyRoot easier.

## RootHelperFunctions

These tools all have the purpose of manipulating root objects into different forms, or applying transformations on these objects. For instance get_histogram is an abstraction of Ttree::Draw, just neatened up a bit, with appropraite error checking to ensure that histogram is returned. 

## DrawingHelperFunctions

These tools are designed to make plotting journal ready plots easy. The StyleOptions class contains all the necesasry settings to foramt histograms nicely. This is primarily used interanlly to functions within DrawingHelperFunctions.

Two default style options are set up:
 data_style_options: formatted to show a filled in black circle for the data point 
 mc_style_options: formatted to show a blue dashed line 

ratio_plot and plot_histogram are the workhorses of this toolkit

## StringHelperFunctions

Used for sanatizing strings and any manipulation that is commonly needed in a ROOT based analysis. 

##ReweightingTool

Constructs a formula string that can be attached to weight in a TTree::Draw command to add an event-by-event slope into a distribution. 




