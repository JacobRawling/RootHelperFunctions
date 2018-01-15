import ROOT as r 
import ATLASStyle.AtlasStyle as AS
from array import array
import RootHelperFunctions as rhf 
from copy import deepcopy
import math 
from collections import OrderedDict

"""
    StyleOptions for a histogram not including the titles of the histogram, this allows the same style options to be used for histograms 
    showing data from the same source, but of a different type (e.g different MC generators showing different variables)

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
        line_width     = 2,
        legend_options = "l",
        y_divisions    = None,
        x_label_size   = None,
        x_title_size   = 0.35,
        x_title_offset = None,
        x_axis_label_offset = None,
        y_axis_label_offset = None,
        y_label_size   = 0.05,
        y_title_size   = 0.05,
        y_title_offset = 1.1,
        x_axis_label_color = r.kBlack
        ):

        self.draw_options = draw_options
        self.line_color   = line_color  
        self.line_style   = line_style  
        self.fill_color   = fill_color  
        self.fill_style   = fill_style 
        self.line_width   = line_width
        self.marker_color = marker_color
        self.marker_style = marker_style
        self.marker_size  = marker_size
        self.legend_options = legend_options
        self.y_divisions    = y_divisions
        self.x_label_size   = x_label_size
        self.y_label_size   = y_label_size
        self.x_title_size    = x_title_size
        self.x_title_offset = x_title_offset
        self.y_title_size   = y_title_size
        self.y_title_offset = y_title_offset
        self.x_axis_label_offset = x_axis_label_offset
        self.y_axis_label_offset = y_axis_label_offset
        self.x_axis_label_color = x_axis_label_color

    def set_default_ratio_options(self):
        self.y_divisions    = 503
        self.y_label_size   = 0.135
        self.y_title_size   = 0.135
        self.y_title_offset = 0.45
        self.x_label_size   = 0.135
        self.x_title_size    = 0.135
        self.x_title_offset = 0.87
        self.x_axis_label_offset = 0.87
        self.y_axis_label_offset = None
        self.draw_options="HIST"

data_style_options = StyleOptions(x_label_size = 0.0,
                                  draw_options = "HIST P",
                                  legend_options = "lp")
mc_style_options   = StyleOptions(
                                 draw_options = "HIST",
                                 line_color   = r.kBlue,
                                 line_style   = 3,
                                 fill_color   = r.kWhite,
                                 fill_style   = 0,
                                 marker_color = r.kBlack,
                                 marker_style = 0,
                                 marker_size  = 0,
                                 x_label_size = 0.0
                                 )
data_ratio_style_options = StyleOptions(
    y_divisions    = 503,
    y_label_size   = 0.135,
    y_title_size   = 0.135,
    y_title_offset = 0.45,
    x_label_size    = 0.135,
    x_title_size    = 0.135,
    x_title_offset  = 0.87,
    x_axis_label_offset = 0.87,
    y_axis_label_offset = None,
    draw_options="HIST"
    )

mc_ratio_style_options = StyleOptions(
    y_divisions    = 503,
    y_label_size   = 0.135,
    y_title_size   = 0.135,
    y_title_offset = 0.45,
    x_label_size   = 0.135,
    x_title_size    = 0.135,
    x_title_offset = 0.87,
    x_axis_label_offset = 0.87,
    y_axis_label_offset = None,
    draw_options="HIST",
    line_color   = r.kBlue,
    line_style   = 3,
    fill_color   = r.kWhite,
    fill_style   = 0,
    marker_color = r.kBlack,
    marker_style = 0,
    marker_size  = 0,
    )


def get_unfolded_mc_stlye_opt(count, is_ratio,line_style = 1):
        colors = [r.kBlack,r.kRed-4, r.kRed, r.kGreen + 3, r.kGreen - 3, r.kAzure -2, r.kAzure +2, r.kMagenta -2, r.kMagenta+2]
        markers = [34,20,24,21,25,22,26,23,32]


        unfolded_mc_style_options = StyleOptions(
                                                    draw_options = "HIST P",
                                                    x_label_size = 0.0,
                                                    legend_options = "lp")
        unfolded_mc_style_options.marker_style = markers[count]
        unfolded_mc_style_options.marker_color = colors[count]
        unfolded_mc_style_options.line_color   = colors[count]

        if not is_ratio:
           return unfolded_mc_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        unfolded_mc_ratio_style_options = StyleOptions(x_label_size = 0.0,
                                                    line_style = line_style,
                                                    legend_options = "lp",
                                                    marker_style = markers[count],
                                                    marker_color = colors[count],
                                                    line_color = colors[count],
                                                    line_width   = 4,)
        unfolded_mc_ratio_style_options.set_default_ratio_options()
        unfolded_mc_ratio_style_options.x_axis_label_offset = None
        return unfolded_mc_ratio_style_options

def get_truth_stlye_opt(count, is_ratio,line_style = 1):
        #set the drawing style options options to be nice 
        colors = [r.kBlack,r.kRed-4, r.kRed, r.kGreen + 3, r.kGreen - 3, r.kAzure -2, r.kAzure +2, r.kMagenta -2, r.kMagenta+2]

        markers = [34,20,24,21,25,22,26,23,32]
        truth_style_options= StyleOptions(
                             draw_options = "HIST",
                             line_style   = line_style,
                             line_width   = 4,
                             fill_color   = r.kWhite,
                             fill_style   = 0,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size = 0.0,
                             legend_options = None,
                             line_color = colors[count] 
                             )
        if not is_ratio:
            return truth_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_ratio_style_options=deepcopy(truth_style_options)
        truth_ratio_style_options.set_default_ratio_options()
        truth_ratio_style_options.x_axis_label_offset = None
        return truth_ratio_style_options

def get_truth_legend_stlye_opt(count, is_ratio,line_style = 1):
        colors = [r.kBlack,r.kRed-4, r.kRed, r.kGreen + 3, r.kGreen - 3, r.kAzure -2, r.kAzure +2, r.kMagenta -2, r.kMagenta+2]
        markers = [34,20,24,21,25,22,26,23,32]

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "HIST",
                             line_style   = line_style,
                             line_width   = 4,
                             fill_color   = r.kWhite,
                             fill_style   = 0,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size = 0.0,
                             line_color = colors[count] 
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options

def get_truth_large_legend_stlye_opt(count, is_ratio,show_legend = True):
        line_style = count%2 + 1 
        colors = [r.kRed-4, r.kRed, r.kGreen + 3, r.kGreen - 3, r.kAzure -2, r.kAzure +2, r.kMagenta -2, r.kMagenta+2]
        max_count = len(colors)
        markers = [34,20,24,21,25,22,26,23,32]
        if math.floor(count/max_count) > 0:
            line_style += int(math.floor(count/max_count))*2

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "HIST",
                             line_style   = line_style,
                             line_width   = 4,
                             fill_color   = r.kWhite,
                             fill_style   = 0,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size   = 0.05,
                             x_title_size   = 0.05,
                             x_title_offset = 1.25,
                             y_title_offset = 1.45,
                             legend_options = "l" if show_legend else None,
                             line_color = colors[count%max_count] 
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options

def get_uncert_stlye_opt(is_ratio = False, show_legend = True ):

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "HIST",
                             line_style   = 1,
                             line_width   = 0,
                             fill_color   = r.kGray,
                             fill_style   = 1001,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size   = 0.05,
                             x_title_size   = 0.05,
                             x_title_offset = 1.25,
                             y_title_offset = 1.45,
                             legend_options = "f" if show_legend else None,
                             line_color = r.kGray
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options


def get_stat_syst_stlye_opt(is_ratio = False, show_legend = True,show_border=False ):

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "HIST",
                             line_style   = 1,
                             line_width   = 4 if show_border else 0,
                             fill_color   = 18, # a light gray
                             line_color   = r.kBlack,
                             fill_style   = 1001,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size   = 0.05,
                             x_title_size   = 0.05,
                             x_title_offset = 1.25,
                             y_title_offset = 1.45,
                             legend_options = "f" if show_legend else None,
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options


def get_uncert_graph_stlye_opt(is_ratio = False, show_legend = True, show_border  = True ):

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "5",
                             line_style   = 0,
                             line_width   = 4 if show_border else 0,
                             fill_color   = r.kGray,
                             line_color   = r.kBlack,
                             fill_style   = 1001,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size   = 0.05,
                             x_title_size   = 0.05,
                             x_title_offset = 1.25,
                             y_title_offset = 1.45,
                             legend_options = "f" if show_legend else None,
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options

def get_stat_syst_graph_stlye_opt(is_ratio = False, show_legend = True, show_border = True ):

        #set the drawing style options options to be nice 
        truth_leg_style_options= StyleOptions(
                             draw_options = "5",
                             line_style   = 1,
                             line_width   = 4 if show_border else 0,
                             fill_color   = 18,
                             line_color   = r.kBlack,
                             fill_style   = 1001,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             x_label_size   = 0.05,
                             x_title_size   = 0.05,
                             x_title_offset = 1.25,
                             y_title_offset = 1.45,
                             legend_options = "f" if show_legend else None,
                             )
        if not is_ratio:
            return truth_leg_style_options

        #ratio is basically the same except the label sizes and things are changed a bit 
        truth_leg_ratio_style_options=deepcopy(truth_leg_style_options)
        truth_leg_ratio_style_options.set_default_ratio_options()
        truth_leg_ratio_style_options.x_axis_label_offset = None
        return truth_leg_ratio_style_options

def draw_migration_matrix(matrix,canvas):
    canvas.cd()
    canvas.Clear()

    AS.SetAtlasStyle()
    canvas.SetTopMargin(    0.1)
    canvas.SetRightMargin(  0.15)
    canvas.SetBottomMargin( 0.15)
    canvas.SetLeftMargin(   0.15)

    #
    matrix.GetYaxis().SetTitleSize(0.035)
    matrix.GetYaxis().SetLabelSize(0.035)
    matrix.GetXaxis().SetTitleSize(0.035)
    matrix.GetXaxis().SetLabelSize(0.035)
    matrix.GetZaxis().SetTitleSize(0.035)
    matrix.GetZaxis().SetLabelSize(0.035)

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

    AS.ATLASLabel(  0.15, 0.96,  r.kBlack, 0.04*2.0, 0.04, "  Simulation Internal")        
    AS.myText    (  0.15, 0.92,r.kBlack,0.04, AS.lumi_string)    

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
    
    if style_options.fill_style != None:
        hist.SetFillStyle(style_options.fill_style  )
    
    hist.SetMarkerColor(style_options.marker_color)
    hist.SetLineColor(style_options.line_color)
    hist.SetLineWidth(style_options.line_width)
    
    #For all the default options that aren't none we need to check if they're set
    #and update the histogram accordingly 
    if  style_options.y_divisions != None:
        hist .GetYaxis().SetNdivisions(style_options.y_divisions)   
    if  style_options.x_label_size != None:
        hist .GetXaxis().SetLabelSize(style_options.x_label_size) 
    if  style_options.x_title_size != None:
        hist .GetXaxis().SetTitleSize(style_options.x_title_size)
    if  style_options.x_title_offset != None:
        hist .GetXaxis().SetTitleOffset(style_options.x_title_offset)

    if  style_options.x_axis_label_offset != None:
        hist.GetXaxis().SetLabelOffset(style_options.x_axis_label_offset)

    if  style_options.y_label_size != None:
        hist .GetYaxis().SetLabelSize(style_options.y_label_size)
    if  style_options.y_title_size != None:
        hist .GetYaxis().SetTitleSize(style_options.y_title_size)
    if  style_options.y_title_offset != None:
        hist .GetYaxis().SetTitleOffset(style_options.y_title_offset)
    if  style_options.y_axis_label_offset != None:
        hist.GetYaxis().SetLabelOffset(style_options.y_axis_label_offset)
    if style_options.x_axis_label_color != None:
        hist.GetXaxis().SetLabelColor(style_options.x_axis_label_color)
    return hist
 
def draw_bold_title_detials( bold_label, sub_label, labels= [], x_pos=0.2,y_pos=0.87,dy=0.04,text_size =0.035,dr = 0.04*3.5):
    AS.BoldLabel(   x_pos,y_pos,1,dr,dy,bold_label,sub_label)
    y_pos -= dy   
    for label in labels:
        AS.myText(       x_pos,y_pos,1,text_size, label )
        y_pos -= dy

def draw_atlas_details(labels=[],x_pos= 0.2,y_pos = 0.87, dy = 0.045,text_space=None,text_size = 0.04):
    if text_space == None:
        AS.ATLASLabel(   x_pos,y_pos,1,dy*3.2,dy,"Simulation Internal")
    else:
        AS.ATLASLabel(   x_pos,y_pos,1,text_space,dy,"Simulation Internal")
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

def get_minimum_y(histograms):
    min_y = 1000000000000
    for name in histograms:
        if histograms[name][0].GetMinimum() < min_y:
            min_y = histograms[name][0].GetMinimum()
    return min_y

def create_legend(histograms, y_pos = 0.925,additional_entry_sizes=0):
    r.gStyle.SetFrameBorderSize(0)
    r.gStyle.SetLegendBorderSize(0)
    r.gStyle.SetLegendFont(42)
    n_leg = additional_entry_sizes
    for name in histograms:      
        if histograms[name][1].legend_options != None:
            n_leg += 1
    if n_leg > 4 and n_leg <= 8:
        legend = r.TLegend(0.55,y_pos-(n_leg/2.0)*0.05,y_pos,0.89)
    elif n_leg > 8 and n_leg <= 12:
        legend = r.TLegend(0.22,y_pos-(n_leg/3.0)*0.05,y_pos,0.9)
    elif n_leg > 12:
        # legend = r.TLegend(0.22,y_pos-(n_leg/3.0)*0.05,y_pos,0.9)
        legend = r.TLegend(0.22,y_pos-(n_leg/4.0)*0.05,y_pos,0.9)
    else:
        legend = r.TLegend(0.635,y_pos-n_leg*0.05,y_pos,0.9)
    legend.SetTextSize(0.03)
    if n_leg > 4:
        legend.SetTextSize(0.02)

    legend.SetFillColor(0)
    legend.SetLineWidth(0)
    legend.SetFillStyle(0)
    legend.SetNColumns(1)
    if n_leg > 4:
        legend.SetNColumns(2)
    if n_leg > 8:
        legend.SetNColumns(3)
    if n_leg > 12:
        legend.SetNColumns(4)


    for name in histograms:
        if histograms[name][1].legend_options != None:
            legend.AddEntry(histograms[name][0],name,histograms[name][1].legend_options)

    r.SetOwnership( legend, 0 ) 
    return legend

def plot_histogram(canvas, histograms, x_axis_title = "x", y_axis_title="Normalized Number of events", 
                labels = [],
                do_legend = True, 
                do_atlas_labels = False,
                force_zero_min = False,
                left_margin = 0.2 ):
    '''
        canvas: TCanvas that will be drawn upon 
        histograms: a dictionary of tuples that will be drawn, scuh that 
                    {
                        histogram_name: (histogram, style_options),

                    }
    '''
    #divide the canvas into 
    canvas.Clear()
    canvas.cd()
    canvas.SetLeftMargin(left_margin )
    AS.SetAtlasStyle()
    r.gStyle.SetOptStat(0)
    r.gPad.Update()

    max_y       = get_maximum_y(histograms)*1.7
    min_y       = get_minimum_y(histograms)*1.15
    if force_zero_min:
        min_y = 0
    same_string = ""
    for name in histograms: 
        #rename the elements of the dictionary 
        hist = histograms[name][0]#.Clone()
        hist.SetName(name)
        hist.SetDirectory(0)
        style_opts = histograms[name][1]

        #format the histograms into nice lookign things 
        hist = set_style_options(hist,style_opts)
        hist.SetMaximum(max_y)
        hist.SetMinimum(min_y)

        hist.GetXaxis().SetTitle(x_axis_title)
        hist.GetYaxis().SetTitle(y_axis_title)

        #draw the histogram
        hist.Draw(style_opts.draw_options + same_string)
        # if "X+" in style_opts.draw_options:
        same_string = " same"

    #grab and draw the legend     
    if do_legend:
        legend = create_legend(histograms,y_pos = 0.945)
        legend.Draw()
    
    if do_atlas_labels:
        draw_atlas_details(labels, x_pos = 0.23,y_pos = 0.88, dy = 0.03, text_size = 0.028)

def th1f_to_tgraph(hist):
    x_points, y_points = [],[]
    for i in xrange(1, hist.GetSize()-2):
        x_points.append(hist.GetBinCenter(i))
        y_points.append(hist.GetBinContent(i))
    return r.TGraph( len(x_points),array('d',x_points), array('d',y_points) )

def ratio_plot(canvas, histograms,
            ratio_y_axis_title = "Data/MC", 
            y_axis_title="Normalzied Number of Events", 
            x_axis_title="",
            ratio_histograms = {},
            messages = []):
    '''
        canvas: TCanvas that will be drawn upon
        histograms: an dictionary of tuples such that 
                    {
                     histogram_name: (histogram, style_options, ratio_style_options), 
                     histogram_2_name: (histogram_2, style_option_2, ratio_style_options_2),
                    }
                    style_otion is an instance of the above class StyleOptions, name is a string and histogram is a TH1F 
        
        returns: a dictionary of ratio histograms such that
                 { 
                    histogram_name: [raito_histogram, ratio_style_options],
                    histogram_2_name: [raito_histogram, ratio_style_options_2]
                 }
        ratio_y_axis_title: title of the y axis of the ratio pannel
        y_axis_title: y axis title of the upper pannel plot
        x_axis_title: x axis title of the upper pannel (typically not shown thpugh )

        ratio_histograms: an dictionary of tuples such that 
                    {
                     histogram_name: (histogram, style_options,style_options ), 
                     histogram_2_name: (histogram_2,style_option_2, style_option_2 ),
                    }
    '''
    AS.SetAtlasStyle()
    r.gStyle.SetOptStat(0)
    
    #divide the canvas into 
    canvas.Clear()
    canvas.cd()
    pad1 =  r.TPad("pad1", "pad1", 0, 0.31, 1, 1.0)
    pad1.SetBottomMargin(0.0175)
    pad1.SetTopMargin(0.06)
    pad1.Draw()
    pad1.cd()

    # upper pannel 
    same_string = ""

    #grab the y axis maximum so we can set every histogram to have this same maximum 
    max_y       = get_maximum_y(histograms)*1.35
    for name in histograms: 
        #for clarity cache the histogram and styling options separately
        hist = histograms[name][0]

        style_opts = histograms[name][1]

        #format the histograms into nice lookign things 
        hist = set_style_options(hist,style_opts)
        hist.SetMaximum(max_y)
        hist.GetYaxis().SetTitle(y_axis_title)

        hist.Draw(style_opts.draw_options + same_string)
        same_string = " SAME "

    draw_atlas_details(messages,x_pos= 0.2,y_pos = 0.87, dy = 0.045,text_space = 0.1,text_size = 0.04)

    #also add ratio plots to the dictionary to be plotted
    # all_legend_histograms = histograms.copy()
    # all_legend_histograms.update(ratio_histograms)
    #copy the ratio histograms across to histograms at the end 
    # that way they appear as the last items in the legend/

    legend = create_legend(histograms,additional_entry_sizes = len(ratio_histograms))
    for name in ratio_histograms:
        if ratio_histograms[name][1].legend_options != None:
            legend.AddEntry(ratio_histograms[name][0],name,ratio_histograms[name][1].legend_options)

    legend.Draw("same")

    # lower pannel for ratio 
    canvas.cd()
    pad2 = r.TPad("pad2", "pad2", 0, 0.05, 1, 0.295)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.285)
    pad2.Draw()
    pad2.cd()


    #first evaluate the ratio plots and determine the maximum and minimum y 
    ratio_hists,  max_y,min_y = rhf.evaluate_ratio_histograms( histograms )
    #
    max_y = max(max_y, (2.0 - min_y))
    # max_y = 1.3
    min_y = 2.0 - max_y 
    max_y *= 1.05
    min_y *= 0.95

    same_string = ""

    # we need an axis to be drawn so that the TGRaphs can be drawn over them 
    # I appreciate this is a nasty and messy way of doing this 
    # but it works so... 
    for name in ratio_hists: 
        #separate out the histogram and style options 
        ratio_histogram = ratio_hists[name][0]
        ratio_style_opts = histograms[name][2] #evaluate_ratio_histograms has already removed the unwanted sytyle opions for the upper pannel
        
        #format the histogram
        ratio_histogram.SetMaximum(max_y) 
        ratio_histogram.SetMinimum(min_y) 
        r.TGaxis.SetMaxDigits(3)
        ratio_hists[name][0] = ratio_histogram = set_style_options(ratio_histogram,ratio_style_opts)
        
        ##
        ratio_histogram.GetYaxis().SetTitle(ratio_y_axis_title)
        ratio_histogram.GetXaxis().SetTitle(x_axis_title)

        #draw the histogram keeping track of what is the same
        ratio_histogram.Draw(ratio_style_opts.draw_options + same_string)
        same_string = " SAME "

    # Now draw the tgraphs that we've handed this function 
    for name in ratio_histograms: 
        #separate out the histogram and style options 
        ratio_histogram = ratio_histograms[name][0]
        ratio_style_opts = ratio_histograms[name][2] #evaluate_ratio_histograms has already removed the unwanted sytyle opions for the upper pannel
        
        #format the histogram
        ratio_histograms[name][0] = ratio_histogram = set_style_options(ratio_histogram,ratio_style_opts)
        
        ##
        ratio_histogram.GetYaxis().SetTitle(ratio_y_axis_title)
        ratio_histogram.GetXaxis().SetTitle(x_axis_title)

        #draw the histogram keeping track of what is the same
        ratio_histogram.Draw("2")

    # Overlay the TGraphs with the ratios of the upper pannel 
    for name in ratio_hists: 
        #separate out the histogram and style options 
        ratio_histogram = ratio_hists[name][0]
        ratio_style_opts = histograms[name][2] #evaluate_ratio_histograms has already removed the unwanted sytyle opions for the upper pannel
        
        #format the histogram
        ratio_histogram.SetMaximum(max_y) 
        ratio_histogram.SetMinimum(min_y) 
        r.TGaxis.SetMaxDigits(3)
        ratio_hists[name][0] = ratio_histogram = set_style_options(ratio_histogram,ratio_style_opts)
        
        ##
        ratio_histogram.GetYaxis().SetTitle(ratio_y_axis_title)
        ratio_histogram.GetXaxis().SetTitle(x_axis_title)

        #draw the histogram keeping track of what is the same
        ratio_histogram.Draw(ratio_style_opts.draw_options + same_string)
        same_string = " SAME "

    return ratio_hists 



