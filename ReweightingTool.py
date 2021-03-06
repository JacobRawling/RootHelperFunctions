import ROOT as r 
import RootHelperFunctions as rhf 

class ReweightingTool:
    """
        Brief: constructs a string to be applied to the weight in a TTree::Draw command 
               to reweight a distribution to have a linear slope of size stress that passes
               through the median of the stressing distribution and increases it 

        Example Usage (after running setup.sh, in a different test.py)
               from RootHelperFunctions.ReweightingTool import ReweightingTool

               #get the histogram we're reweighting to 
               weight = "weight_mc"
               pt_spectrum = tuple.Draw("pT",weight,"")

               #construct a stressed histogram
               reweighter = ReweightingTool(pt_spectrum, 0.3)
               reweight = weight "*" + reweighter.reweight_string("pT")
               stressed_pt_sprectrum = tuple.Draw("pT",reweight,"")
    """
    def __init__(self,hist, stress, name = None):
        if name == None:
            self.name = hist.GetName() + "_reweighting_" + str(int(100.0*stress)) 
        else:
            self.name = name

        self.hist = hist
        self.stress = stress
        self.construct_reweighting()

    def construct_reweighting(self):
        # evalaute the range we are going to plot a linear fit to 
        # self.construct_reweighting_fixed_shape_difference()
        # return

        self.quanitles = rhf. GetQuantiles(self.hist,[0.0,0.5,0.99])
        last_quanitle  = self.quanitles[2]
        median         = self.quanitles[1]
        first_quantile = self.quanitles[0]
        # print "[ REWEIGHTER ] - Found median for hist: ", self.quanitles[1]

        #then get the gradient and intercept for this linear fit 
        self.m = 2.0*self.stress/last_quanitle 
        self.c = 1. - self.stress

        # self.m = self.stress/(median - first_quantile)
        # self.c = 1 - self.m*median

        # n_bins    = self.hist.GetNbinsX()
        # mid_point = self.hist.GetBinCenter(int(n_bins/2)+1)
        # upward    = self.hist.GetBinCenter(n_bins)
        # lower_bin_midpoint    = self.hist.GetBinCenter(1)
        # print "[ REWEIGHTER ] - Found n_bins = ", n_bins, " mid_pint = ", mid_point, " upward point = ", upward

        # self.m = self.stress/(mid_point-lower_bin_midpoint)
        # self.c = 1 - self.m*mid_point

    def construct_reweighting_fixed_shape_difference(self):
      n_bins    = self.hist.GetNbinsX()
      mid_point = self.hist.GetBinContent(int(n_bins/2))
      upward    = self.hist.GetBinContent(n_bins)

      self.m = self.stress/(mid_point-lower_bin_midpoint)
      self.c = 1 - self.m*mid_point

    def weight(self,var):
      """
        Var: a float of the variable that stress distirubiont has been constructed with. 
      """
      return self.m*var+self.c

    def reweight_string(self,var):
        return "("+str(self.m)+"*"+var+"+"+str(self.c)+")"