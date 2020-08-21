def load_spectra(target, spec1d):
    import os
    from specutils import Spectrum1D

    for i in range(1,11):
        target[i] = i
        if os.path.isfile( str(i) + '.fits'):
            spec1d[i] = Spectrum1D.read( str(i) + '.fits' )  
        else:
            print('[-] No se encuentra: ' + str(i) + '.fits' )

def gaussian(x, amp, cen, wid):
    from numpy import exp 
    return 1 + amp * exp(-(x-cen)**2 / wid)
