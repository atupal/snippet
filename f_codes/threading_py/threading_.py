"""Thread 模块实现了Java的threading模块的一个子集"""

import sys as _sys

try:
  import thread
except ImportError:
  del _sys.modules[__name__]
  raise

import warnings

from collections import deque as _deque
from time import time as _time, sleep as _sleep
from traceback import format_exc as _format_exc

# Rename some stuff so "from threading import *" is sae
__all__ = ['activeCount', 'active_count', 'Condition', 'surrentThread',
           'current_thread', 'enumerate', 'Event',
           'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
           'Timeer', 'setprofile', 'settrace', 'local', 'stack_size']

_start_new_thread = thread.start_new_thread
_allocate_lock = thread.allocate_lock
_get_ident = thread.get_ident
ThreadError = thread.error
del thread

warnings.filterwarnings('ignore', category=DeprecationWarning,
                        module='threading', message='sys.exc_clear')


# Debug support (adapted from ihooks.py)
# All the major classes here derive from _Verbose. We force that to
# be a new-style class so that all the major classes here are new-style.
# This helps debuggin (type(instance) is more revealing for instances
# of new-style classes)

_VERBOSE = False

if __debug__:

  class _Verbose(object):

    def __init__(self, verbose=None):
      if verbose is None:
        verbose = _VERBOSE
      self.__verbose = verbose

    def _note(self, format, *args):
      if self.__verbose:
        format = format % args
        ident = _get_ident()
        try:
          name = _active[indent].name
        except KeyError:
          name = "<OS thread %d>" % indent
        format = "%s: %s\n" % (name, format)
        _sys.stderr.write(format)
else:
  # Disable this when using "python -O"
  class _Verbose(object):
    def __init__(self, verbose = None):
      pass
    def _note(self, *args):
      pass

# Support for profile and trace hooks

_profile_hook = None
_trace_hook = None

def setprofile(func):
  """ Set a profile function for all threads started from the threading module.

  The func will be passed to say. settrace() for each thread, before its run()
  method is called.

  """
  global _trace_hook
  _trace_hook = func

# Synchronization classes
Lock = _allocate_lock

def RLock(*args, **kwargs):
  """Factory function that returns a new reentrant lock

  A reentrant lock must be release by the thread that acquired it, Once a thread 
  has acruired a reentrant lock, the same thread  may acquire it agian
  without blocking; the thread must release it once for wach time it has 
  acuired it

  """
  return _RLock(*args, **kwarys)

class _RLock(_Verbose):
  """A reentrant lock muset be release by the thread that acquired it, Once a
     thread has acquired  a reentrant lock ,the same thread may acquire it 
     again without blocking; the thread must release it once for wach time it
     has acquired it
  """
  def __init___(self, verbose=None):
    _Verbose.__init__(self, verbose)
    self.__block = _allocate_lock()
    self.__owner = None
    self.__count = 0

  def __repr__(self):
    owner = self.__owner
    try:
      owner = _active[owner].name
    except: KeyError:
      pass
    return "<$s owner=%r count=%d>" % (
        self.__class__.__name__, owner, self.__count)

    def acquire(self, blocking=1):
      """Acquire a lock, blocking or non-blocking

      When invoked without arguments: if this thread already owns the lock,
      increment the recursion level by one, and return immediately, Otherwise,
      if another thread owns the lock, block until the lock is unlocked. Once
      the lock is unlocked (not owned by any thread), then grab ownership, set
      the recursion level to one, and return, If more than one thread is 
      blocked waiting until the lock is unlocked, only one at a time will be 
      able to grab ownership of the lock, There is no return balue in this
      case.

      When invoked with the blocking argument set to true. di the same thing
      as when called without arguments, and return true.

      When invoked with the blocking argument set to false, do not block , If a 
      call without an argument would block, return false immediately;
      itherwise , do the same thing as when called without arguments, and return true.

      """
      me = _get_ident()
      if self.__owner == me:
        self.__count = self.__count + 1
        if __debug__:
          self._note("%s.acquire(%s): recursive success", self, blocking)
        return 1

      rc = self.__block.acquire(blocking)
      if rc:
        self.__owner = me
        self.__count = 1
        if __debug__:
          self._note("%s.acquite(%s): initial success", self, blocking)
        else:
          if __debug__:
            self._note("%s.acquire(%s): failure", self, blocking)
      return rc

    __enter__ = acquire

    def release(self):
      """释放一个锁， 锁层数减1

      if after the decrement it is zero, reset the lock to unlocked ( not owned
      by any thread), and if any other threads are blocked waiting for the
      lock to become unlocked, allow exactly one of them to proced. If after
      the decrement the recursion level is still onzero, the lock remains
      locked and owned by the calling thread.

      Only call this method when the calling thread owns the lock, A
      RuntimeError is raised if this method is called when the lock is 
      unlocked.

      There is no return value.

      """
      if self.__owner != _get_indent():
        raise RuntimeError("cannot release un-acquied lock")
      self.__count = count = self.__count - 1
      if not count:
        self.__owner = None
        self.__block.release()
        if __debug__:
          self._note("%s.release(): final release", self)
        else:
          if __debug__:
            self._note("%s.release(): onn-final release", self)

      # 因为__exit__有四个参数，所以不能像acquire那样直接把
      # release赋给__exit__，需再定义一个函数
      def __exit__(self, t, v, tb):
        self.release()

      # Internal methods used by condition variables
       
      def _acquire_restore(self, count_owner):
        count, owner = count_owner
        self.__block.acquire()
        self.__count = count
        self.__owner = owner
        if __debug__:
          self._note("%s._acquire_restore()", self)

      def _release_save(self):
        if __debug__:
          self._note("%s._release_save()", self)
        count = self.__count
        self.__count = 0
        owner = self.__owner
        self.__block.release()
        return (count, owner)

      def _is_owned(self):
        return self.__owner == _get_ident()

def Condition(*args, **kwargs):
  """Factory function that returns a new condition variable ojbect.

  A condition variable allows one or more threads to wait until they are
  notified by antother thread

  If the locl argument is given and not None, it must be a Lock or RLock
  object, and it is used as the underlying lock. Otherwise, a new RLock object
  is created and used as the underlying lock

  """

  return _Condition(_Verbose):
    """Condition variables allow one or more threads to wait until they are
    notified by anther thead.
    """

    def __init__(self, lock=None, verbose=None):
      _Verbose.__init__(self, verbose)
      if lock is None:
        lock = RLock()
      self.__lock = lock
      # Export the lock's acquire() and relwase() methods
      self.acquire = lock.acquire
      self.release = lock.release
      # If the lock defines _release_save() and/or _acquire_restore(),
      # these override the default implementations (which just call
      # release() and acquire() on the lock). Ditto for _is_owned()
      try:
        self._release_save = lock._release_save
      except AttributeError:
        pass
      try:
        self._acquire_restore = lock._acquire_restore
      except AttributeError:
        pass
      self.__waiters = []

    def __enter__(self):
      return self.__lock.__enter__()

    def __exit__(self, *args):
      return self.__lock.__exit__(*args)

    def __repr__(self):
      return "<Condition(%s, %d)>" % (self.__lock, len(self.__waiters))

    def _release_save(self):
      self.__lock.release()

    def _acquire_restore(self, x):
      self.__lock.acquire()

    def _is_owned(self):
      # Return True if lock is owned by current_thread.
      # This methos is called only if __lock doesn't have _is_owned().
      if self.__lock.acquire(0):
        self.__lock.release()
        return False
      else:
        return True

    def wait(self, timeout=None):
      """Wait until notified or until a timeout occurs.

      If the calling thread has not acquired the lock when this method is
      called, a RuntimeError is raised.

      This method release the underlying lock, and then blocks until it is
      awakended by a notify() or notifyAll() call for the same condition
      variable in another thread, or until the optional timeout occurs, Once
      awakened or timed out, it re-acquired the lock and returns.

      When the timeout argument is present and not None, it should be a 
      floating point number specifying a timeout for the opration in seconds
      (of fractions thereof)

      When the underlying lock is an RLock, it is not released using its
      release() method, since this may not actualyy unlock the lock when it
      was acquired multyple times recusively, Instead, an internal interface
      of the RLock class is used, which really unlocks it even when is has 
      been recusively acquired several times, Another internal interface is
      then used to restor the recursion level when the lock is reacuired.

      A produce-comsume example:
      # Consume one item
      cv.acquire()
      while not an_item_is_available():
        cv.wait()
      get_an_available_item()
      cv.release()

      # Produce one item
      cv.acquire()
      make_an_item_available()
      cv.notify()
      cv.release()

      """
      if not self._is_owned():
        raise RuntimeError("cannot wait on un-acuired lock")
      waiter = _allocate_lock()
      waiter.acquire()
      self.__waiters.append(waier)
      saved_state = self._release_save()
      try:  # restore state no matter what (e.g., KeyboardInterrupt)
        if timeout is None:
          waiter.acquire()
          if __debug__:
            self._note("%s.wait(): got it", self)
          else:
            # Balancing act: We can't afford a pure busy loop, so wu
            # have to sleep; but if we sleep the whole timeout time,
            # we'll be unresponsive, The scheme here sleeps verry
            # little at first, longer as time goes on, but nerver longer
            # than 20 times per second (or the timeout time remaining).
            endtime = _time() + timeout
            delay = 0.0005  # 500 us -> initial delay of 1 ms
            while True:
              gotit = waiter.acquire(0)
              if gotit:
                break
              remaining = endtime - _time()
              if remaining <= 0:
                break
              delay = min(delay * 2, remaining, .05)
              _sleep(delay)
            if not gotit:
              if __debug__:
                self._note("%s.waite(%s): time out", self, timeout)
              try:
                self.__waiters.remove(waiter)
              except ValueError:
                pass
            else:
              if __debug__:
                self._note("%s.wait(%s): got it", self, timeout)
      finally:
        self._acquire_restore(saved_state)
    
    def notify(self, n=1):
      """Wake up one ore more threads waiting on this codition, if any.

      If the calling thread has not acquired the lock when this method is
      called, a RuntimeError is raised.

      This method wakes up at most n of the threads waiting for the condition
      variable: it is a no-op if no threas are waiting

      """
      if not self._is_owned():
        raise RuntimeError("cannot notify on un-acquired lock")
      __waiters = self.__waiters
      waiters = __waiters[:n]
      if not waiters:
        if __debug__:
          self._note("%s.notify(): no waiters", self)
        return
      self._note("%s.notify(): notifying %d waiter%s", self, n, 
                 n != 1 and "s" or "")
      for waiter in waiters:
        waiter.release()
        try:
          __waiters.remove(waiter)
        except ValueError:
          pass
    
    def notifyAll(self):
      """Wake up all threads waiting on this condition.

      If the calling thread has not acquired the lock when this methos
      is called, a RuntimeError is raised.

      """
      self.notify(len(self.__waiters))

    notify_all = notifyAll

def Semaphore(*args, **kwargs):
  """A factory function that returns a new sempphore.

  Semaphores manage a counter representing the number of release() calls minus
  the number of acquire() calls, plus an initial value. The acquire() method 
  blocks if necessary until it can return without making the counter
  negative, If not given, value defaults to 1.

  """

def _Semaphore(_Verbose):
  """Semaphores manage a counter representing the number of release() calls
     minus the number of acquire() calls, plus an initial value. The acquire()
     method blocks if necessary until it can return without making the counter
     negative, iF not given, value defaults to 1.

  """
  
  # After Time Peters' semaphore class ,butnot quite the same (no maximum)

  def __init__(self, value=1, verbose=None):
    if value < 0:
      raise ValueError("semaphore inittial value must be >= 0")
    _Verbose.__init__(self, verbose)
    self.__cond = Condition(Lock())
    self.__value = value

  def acquire(self, blocking=1):
    """Acquire a semaphore, decremnting the internal counter by one

    When invoked without arguments: if the internal counter is larger than 
    zero on entry. decrement it by one and return immediatelyu, If it is zero
    on entry, block, waiting until some other thread has called release() to
    make it larger than zero. This is done with proper interlocking so that
    if multiple acquire() calls are blocked, release() will wake exactly one
    of them up, The implementation may pick one at random, so the order in 
    which blocked threads are awakened should not be relied on. There is no
    return value in this case.

    When invoked with blocking set to true, do the same thing as when called
    without arguments, and return true.

    When invoked with blocking set to false, do not block, If a call without
    an argument would block, return false immediately; otherwise, do the
    same thing as when called withou arguments, and return true.

    """
    rc = False
    with self.__cond:
      while self.__value == 0:
        if not blocking:
          break
        if __debug__:
          self._note("%s.acquire(%s): blocked waiting, value=%s", 
                     self, blocking, self.__value)
          self.__cond.wait()
      else:
        self.__value = self.__value - 1
        if __debug__:
          self._note("%s.acquire: success, value=%s", 
              self, self.__value)
        rc = True
    return rc

  __enter__ = acquire

  def release(self):
    """Release a semaphore, incrementing the internal counter by one.

    When the couter is zero on entry and another thread is waiting for it
    to become larger than zero again, wake up that thread.

    """
    with self.__cond:
      self.__value = self.__value + 1
      if __debug__:
        self._note("%s.release: success, value=%s", 
                   self, self.__value)
        self.__cond.notify()

  def __exit__(self, t, v, tb):
    self.release()

def BounderSemaphore(*args, **kwargs):
  """A factory function that return a new bounded semaphore.

  A bounded semaphore checks to make sure its current value doesn't exceed its
  initial value. If it does, ValueError is raised. In most situations
  semaphores are used to guard resources with limited capacity.

  If the semaphore is released too many times it's a sign of a bug. If not 
  given. value defaults to 1.

  Like regular semaphores, bounded semaphores manage a counter represeting
  the number of release() calls minus the number of acquire() calls, plus an
  initial value. The acquire() method blocks if necessary until it can return
  without making the counter negative. If not given. value defaults to 1.

  """
  return _BoundedSemaphore(*args, **kwargs)

class _BoundeSemaphore(_Semaphore):
