import ROOT as r 
import ATLASStyle.AtlasStyle as AS
from array import array
import RootHelperFunctions as rhf 

"""

    
"""
class StyleOptions:
    def __init__(
        self,
        draw_options   = "",
        line_color     = r.kBlack,
        line_style     = 1,
        fill_color     = r.kWhite,
        fill_style     = 0,
        marker_color   = r.kBlack,
        marker_style   = 20,
        marker_size    = 0.045,
        legend_options = "l",
        y_divisions    = None,
        x_label_size   = None,
        y_label_size   = None,
        x_title_size    = None,
        x_title_offset = None,
        y_title_size   = None,
        y_title_offset = None,
        ):
        self.draw_options = draw_options
        self.line_color   = line_color  
        self.line_style   = line_style  
        self.fill_color   = fill_color  
        self.fill_style   = fill_style 
        self.marker_color = marker_color
        self.marker_style = marker_style
        self.marker_size  = marker_size
        self.legend_options = legend_options
        self.y_divisions    = y_divisions
        self.x_label_size   = x_label_size
        self.y_label_size   = y_label_size
        print "y_label_size = ", self.y_label_size
        self.x_title_size    = x_title_size
        self.x_title_offset = x_title_offset
        self.y_title_size   = y_title_size
        self.y_title_offset = y_title_offset


data_style_options = StyleOptions()
mc_style_options   = StyleOptions(
                                 draw_options = "E2 HIST",
                                 line_color   = r.kBlue,
                                 line_style   = 3,
                                 fill_color   = r.kWhite,
                                 fill_style   = 0,
                                 marker_color = r.kBlack,
                                 marker_style = 0,
                                 marker_size  = 0
                                 )
data_ratio_style_options = StyleOptions(
    y_divisions    = 503,
    x_label_size   = 0.15,
    y_label_size   = 0.15,
    x_title_size    = 0.15,
    x_title_offset = 0.82,
    y_title_size   = 0.15,
    y_title_offset = 0.45,
        )

def draw_migration_matrix(matrix):
    AS.SetAtlasStyle()
    r.gStyle.SetPadTopMargin(    0.05)
    r.gStyle.SetPadRightMargin(  0.15)
    r.gStyle.SetPadBottomMargin( 0.20)
    r.gStyle.SetPadLeftMargin(   0.15)
    r.gPad.Update()

    #nice green color 
    set_palette("green",99)
    matrix.Scale(100.0)
    matrix.SetMinimum(0.0)

    r.gStyle.SetPaintTextFormat("2.2f")
    if matrix.GetNbinsX() < 13 and matrix.GetNbinsY() < 13:
        matrix.Draw("COLZ TEXT")
    else:
        matrix.Draw("COLZ")
    # matrix.Scale(1.0/100.0)

    AS.ATLASLabel(  0.12, 0.96,  r.kBlack, 0.04*2.0, 0.04, "  Simulation Internal")        
    AS.myText    (  0.12, 0.92,r.kBlack,0.04, AS.lumi_string)    

def set_palette(name="palette", ncontours=999):
    """
    Set a color palette from a given RGB list
    - stops, red, green and blue should all be lists of the same length
    - see set_decent_colors for an example
    -
    """
 
    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    elif name == "green":
        stops = [0.000, 0.100, 0.700, 1.000]        
        red   = [1.000, 1.000, 0.476, 0.476]
        green = [1.000, 1.000, 0.760, 0.760]
        blue  = [1.000, 1.000, 0.476, 0.476]
    elif name == "blue":
        stops = [0.000, 0.100, 0.700, 1.000]
        red   = [1.000, 1.000, 0.476, 0.476]
        green = [1.000, 1.000, 0.476, 0.476]
        blue  = [1.000, 1.000, 0.760, 0.760]
    else:
        # default palette, looks cool
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]
 
    stops  = array('d', stops)
    red    = array('d', red)
    green  = array('d', green)
    blue   = array('d', blue)
 
    npoints = len(stops)
    r.TColor.CreateGradientColorTable(npoints, stops, red, green, blue, ncontours)
    r.gStyle.SetNumberContours(ncontours)

def set_style_options(hist,style_options):
    hist.SetMarkerStyle(style_options.marker_style  )
    hist.SetLineStyle(style_options.line_style  )
    hist.SetFillColor(style_options.fill_color  )
    hist.SetFillStyle(style_options.fill_style  )
    hist.SetMarkerColor(style_options.marker_color)
    # hist.SetMarkerSize(style_options.marker_size )
    if  style_options.y_divisions != None:
        hist .GetYaxis().SetNdivisions(style_options.y_divisions)   
    if  style_options.x_label_size != None:
        hist .GetXaxis().SetLabelSize(style_options.x_label_size) 
    if  style_options.x_title_size != None:
        hist .GetXaxis().SetTitleSize(style_options.x_title_size)
    if  style_options.x_title_offset != None:
        hist .GetXaxis().SetTitleOffset(style_options.x_title_offset)

    # 

    if  style_options.y_label_size != None:
        print "SETITNG y_label_size = ", style_options.y_label_size
        hist .GetYaxis().SetLabelSize(style_options.y_label_size)
    else: 
        print "NOT SETITNG y_label_size = ", style_options.y_label_size

    if  style_options.y_title_size != None:
        hist .GetYaxis().SetTitleSize(style_options.y_title_size)
    if  style_options.y_title_offset != None:
        hist .GetYaxis().SetTitleOffset(style_options.y_title_offset)
    return hist
 
def draw_atlas_details(labels,x_pos= 0.2,y_pos = 0.87, dy = 0.04,text_size = 0.035):
    AS.ATLASLabel(   x_pos,y_pos,1,dy*2.2,dy,"Simulation Internal")
    y_pos -= dy
    AS.myText(       x_pos,y_pos,1,dy,AS.lumi_string)
    y_pos -= dy
   
    for label in labels:
        AS.myText(       x_pos,y_pos,1,text_size, label )
        y_pos -= dy

def get_maximum_y(histograms):
    max_y = -1
    for name in histograms:
        if histograms[name][0].GetMaximum() > max_y:
            max_y = histograms[name][0].GetMaximum()
    return max_y


def create_legend(histograms):
    r.gStyle.SetFrameBorderSize(0)
    r.gStyle.SetLegendBorderSize(0)
    legend = r.TLegend(0.6,0.9-len(histograms)*0.05,0.9,0.9)
    legend.SetTextSize(0.045)
    legend.SetFillColor(0)
    legend.SetLineWidth(0)
    legend.SetFillStyle(0)
    legend.SetNColumns(1)

    print "len(histograms) = ",len(histograms)
    for name in histograms:
        print "ADDING LEGEND ENTRY: ",histograms[name][0],name,histograms[name][1].legend_options 

        legend.AddEntry(histograms[name][0],name,histograms[name][1].legend_options)

    return legend


def ratio_plot(canvas, histograms, denominator_hist_name = None):
    '''
        canvas: TCanvas that will be drawn upon
        histograms: an dictionary of tuples such that 
                    {
                     histogram_name: (histogram, style_options, ratio_style_options), 
                     histogram_2_name: (histogram_2, style_option_2, ratio_style_options_2),
                    }
                    style_otion is an instance of the above class StyleOptions, name is a string and histogram is a TH1F 
        denominator_hist_name: by default will take the first histogram in the dictionary, but if specificied will use the 
                               histogram with this variable's name in the ratio plot

        returns: a dictionary of ratio histograms such that
                 { 
                    histogram_name: [raito_histogram, ratio_style_options],
                    histogram_2_name: [raito_histogram, ratio_style_options_2]
                 }
    '''
    AS.SetAtlasStyle()
    r.gStyle.SetOptStat(0)
    
    #divide the canvas into 
    canvas.Clear()
    canvas.cd()
    pad1 =  r.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0)
    pad1.Draw()
    pad1.cd()

    # upper pannel 
    same_string = ""
    max_y       = get_maximum_y(histograms)*1.35
    for name in histograms: 
        #for clarity cache the histogram and styling options separately
        hist = histograms[name][0]
        style_opts = histograms[name][1]

        #format the histograms into nice lookign things 
        hist = set_style_options(hist,style_opts)
        hist.SetMaximum(max_y)

        hist.Draw(style_opts.draw_options + same_string)
        same_string = " SAME "

    draw_atlas_details( ["Combined regions"] )
    legend = create_legend(histograms)
    legend.Draw("same")

    # lower pannel for ratio 
    canvas.cd()
    pad2 = r.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.285)
    pad2.Draw()
    pad2.cd()

    #we want to use the first element in the dictionary if the denominator_hist_name is not set by the user
    if denominator_hist_name == None:
        denominator_hist_name = next(iter(histograms))


    #first evaluate the ratio plots and determine the maximum and minimum y 
    ratio_hists,  min_y,max_y = rhf.evaluate_ratio_histograms( histograms, denominator_hist_name )
    max_y = max(max_y*1.3, 2.0 - min_y*1.3)
    min_y = 2.0 - max_y 

    same_string = ""
    for name in ratio_hists: 
        #we don't want to draw the default straight line at one coloured in whatever style has been chosen for the denom. 
        if name == denominator_hist_name:
            continue 

        #separate out the histogram and style options 
        ratio_histogram = ratio_hists[name][0]
        ratio_style_opts = histograms[name][1] #evaluate_ratio_histograms has already removed the unwanted sytyle opions for the upper pannel
        
        #format the histogram
        ratio_histogram.SetMaximum(max_y) 
        ratio_histogram.SetMinimum(min_y) 

        print "SETTING RATIO STYLE OPTIONS: ", ratio_style_opts
        ratio_hists[name][0] = ratio_histogram = set_style_options(ratio_histogram,ratio_style_opts)
        print "Drawing ",ratio_histogram, "..."
        print "Setting max to ", max_y
        print "Setting min to ", min_y

        #draw the histogram keeping track of what is the same
        ratio_histogram.Draw(style_opts.draw_options + same_string)
        same_string = " SAME "
    legend.Draw("same")

    return ratio_hists 



