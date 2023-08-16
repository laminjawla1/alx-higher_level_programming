#include <Python.h>

/**
* print_python_bytes - Prints bytes bytes objects
*
*@p: Python object
*
*/
void print_python_bytes(PyObject *p)
{
	PyListObject *plo = (PyListObject *)p;
	PyBytesObject *pbo = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("    [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("    size: %ld\n", plo->ob_base.ob_size);
	printf("    trying string: %s\n", pbo->ob_sval);
}
/**
* print_python_list - Prints information about python list
*
*@p: Python object
*
*/
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *pp = (PyListObject *)p;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the python list %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		item = pp->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
