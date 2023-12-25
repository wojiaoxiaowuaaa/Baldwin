// example.c
#include <Python.h>

static PyObject* example_add(PyObject* self, PyObject* args) {
    int a, b;

    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    return PyLong_FromLong(a + b);
}

static PyMethodDef example_methods[] = {
    {"add", example_add, METH_VARARGS, "Add two numbers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef example_module = {
    PyModuleDef_HEAD_INIT,
    "example",   // 模块名
    NULL,
    -1,
    example_methods
};

PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&example_module);
}
