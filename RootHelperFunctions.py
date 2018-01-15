import ROOT as r 
import sys
import array
import os 
from math import sqrt

def open_file(file_name, option="READ" ):
    f = r.TFile(file_name,option)
    assert f, ("ERROR: failed to open file: ",file_name)
    return f

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_up_down_uncert_to_asymmerrors(up_hist,down_hist,y_centre=1.0):
    x,y,exl,eyl,exh,eyh = array.array('d'),array.array('d'),array.array('d'),array.array('d'),array.array('d'),array.array('d')
    for i in xrange(up_hist.GetSize()):
        x.append(up_hist.GetBinCenter(i))
        y.append(y_centre)
        exl.append(up_hist.GetBinWidth(i)/2.0)
        exh.append(up_hist.GetBinWidth(i)/2.0)
        eyh.append(up_hist.GetBinContent(i))
        eyl.append(down_hist.GetBinContent(i))

    graph = r.TGraphAsymmErrors(len(x),x,y,exl,exh,eyl,eyh)
    return graph



def poisson_fluctuate(hist,random_generator):
    new_hist = hist.Clone()
    for i in range(0, hist.GetNbinsX() + 1):
        old_bin_error = 0
        if not hist.GetBinContent(i) == 0:
            #old_bin_error = hist.GetBinError(i)/hist.GetBinContent(i) ###you probably don't need this
            new_hist.SetBinContent(i, random_generator.Poisson(hist.GetBinContent(i)))
    return new_hist

#
# Draws a 1D histogram histogram using TTree::Daw
def get_histogram(file_name_list,ntuple_name, variable_name,x_axis_binning,weight,scale = 1.0, draw_options = "e", hist_name = "htemp", friend_name = None,
                     index_variable = None ):
    r.gROOT.SetBatch()
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
        friend_chain.AddFriend(chain)

        
    if isinstance(x_axis_binning,list) == True: 
        htemp = r.TH1F(hist_name,"",len(x_axis_binning)-1,array.array('d',x_axis_binning))
        chain.Draw(variable_name+">>"+hist_name+"", weight, draw_options)
    else:
        chain.Draw(variable_name+">>"+hist_name+"("+x_axis_binning+")", weight, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = r.gDirectory.Get(hist_name)
    assert isinstance(htemp,r.TH1F),( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp

def get_histogram_with_chains(chain,variable_name,x_axis_binning,weight,scale = 1.0, draw_options = "e", hist_name = "htemp" ):
    r.gROOT.SetBatch()        

    if isinstance(x_axis_binning,list) == True: 
        htemp = r.TH1F(hist_name,"",len(x_axis_binning)-1,array.array('d',x_axis_binning))
        chain.Draw(variable_name+">>"+hist_name+"", weight, draw_options)
    else:
        chain.Draw(variable_name+">>"+hist_name+"("+x_axis_binning+")", weight, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = r.gDirectory.Get(hist_name)
    assert isinstance(htemp,r.TH1F),( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp
#
# Draws a 2D histogram histogram using TTree::Daw 
#
# Note: Suggest always setting histname to avoid battling ROOTs memory management system
def get_2d_histogram(file_name_list,
                     ntuple_name, 
                     variable_name,
                     x_axis_binning,
                     y_axis_binning,
                     weight,
                     scale = 1.0,
                     friend_name = None,
                     index_variable = None, 
                     draw_options = "",
                     hist_name    = "htemp"):
    r.gROOT.SetBatch()
        
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
    weight += "*(" + index_variable + " == " + friend_name + "." + index_variable + ")"

    if variable_binning_x and variable_binning_y: 
        htemp = r.TH2F(hist_name,"",len(x_axis_binning)-1,array.array('d',x_axis_binning),len(y_axis_binning)-1,array.array('d',y_axis_binning))
        chain.Draw(variable_name+">>"+hist_name+"", weight, draw_options)
    else:
        chain.Draw(variable_name+">>"+hist_name+"("+x_axis_binning+","+y_axis_binning+")", weight, draw_options)

    #retrive the histogram from ROOT and free it from this instance in memory 
    htemp = r.gDirectory.Get(hist_name)
    assert isinstance(htemp,r.TH2F) or isinstance(htemp,r.TProfile) ,( "ERROR: Failed to open get histogram with variable expression",variable," from files", file_list," is type ",type(htemp))
    htemp.SetDirectory(0)

    #let's the user rescale    
    htemp.Scale(scale)
    return htemp

def normalize_histogram(hist, correct_uncert = False):
    integral = hist.Integral()
    if integral == 0:
        integral = 1
    hist.Scale(1.0/integral)

    if correct_uncert:
        for i in xrange(1,hist.GetSize()):
            # hist.SetBinContent(i, hist.GetBinContent(i)/integral)
            hist.SetBinError(i, (hist.GetBinError(i)/integral ) )

    return hist

def extract_errors_to_hist(hist):
    """
        Takes the  uncertainty on each bin and sets them as the bin content
        of the error_hist
    """
    error_hist = hist.Clone()
    error_hist.SetDirectory(0)

    for i in xrange(1, hist.GetSize()):
        error_hist.SetBinContent(i,hist.GetBinError(i))
        error_hist.SetBinError(i,0)

    return error_hist 

def normalize_migration_matrix(migration_matrix):
    n_cols = migration_matrix.GetXaxis().GetNbins()

    for j in range(1,migration_matrix.GetYaxis().GetNbins()+1):
         norm = migration_matrix.Integral(0,n_cols,j,j)

         #protectiong against zero particle level events in a row
         if norm == 0:
             norm = 1.0

         for i in range(1,migration_matrix.GetXaxis().GetNbins()+1):
             migration = migration_matrix.GetBinContent(i,j)
             migration *= 1.0/norm
             migration_matrix.SetBinContent(i,j,migration)
    return migration_matrix

def times_by_bin_center(hist):
    hist = hist.Clone()
    hist.SetDirectory(0)
    for i in xrange(0,hist.GetSize()):
        hist.SetBinContent(i,hist.GetBinContent(i)*hist.GetBinCenter(i))
    return hist

def remove_errors(hist):
    hist = hist.Clone()
    hist.SetDirectory(0)
    for i in xrange(0,hist.GetSize()):
        hist.SetBinError(i,0)
    return hist

def hide_root_infomessages():
    r.gErrorIgnoreLevel = 1001#r.kPrint

def evaluate_ratio_histogram(numerator_hist,denonimator_hist):
    ratio_hist = numerator_hist.Clone("ratio_"+numerator_hist.GetName())
    ratio_hist.Divide(denonimator_hist)
    ratio_hist.SetDirectory(0)
    return ratio_hist

def shift_hist_yaxis(hist, amount):
    shifted_hist = hist.Clone()
    for i in xrange(1,shifted_hist.GetSize()):
        shifted_hist.SetBinContent(i,shifted_hist.GetBinContent(i)+amount)
    shifted_hist.SetDirectory(0)
    return shifted_hist

def bin_by_bin_divide_histogram(numerator_hist,denonimator_hist):
    ratio_hist = numerator_hist.Clone("ratio_"+numerator_hist.GetName())
    for i in xrange(1, numerator_hist.GetSize()):
        try:
            new_content = numerator_hist.GetBinContent(i)/denonimator_hist.GetBinContent(i)
        except ZeroDivisionError:
            new_content = 0.0

        ratio_hist.SetBinContent(i,new_content )

    ratio_hist.SetDirectory(0)
    return ratio_hist

def GetQuantiles(hist,quants):
    """ 
        takes a LIST of quantiles and returns an array of the corresponding x coordinates 
        of the input histogram hist
    """
    quants = array.array('d', [ quant for quant in quants])
    q = array.array('d', [0.0]*len(quants))
    hist.GetQuantiles(len(quants), q, quants)
    return q

def combine_bincenters_in_quadrature(hists):
    combination = hists[0].Clone()

    for i in xrange(1,combination.GetSize()):
        total = 0.0
        for h in hists:
          total += h.GetBinContent(i)**2

        total = sqrt(total)
        combination.SetBinContent(i,total)
        combination.SetBinError(i,0)
    combination.SetDirectory(0)
    return combination

def clear_histogram(hist):
    for i in xrange(0,hist.GetSize()):
        hist.SetBinContent(i,0)
        hist.SetBinError(i,0)
    return hist

def apply_stress(hist,stress):
    """
        Stresses a distribution, such that the first bin is increased by a factor 1, and the last by 1 + stress
    """
    stressed_hist = hist.Clone()
    stressed_hist.SetDirectory(0)
    
    n_bins = hist.GetSize()
    for i in xrange(1,n_bins):
        stressed_hist.SetBinContent(i, hist.GetBinContent(i)*(1.0 + stress*float(i)/float(n_bins) ))

    return stressed_hist

def evaluate_ratio_histograms(histograms ):
    '''
        brief: turns a dictionary of histograms and key for the denominator histogram into a dictionary of ratio plots 
    
        histograms: an dictionary of tuples such that 
                    {
                     histogram_name: (histogram, style_options, ratio_style_options, ratio_hist_string), 
                     histogram_2_name: (histogram_2, style_option_2, ratio_style_options_2, ratio_hist_string),
                    }
                    style_otion is an instance of the above class StyleOptions, name is a string and histogram is a TH1F 
                    ratio_hist_string is the name of the histogram to divide this one by, if it's None then the histogram is not added to the returned histograms
    
    '''      
    ratio_hists = {}
    
    max_y,min_y = -1e5, 1e5
    for name in histograms: 
        #we don't ever want to evaluate this straight line at y=1.
        denominator_hist_name =  histograms[name][3] 
        if denominator_hist_name == None:
            continue

        #ensure we've given sensible parameter to this function 
        assert denominator_hist_name in histograms, "ERROR: Denominator histogram '"+denominator_hist_name+"'' not in input dictioanry."
        denominator_hist = histograms[denominator_hist_name][0] 
    
        numerator_hist    = histograms[name][0] 
        ratio_style_opts  = histograms[name][2] 
    
        ratio_hists[name] = []
        r_plot = evaluate_ratio_histogram(numerator_hist,denominator_hist)
        r_plot.SetDirectory(0)

        max_y = max(r_plot.GetMaximum(),max_y)
        min_y = min(r_plot.GetMinimum(),min_y)

        ratio_hists[name].append( r_plot)
        ratio_hists[name].append( ratio_style_opts)
    
    return ratio_hists, max_y,min_y

def shift_bins(hist, shift_index):
    """
        brief: sequentially moves the all the bins and lables from shift index to 1

        params: 
            - hist: TH1 histograms
            - shift_index: Starting index of bin that shall be moved.
    """

    #create acopy and free it from ROOT's memory managemnet 
    hist = hist.Clone()
    hist.SetDirectory(0)

    # 
    for i in xrange(1,hist.GetSize()-1):
        if i + shift_index <= hist.GetSize()-1:
            # we want to move bins if possible
            new_label   = hist.GetXaxis().GetBinLabel(i+shift_index)
            new_content = hist.GetBinContent(i+shift_index)

            hist.GetXaxis().SetBinLabel(i, new_label)
            hist.SetBinContent(i, new_content)
        else:
            #otherwise, just remove the lable and set the content to zero
            hist.SetBinContent(i,0)
            hist.GetXaxis().SetBinLabel(i,"")

    return hist

