def load_spectra(target, spec1d):
    import os
    from specutils import Spectrum1D

    for i in range(1,11):
        newdata = 'espectro' + '{:02.0f}'.format(i)
        target[i] = newdata
        if os.path.isfile(newdata + '.fits'):
            spec1d[i] = Spectrum1D.read( newdata + '.fits' )  
        else:
            print('[-] No se encuentra: ' + newdata )

