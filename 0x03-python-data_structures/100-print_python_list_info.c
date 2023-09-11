#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - his function prints the size, allocated memory,
 * and types of elements
 * @p: pointer to a Python list object (PyObject)
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t len, alloc;
  Py_ssize_t i;
  PyObject *item, *type;

  if (PyList_Check(p)) 
{
    len = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < len; i++) {
      item = PyList_GetItem(p, i);
      type = PyObject_Type(item);
      printf("Element %ld: %s\n", i, ((PyTypeObject *)type)->tp_name);
      Py_XDECREF(type);
    }
  }
}
