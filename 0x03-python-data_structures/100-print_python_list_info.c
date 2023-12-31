#include <Python.h>

/**
* print_python_list_info - Prints informations about a python list
*
*@p: An instance of the PyObject struct
*
*/
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *pp = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);
	for (i = 0; i < pp->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
}
