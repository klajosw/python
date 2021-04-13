from __future__ import division
from __future__ import print_function
from __future__ import with_statement

from fortranfile import FortranRead
import physconst
import os.path

from byte2human import byte2human
from time2human import time2human
from version2human import version2human
from logged import Logged
import isotope

import datetime
import numpy as np
import sys
import socket
import time
from utils import loader

class WindData(Logged):
    """
    Interface to read KEPLER wnd (wind) files.
    """
    def __init__(self, 
                 filename, 
                 silent = False,
                 Rec = True):
        """
        Constructor; wants file name.
        """
        self.setup_logger(silent)
        filename = os.path.expanduser(filename)
        self.filename = os.path.expandvars(filename)
        self.file = FortranRead(self.filename)
        self._load(Rec)
        self.file.close()
        self.close_logger()
        self.file = None


    def _load(self, Rec = True):
        """Open file, call load data, time the load, print out
        diagnostics.

        If *Rec* is True (default) we use a record array,
        if *Rec* id False, load data as an object for each cycle.
        The latter mathod is about 200x slower for a full run."""

        self.logger_file_info(self.file)
        self.Rec = Rec
        if Rec == True:
            self.load_recarray()
        else:
            self.load_record_objects()
        self.logger_load_info(self.data[0].nvers,
                              self.data[ 0].ncyc,
                              self.data[-1].ncyc,
                              self.nmodels)

    def load_record_objects(self):
        """Load data as object records."""
        self.data=[]
        while not self.file.eof():
            record=WindRecord(self.file)
            self.data.append(record)
        self.nmodels = len(self.data)


    def load_recarray(self):
        """Load the entire wind file as a record aray."""
        
        # start by reading version information
        f = self.file        
        f.load()
        nvers = f.get_i4()
        ncyc = f.get_i4()
        f.rewind()
        if nvers == 20100:
            nsp = 19
            rectype = np.dtype([\
                ("reclen0", ">i4"),\
                ("nvers", ">i4"),\
                ("ncyc", ">i4"),\
                ("time", ">f8"),\
                ("dtime", ">f8"),\
                ("xm", ">f8"),\
                ("dms", ">f8"),\
                ("r", ">f8"),\
                ("u", ">f8"),\
                ("aw", ">f8"),\
                ("t", ">f8"),\
                ("sl", ">f8"),\
                ("cap", ">f8"),\
                ("teff", ">f8"),\
                ("reff", ">f8"),\
                ("yps", ">f8", (nsp)),\
                ("reclen1", ">i4")])
        elif nvers == 20000:
            nsp = 19
            rectype = np.dtype([\
                ("reclen0", ">i4"),\
                ("nvers", ">i4"),\
                ("ncyc", ">i4"),\
                ("time", ">f8"),\
                ("xm", ">f8"),\
                ("dms", ">f8"),\
                ("r", ">f8"),\
                ("u", ">f8"),\
                ("aw", ">f8"),\
                ("t", ">f8"),\
                ("sl", ">f8"),\
                ("cap", ">f8"),\
                ("teff", ">f8"),\
                ("reff", ">f8"),\
                ("yps", ">f8", (nsp)),\
                ("reclen1", ">i4")])
        elif nvers == 10100:
            nsp = 36
            rectype = np.dtype([\
                ("reclen0", ">i4"),\
                ("nvers", ">i4"),\
                ("ncyc", ">i4"),\
                ("time", ">f8"),\
                ("xm", ">f8"),\
                ("dms", ">f8"),\
                ("uterm", ">f8"),\
                ("r", ">f8"),\
                ("u", ">f8"),\
                ("aw", ">f8"),\
                ("t", ">f8"),\
                ("sl", ">f8"),\
                ("gammax", ">f8"),\
                ("cap", ">f8"),\
                ("teff", ">f8"),\
                ("reff", ">f8"),\
                ("yps", ">f8", (nsp)),\
                ("reclen1", ">i4")])
        elif nvers == 10000:
            nsp = 36
            rectype = np.dtype([\
                ("reclen0", ">i4"),\
                ("nvers", ">i4"),\
                ("ncyc", ">i4"),\
                ("time", ">f8"),\
                ("xm", ">f8"),\
                ("dms", ">f8"),\
                ("uterm", ">f8"),\
                ("r", ">f8"),\
                ("u", ">f8"),\
                ("aw", ">f8"),\
                ("teff", ">f8"),\
                ("sl", ">f8"),\
                ("gammax", ">f8"),\
                ("cap", ">f8"),\
                ("yps", ">f8", (nsp)),\
                ("reclen1", ">i4")])
        else:
            raise Error("Version not supported.")

        recsize = rectype.itemsize
        filesize = f.filesize
        assert np.mod(filesize, recsize) == 0,\
               "Inconsistent recod length / file size."
        self.nmodels = filesize // recsize
        self.data = np.recarray(\
            self.nmodels, \
            dtype = rectype, \
            buf = f.file.read())
        
    def write(self,
              filename=None,
              composition=True):
        if filename is None:
            f = sys.stdout
        else:
            f = open(os.path.expandvars(os.path.expanduser(filename)),'w')
        version = 10000
        user = os.getlogin()
        host = socket.gethostname()
        f.write("# Version {version:s} created from file {file:s} by {user:s} on {host:s} at {time:s}\n".format(
                version=version2human(version),
                file=self.filename,
                user=user,
                host=host,
                time=time.asctime(time.gmtime())+' UTC'))
        layout = "{:>8s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s} {:>23s}"
        format = "{:8d} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e} {:23.16e}"
        header = layout.format(
            'cycle',
            'time',
            'dt',
            'stellar mass',
            'mass loss rate',
            'outer radius',
            'surface velocity',
            'angular velocity',
            'surface temperature',
            'luminosity',
            'surface opacity',
            'effective temperature',
            'effective radius')
        units = layout.format(
            'number',
            's',
            's',
            'g',
            'cm',
            'g/s',
            'cm/s',
            'rad/s',
            'K',
            'erg/s',
            'cm2/g',
            'K',
            'cm')
        ions = isotope.KepIon.approx_ion_names()
        if composition:
            for ion in ions:
                header += ' {:>23s}'.format(ion)
                units += ' {:>23s}'.format('mass fraction')
        f.write(header+'\n')
        f.write(units +'\n')
        for record in self.data:
            # rec=dict()
            # for i in record.dtype.names:
            #     rec[i] = record[i]            
            data = format.format(
                    int(record.ncyc),
                    float(record.time),
                    float(record.dtime),
                    float(record.xm),
                    float(record.dms),
                    float(record.r),
                    float(record.u),
                    float(record.aw),
                    float(record.t),
                    float(record.sl),
                    float(record.cap),
                    float(record.teff),
                    float(record.reff))

            if composition:
                for i in xrange(len(ions)):
                    data += ' {:>23.16e}'.format(record.yps[i])
                f.write(data  +'\n')
        if filename is not None:
            f.close()

loadwind = loader(WindData, 'loadwind')

class WindRecord(object):
    def __init__(self,
                 file, 
                 data = True):
        self.ftag = ' ['+self.__class__.__name__+'] '
        self.file = file
        self.load(data)

    def load(self,
             data = True):
        f = self.file        
        f.load()
        self.nvers = f.get_i4()
        self.ncyc = f.get_i4()
        if self.nvers == 10000:
            nsp = 36
            self.time,\
                        self.xm,\
                        self.dms,\
                        self.uterm,\
                        self.r,\
                        self.u,\
                        self.aw,\
                        self.teff,\
                        self.sl,\
                        self.gammax,\
                        self.cap\
                        = f.get_f8an([11])
            self.yps = f.get_f8an([nsp-1])
        elif self.nvers == 10100:
            nsp = 36
            self.time,\
                        self.xm,\
                        self.dms,\
                        self.uterm,\
                        self.r,\
                        self.u,\
                        self.aw,\
                        self.t,\
                        self.sl,\
                        self.gammax,\
                        self.cap,\
                        self.teff,\
                        self.reff\
                        = f.get_f8an([13])
            self.yps = f.get_f8an([nsp-1])
        elif self.nvers == 20000:
            nsp = 19
            self.time,\
                        self.xm,\
                        self.dms,\
                        self.r,\
                        self.u,\
                        self.aw,\
                        self.t,\
                        self.sl,\
                        self.cap,\
                        self.teff,\
                        self.reff,\
                        = f.get_f8an([11])
            self.yps = f.get_f8an([nsp])
        elif self.nvers == 20100:
            nsp = 19
            self.time,\
                        self.dtime,\
                        self.xm,\
                        self.dms,\
                        self.r,\
                        self.u,\
                        self.aw,\
                        self.t,\
                        self.sl,\
                        self.cap,\
                        self.teff,\
                        self.reff\
                        = f.get_f8an([12])
            self.yps = f.get_f8an([nsp])
        f.assert_eor()
