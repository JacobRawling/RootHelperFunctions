import ROOT as r 
import sys
import array

def open_file(file_name, option="READ" ):
    f = r.TFile(file_name,option)
    assert f, ("ERROR: failed to open file: ",file_name)
    return f

#
# Draws a 1D histogram histogram using TTree::Daw
def get_histogram(file_name_list,ntuple_name, variable_name,x_axis_binning,weight,scale = 1.0, draw_options = "e" ):
    chain = r.TChain(ntuple_name)

    # Support both a list of files and an invidiual file
    if isinstance(file_name_list, list):
        for file in file_list:
            chain.Add(file)
    else:
        chain.Add(file_name_list)
    r.TH1.SetDefaultSumw2()

    if isinstance(x_axis_binning,list) == True: 
        htemp = r.TH1F("htemp","",len(x_axis_binning)-1,array.array('d',x_axis_binning))
        chain.Draw(variable_name+">>htemp", weight, draw_options)
    else:
        chain.Draw(variable_name+">>htemp("+x_axis_binning+")", weight, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = r.gDirectory.Get("htemp")
    assert isinstance(htemp,r.TH1F),( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp

#
# Draws a 2D histogram histogram using TTree::Daw 
def get_2d_histogram(file_name_list,
                     ntuple_name, 
                     variable_name,
                     x_axis_binning,
                     y_axis_binning,
                     weight,
                     scale = 1.0,
                     friend_name = None,
                     index_variable = None, 
                     draw_options = "" ):
    
    chain = r.TChain(ntuple_name)

    # Support both a list of files and an invidiual file
    if isinstance(file_name_list, list):
        for file in file_list:
            chain.Add(file)
    else:
        chain.Add(file_name_list)
    r.TH1.SetDefaultSumw2()

    # Check to see if the user is attempting to access variables from a friended tree 
    if friend_name != None:
        assert index_variable != None,"ERROR: index_variable must be set when using a friend tree"

        friend_chain = r.TChain(friend_name)
        if isinstance(file_name_list, list):
            for file in file_list:
                friend_chain.Add(file)
        else:
            friend_chain.Add(file_name_list)

        friend_chain.BuildIndex(index_variable)
        chain.BuildIndex(index_variable)
        chain.AddFriend(friend_chain)

    #are we handing lists as binning or text ? 
    variable_binning_x = not isinstance(x_axis_binning,str)
    variable_binning_y = not isinstance(y_axis_binning,str)
    weight += "(" + index_variable + " == " + friend_name + "." + index_variable + ")"

    if variable_binning_x or variable_binning_y: 
        htemp = r.TH2F("htemp","",len(x_axis_binning)-1,array.array('d',x_axis_binning),len(y_axis_binning),array.array('d',y_axis_binning))
        chain.Draw(variable_name+">>htemp", weight, draw_options)
    else:
        chain.Draw(variable_name+">>htemp("+x_axis_binning+")", weight, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = r.gDirectory.Get("htemp")
    assert isinstance(htemp,r.TH2F) or isinstance(htemp,r.TProfile) ,( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp

#Remove unaccetable characters frmo a string - basic sanitization
def clean_string(cleaning_string):
    cleaning_string = cleaning_string.replace("'","")
    cleaning_string = cleaning_string.replace("(","")
    cleaning_string = cleaning_string.replace(")","")
    cleaning_string = cleaning_string.replace("[","")
    cleaning_string = cleaning_string.replace("]","")
    cleaning_string = cleaning_string.replace("~","")
    cleaning_string = cleaning_string.replace("!","")
    cleaning_string = cleaning_string.replace("%","")
    cleaning_string = cleaning_string.replace("^","")
    cleaning_string = cleaning_string.replace("*","")
    return cleaning_string

