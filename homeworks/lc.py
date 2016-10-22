
import itertools
import os
import reprlib
from collections import defaultdict
import matplotlib.pyplot as plt


def lc_reader(filename):
    lclist=[]
    with open(filename) as fp:
        for i, line in enumerate(fp):
            if (i == 0):
                line = line.replace('#','')
                facetname=line.split()
            elif (i == 1):
                line = line.replace('#','')
                facetvalues=line.split()
            elif (line.find('#')!=0):
                lclist.append([float(f) for f in line.strip().split()])
        
        dict_of_facets = dict(zip(facetname, facetvalues))
        
    return (lclist, dict_of_facets)
                
class LightCurve:
    
    
    def __init__(self, data, metadict):
        self._time = [x[0] for x in data]
        self._amplitude = [x[1] for x in data]
        self._error = [x[2] for x in data]
        self.metadata = metadict
        self.filename = None
        self.listofTuples = []
    
    @classmethod
    def from_file(cls, filename):
        lclist, metadict = lc_reader(filename)
        instance = cls(lclist, metadict)
        instance.filename = filename
        instance.listofTuples = list(zip(instance._time, instance._amplitude))
        return instance
    
    def __repr__(self):
        class_name = type(self).__name__
        components = reprlib.repr(list(itertools.islice(self.timeseries,0,10)))
        components = components[components.find('['):]
        return '{}({})'.format(class_name, components)        
        
    #your code here
    @property
    def time(self):
        return self._time
    
    @property
    def amplitude(self):
        return self._amplitude
    
    @property
    def timeseries(self):
        return zip(self.time, self.amplitude)
    
    def __getitem__(self, index):
        return self.listofTuples[index]
    
    def __len__(self):
        return len(self.listofTuples)
    
class LightCurveDB:
    
    def __init__(self):
        self._collection={}
        self._field_index=defaultdict(list)
        self._tile_index=defaultdict(list)
        self._color_index=defaultdict(list)
    
    def populate(self, folder):
        for root,dirs,files in os.walk(folder): # DEPTH 1 ONLY
            for file in files:
                if file.find('.mjd')!=-1:
                    the_path = root+"/"+file
                    self._collection[file] = LightCurve.from_file(the_path)
    
    def index(self):
        for f in self._collection:
            lc, tilestring, seq, color, _ = f.split('.')
            field = int(lc.split('_')[-1])
            tile = int(tilestring)
            self._field_index[field].append(self._collection[f])
            self._tile_index[tile].append(self._collection[f])
            self._color_index[color].append(self._collection[f])
     
    def retrieve(self,facet,value):
        facet_dict = {'field':self._field_index, 'tile':self._tile_index, 'color':self._color_index}
        return(facet_dict[facet][value])