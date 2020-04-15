#!/usr/bin/env python
import numpy as np
import math
import glob
from astropy.io import fits
from astropy.time import Time

fits_files=glob.glob('*.fits')

for i in fits_files:
    hdul = fits.open(i)
    date=hdul[0].header['date-obs']
    t = Time(date, format='isot', scale='utc')
    mjd=t.mjd
    #print (i, date, mjd)
    f = open("times_dates.txt", "a")
    print (i, date, mjd, file=f)
    f.close()
