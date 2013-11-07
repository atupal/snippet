classLoader = Thread.currentThread().getContextClassLoader();
if (classLoader == null) {
  classLoader = ***.class.getClassLoader();
}
