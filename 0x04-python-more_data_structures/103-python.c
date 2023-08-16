#include <Python.h>

/**
* print_python_bytes - Prints bytes bytes objects
*
*@p: Python object
*
*/
void print_python_bytes(PyObject *p)
{
	char *trying_string;
	unsigned long int threshold, i;
	size_t list_size;

	PyListObject *plo = (PyListObject *)p;
	PyBytesObject *pbo = (PyBytesObject *)p;

	list_size = plo->ob_base.ob_size;
	trying_string = pbo->ob_sval;
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", list_size);
	printf("  trying string: %s\n", trying_string);
	threshold = (list_size >= 10) ? 10 : list_size + 1;

	printf("first %ld bytes: ", threshold);
	for (i = 0; i < threshold; i++)
		(trying_string[i] >= 0) ? printf(" %02x", trying_string[i]) :
			printf(" %02x", 256 + trying_string[i]);
	printf("\n");
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
	printf("[*] Size of the python list = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		item = pp->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
