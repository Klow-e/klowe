

# klowe/chisquare.py


###############################################################################################


import scipy.stats as stats


###############################################################################################


def chi2(a: int, b: int, c: int) -> float:
    d = a+b+c
    chi_num = 2*d*((a*d-b*c)**2)
    chi_den = (d**2-c**2)*(d**2-b**2)
    if chi_num == 0: chi = 0
    else: chi = chi_num / chi_den
    return chi


def confidence_chi2(chi: float) -> float:
    conlvl: float = round(1-(1-stats.chi2.cdf(chi,1)), 4)
    return conlvl


###############################################################################################

