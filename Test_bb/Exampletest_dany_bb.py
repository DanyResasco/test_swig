# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Exampletest_dany_bb', [dirname(__file__)])
        except ImportError:
            import _Exampletest_dany_bb
            return _Exampletest_dany_bb
        if fp is not None:
            try:
                _mod = imp.load_module('_Exampletest_dany_bb', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Exampletest_dany_bb = swig_import_helper()
    del swig_import_helper
else:
    import _Exampletest_dany_bb
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Box(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Box, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Box, name)
    __repr__ = _swig_repr
    __swig_setmethods__["T"] = _Exampletest_dany_bb.Box_T_set
    __swig_getmethods__["T"] = _Exampletest_dany_bb.Box_T_get
    if _newclass:T = _swig_property(_Exampletest_dany_bb.Box_T_get, _Exampletest_dany_bb.Box_T_set)
    __swig_setmethods__["Points"] = _Exampletest_dany_bb.Box_Points_set
    __swig_getmethods__["Points"] = _Exampletest_dany_bb.Box_Points_get
    if _newclass:Points = _swig_property(_Exampletest_dany_bb.Box_Points_get, _Exampletest_dany_bb.Box_Points_set)
    __swig_setmethods__["Isobox"] = _Exampletest_dany_bb.Box_Isobox_set
    __swig_getmethods__["Isobox"] = _Exampletest_dany_bb.Box_Isobox_get
    if _newclass:Isobox = _swig_property(_Exampletest_dany_bb.Box_Isobox_get, _Exampletest_dany_bb.Box_Isobox_set)
    __swig_setmethods__["Isobox_volume"] = _Exampletest_dany_bb.Box_Isobox_volume_set
    __swig_getmethods__["Isobox_volume"] = _Exampletest_dany_bb.Box_Isobox_volume_get
    if _newclass:Isobox_volume = _swig_property(_Exampletest_dany_bb.Box_Isobox_volume_get, _Exampletest_dany_bb.Box_Isobox_volume_set)
    __swig_setmethods__["centroid"] = _Exampletest_dany_bb.Box_centroid_set
    __swig_getmethods__["centroid"] = _Exampletest_dany_bb.Box_centroid_get
    if _newclass:centroid = _swig_property(_Exampletest_dany_bb.Box_centroid_get, _Exampletest_dany_bb.Box_centroid_set)
    __swig_setmethods__["distance_cm_orig"] = _Exampletest_dany_bb.Box_distance_cm_orig_set
    __swig_getmethods__["distance_cm_orig"] = _Exampletest_dany_bb.Box_distance_cm_orig_get
    if _newclass:distance_cm_orig = _swig_property(_Exampletest_dany_bb.Box_distance_cm_orig_get, _Exampletest_dany_bb.Box_distance_cm_orig_set)
    def box_distance(self, *args): return _Exampletest_dany_bb.Box_box_distance(self, *args)
    def __init__(self): 
        this = _Exampletest_dany_bb.new_Box()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Exampletest_dany_bb.delete_Box
    __del__ = lambda self : None;
Box_swigregister = _Exampletest_dany_bb.Box_swigregister
Box_swigregister(Box)

# This file is compatible with both classic and new-style classes.

