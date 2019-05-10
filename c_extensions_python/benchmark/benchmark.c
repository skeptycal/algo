#include <Python.h>
#include <stdio.h>
static PyObject *foo_bar(PyObject *self, PyObject *args);
static PyMethodDef FooMethods[] = {
{"calc",  foo_bar, METH_VARARGS},
{NULL, NULL}  /* Sentinel */
};
void initbenchmark()
{
(void) Py_InitModule("benchmark", FooMethods);
}
static PyObject *foo_bar(PyObject *self, PyObject *args)
{
if (!PyArg_ParseTuple(args, ""))
return NULL;
long long a = 100234234;  long long b = 22342342;  long long c = 341342;
for(int i = 1; i <= 10000000; i++){
a = (a * a * b)%c;
b = (a * b * b)%c;
}
return Py_BuildValue("L", a+b);
}
