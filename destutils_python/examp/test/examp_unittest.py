import unittest
import doctest

class DeviceTest( unittest.TestCase ):
  def runTest( self ):
    try:
      import examp
    except ImportError, e:
      self.Fail( str( e ) )
