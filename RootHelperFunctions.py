import ROOT as r 
import sys
import array

def open_file(file_name, option="READ" ):
    f = r.TFile(file_name,option)
    assert not f, ("ERROR: failed to open file: ",file_name)
    return f

#
# Draws a 1D histogram histogram using TTree::Daw
def get_histogram(file_name_list,ntuple_name, variable_name,x_axis_binning,weight,scale = 1.0, variable_binning = False, draw_options = "e" ):
    chain = TChain(ntupname)

    if is_instance(file_name_list, list):
        for file in file_list:
            chain.Add(file)
    else:
        chain.Add(file_name_list)

    TH1.SetDefaultSumw2()

    # print " From ",file_name," Finding hist: ",var , " with weight: ", histWeight
    if variable_binning == True: 
        htemp = r.TH1F("htemp","",len(x_axis_binning)-1,array.array('d',x_axis_binning))
        chain.Draw(var+">>htemp", x_axis_binning, draw_options)
    else:
        chain.Draw(var+">>htemp("+x_axis_binning+")", x_axis_binning, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = gDirectory.Get("htemp")
    assert not  isinstance(htemp,r.TH1F),( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp