import ROOT as r 
import ATLASStyle.AtlasStyle as AS
from array import array
import RootHelperFunctions as rhf 

"""

    
"""
class StyleOptions:
    def __init__(
        self,
        draw_options = "",
        line_color   = r.kBlack,
        line_style   = 1,
        fill_color   = r.kWhite,
        fill_style   = 0,
        marker_color = r.kBlack,
        marker_style = 20,
        marker_size  = 0.045,
        legend_options = "l"
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
    return hist
 
def draw_atlas_details(labels,x_pos= 0.2,y_pos = 0.87, dy = 0.04,text_size = 0.035):
    AS.ATLASLabel(   x_pos,y_pos,1,dy*2.0,dy,"Simulation Internal")
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

    for name in histograms:
        legend.AddEntry(histograms[name][0],name,histograms[name][1].legend_options)

    return legend

def ratio_plot(canvas, histograms, denonimator_hist_name = "MC"):
    AS.SetAtlasStyle()

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
        same_string += " SAME "

    draw_atlas_details( ["Combined regions"] )
    legend = create_legend(histograms)
    legend.Draw()

    # lower pannel for ratio 
    canvas.cd()
    pad2 = r.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.285)
    pad2.Draw()
    pad2.cd()

    same_string = ""
    for name in histograms: 
        # if name == denonimator_hist_name:
            # continue 
        #
        hist = histograms[name][0]
        style_opts = histograms[name][1]
        #
        hist = set_style_options(hist,style_opts)
        #
        ratio_hist = rhf.evaluate_ratio_histogram(hist,histograms[denonimator_hist_name][0])
        ratio_hist.Draw(style_opts.draw_options + same_string)
        same_string += " SAME "



