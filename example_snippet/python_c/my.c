#include "Python.h"
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

static PyObject *
add(PyObject *self,PyObject *args){
  const int *x;
  const int *y;
  if (!PyArg_ParseTuple(args, "ii", &x, &y))
    return NULL;
  return Py_BuildValue("i",x+y);
}

PyMethodDef methods[] = {
  {"add", add, METH_VARARGS},
}

void initpycabinet(){
  PyObject* m;
  m = Py_InitModule("my", methods);
}
