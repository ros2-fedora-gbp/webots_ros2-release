# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import sys
import os
if os.name == 'nt' and sys.version_info >= (3, 8):  # we need to explicitly list the folders containing the DLLs
    webots_home = os.environ['WEBOTS_HOME']
    os.add_dll_directory(os.path.join(webots_home, 'lib', 'controller'))
# MSYS2_HOME should be set by Webots or ~/.bash_profile
# if not set, we are in the case of an extern controller and a regularly installed version of Webots
    msys64_root = os.environ['MSYS2_HOME'] if 'MSYS2_HOME' in os.environ else os.path.join(webots_home, 'msys64')
    cpp_folder = os.path.join(msys64_root, 'mingw64', 'bin', 'cpp')
    if not os.path.isdir(cpp_folder):  # development environment
        cpp_folder = os.path.join(msys64_root, 'mingw64', 'bin')
    os.add_dll_directory(cpp_folder)



from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vehicle')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vehicle')
    _vehicle = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vehicle', [dirname(__file__)])
        except ImportError:
            import _vehicle
            return _vehicle
        try:
            _mod = imp.load_module('_vehicle', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vehicle = swig_import_helper()
    del swig_import_helper
else:
    import _vehicle
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import controller
class Driver(controller.Supervisor):
    __swig_setmethods__ = {}
    for _s in [controller.Supervisor]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Driver, name, value)
    __swig_getmethods__ = {}
    for _s in [controller.Supervisor]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Driver, name)
    __repr__ = _swig_repr
    INDICATOR_OFF = _vehicle.Driver_INDICATOR_OFF
    INDICATOR_RIGHT = _vehicle.Driver_INDICATOR_RIGHT
    INDICATOR_LEFT = _vehicle.Driver_INDICATOR_LEFT
    SPEED = _vehicle.Driver_SPEED
    TORQUE = _vehicle.Driver_TORQUE
    DOWN = _vehicle.Driver_DOWN
    SLOW = _vehicle.Driver_SLOW
    NORMAL = _vehicle.Driver_NORMAL
    FAST = _vehicle.Driver_FAST

    def __init__(self):
        this = _vehicle.new_Driver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    if _newclass:
        getDriverInstance = staticmethod(_vehicle.Driver_getDriverInstance)
    else:
        getDriverInstance = _vehicle.Driver_getDriverInstance
    __swig_destroy__ = _vehicle.delete_Driver
    __del__ = lambda self: None
    if _newclass:
        isInitialisationPossible = staticmethod(_vehicle.Driver_isInitialisationPossible)
    else:
        isInitialisationPossible = _vehicle.Driver_isInitialisationPossible

    def step(self):
        return _vehicle.Driver_step(self)

    def setSteeringAngle(self, steeringAngle):
        return _vehicle.Driver_setSteeringAngle(self, steeringAngle)

    def getSteeringAngle(self):
        return _vehicle.Driver_getSteeringAngle(self)

    def setCruisingSpeed(self, speed):
        return _vehicle.Driver_setCruisingSpeed(self, speed)

    def getTargetCruisingSpeed(self):
        return _vehicle.Driver_getTargetCruisingSpeed(self)

    def getCurrentSpeed(self):
        return _vehicle.Driver_getCurrentSpeed(self)

    def setThrottle(self, throttle):
        return _vehicle.Driver_setThrottle(self, throttle)

    def getThrottle(self):
        return _vehicle.Driver_getThrottle(self)

    def setBrakeIntensity(self, intensity):
        return _vehicle.Driver_setBrakeIntensity(self, intensity)

    def getBrakeIntensity(self):
        return _vehicle.Driver_getBrakeIntensity(self)

    def setIndicator(self, state):
        return _vehicle.Driver_setIndicator(self, state)

    def setHazardFlashers(self, state):
        return _vehicle.Driver_setHazardFlashers(self, state)

    def getIndicator(self):
        return _vehicle.Driver_getIndicator(self)

    def getHazardFlashers(self):
        return _vehicle.Driver_getHazardFlashers(self)

    def setDippedBeams(self, state):
        return _vehicle.Driver_setDippedBeams(self, state)

    def setAntifogLights(self, state):
        return _vehicle.Driver_setAntifogLights(self, state)

    def getDippedBeams(self):
        return _vehicle.Driver_getDippedBeams(self)

    def getAntifogLights(self):
        return _vehicle.Driver_getAntifogLights(self)

    def getRpm(self):
        return _vehicle.Driver_getRpm(self)

    def getGear(self):
        return _vehicle.Driver_getGear(self)

    def setGear(self, gear):
        return _vehicle.Driver_setGear(self, gear)

    def getGearNumber(self):
        return _vehicle.Driver_getGearNumber(self)

    def getControlMode(self):
        return _vehicle.Driver_getControlMode(self)

    def setWiperMode(self, mode):
        return _vehicle.Driver_setWiperMode(self, mode)

    def getWiperMode(self):
        return _vehicle.Driver_getWiperMode(self)

    def setBrake(self, brake):
        return _vehicle.Driver_setBrake(self, brake)

    def setWipersMode(self, mode):
        return _vehicle.Driver_setWipersMode(self, mode)

    def getWipersMode(self):
        return _vehicle.Driver_getWipersMode(self)
Driver_swigregister = _vehicle.Driver_swigregister
Driver_swigregister(Driver)

def Driver_getDriverInstance():
    return _vehicle.Driver_getDriverInstance()
Driver_getDriverInstance = _vehicle.Driver_getDriverInstance

def Driver_isInitialisationPossible():
    return _vehicle.Driver_isInitialisationPossible()
Driver_isInitialisationPossible = _vehicle.Driver_isInitialisationPossible

class Car(Driver):
    __swig_setmethods__ = {}
    for _s in [Driver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Car, name, value)
    __swig_getmethods__ = {}
    for _s in [Driver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Car, name)
    __repr__ = _swig_repr
    TRACTION = _vehicle.Car_TRACTION
    PROPULSION = _vehicle.Car_PROPULSION
    FOUR_BY_FOUR = _vehicle.Car_FOUR_BY_FOUR
    COMBUSTION_ENGINE = _vehicle.Car_COMBUSTION_ENGINE
    ELECTRIC_ENGINE = _vehicle.Car_ELECTRIC_ENGINE
    PARALLEL_HYBRID_ENGINE = _vehicle.Car_PARALLEL_HYBRID_ENGINE
    POWER_SPLIT_HYBRID_ENGINE = _vehicle.Car_POWER_SPLIT_HYBRID_ENGINE
    WHEEL_FRONT_RIGHT = _vehicle.Car_WHEEL_FRONT_RIGHT
    WHEEL_FRONT_LEFT = _vehicle.Car_WHEEL_FRONT_LEFT
    WHEEL_REAR_RIGHT = _vehicle.Car_WHEEL_REAR_RIGHT
    WHEEL_REAR_LEFT = _vehicle.Car_WHEEL_REAR_LEFT
    WHEEL_NB = _vehicle.Car_WHEEL_NB

    def __init__(self):
        this = _vehicle.new_Car()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _vehicle.delete_Car
    __del__ = lambda self: None

    def getType(self):
        return _vehicle.Car_getType(self)

    def getEngineType(self):
        return _vehicle.Car_getEngineType(self)

    def setIndicatorPeriod(self, period):
        return _vehicle.Car_setIndicatorPeriod(self, period)

    def getIndicatorPeriod(self):
        return _vehicle.Car_getIndicatorPeriod(self)

    def getBackwardsLights(self):
        return _vehicle.Car_getBackwardsLights(self)

    def getBrakeLights(self):
        return _vehicle.Car_getBrakeLights(self)

    def getTrackFront(self):
        return _vehicle.Car_getTrackFront(self)

    def getTrackRear(self):
        return _vehicle.Car_getTrackRear(self)

    def getWheelbase(self):
        return _vehicle.Car_getWheelbase(self)

    def getFrontWheelRadius(self):
        return _vehicle.Car_getFrontWheelRadius(self)

    def getRearWheelRadius(self):
        return _vehicle.Car_getRearWheelRadius(self)

    def getWheelEncoder(self, wheel):
        return _vehicle.Car_getWheelEncoder(self, wheel)

    def getWheelSpeed(self, wheel):
        return _vehicle.Car_getWheelSpeed(self, wheel)

    def getRightSteeringAngle(self):
        return _vehicle.Car_getRightSteeringAngle(self)

    def getLeftSteeringAngle(self):
        return _vehicle.Car_getLeftSteeringAngle(self)

    def enableLimitedSlipDifferential(self, enable):
        return _vehicle.Car_enableLimitedSlipDifferential(self, enable)

    def enableIndicatorAutoDisabling(self, enable):
        return _vehicle.Car_enableIndicatorAutoDisabling(self, enable)
Car_swigregister = _vehicle.Car_swigregister
Car_swigregister(Car)

# This file is compatible with both classic and new-style classes.


