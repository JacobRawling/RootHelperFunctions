import ROOT as r 
import RootHelperFunctions as rhf 

class ReweightingTool:
    """
        Brief: constructs a string to be applied to the weight in a TTree::Draw command 
               to reweight a distribution to have a linear slope of size stress

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
        #evalaute the range we are going to plot a linear fit to 
        self.quanitles = rhf. GetQuantiles(self.hist,[0.0,0.99])
        last_quanitle = self.quanitles[1]
        first_quantile = self.quanitles[0]

        #then get the gradient and intercept for this linear fit 
        self.m = 2.0*self.stress/last_quanitle 
        self.c = 1. - self.stress

    def reweight_string(self,var):
        return "("+str(self.m)+"*"+var+"+"+str(self.c)+")"