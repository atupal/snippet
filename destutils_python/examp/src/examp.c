#include <Python.h>

PyMODINIT_FUNC initexamp(void) {
  PyObject *m;
  m = Py_InitModule("examp", NULL);
}
