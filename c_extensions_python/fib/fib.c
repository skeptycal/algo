#include <Python.h>

//a func to calc fib numbers
int cFib(int n)
{
    if (n < 2)
        return n;
    return cFib(n - 1) + cFib(n - 2);
}

static PyObject *fib(PyObject *self, PyObject *args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    return Py_BuildValue("i", cFib(n));
}

static struct PyModuleDef cModPyDem =
    {
        PyModuleDef_HEAD_INIT,
        "fib",                              /* name of module */
        "Calculates the fibonacci number.", /* module documentation, may be NULL */
        -1,                                 /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

PyMODINIT_FUNC PyInit_cModPyDem(void)
{
    return PyModule_Create(&cModPyDem);
}
