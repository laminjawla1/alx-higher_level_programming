#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - Prints the bytes information of a PyObject
*
* @p: A Python Object
*/
void print_python_bytes(PyObject *p)
{
	char *trying_string;
	size_t list_size, threshold, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	list_size = ((PyVarObject *)(p))->ob_size;
	trying_string = ((PyBytesObject *)p)->ob_sval;
	threshold = (list_size >= 10) ? 10 : list_size + 1;
	printf("  size: %ld\n", list_size);
	printf("  trying string: %s\n", trying_string);
	printf("  first %ld bytes:", threshold);
	for (i = 0; i < threshold; i++)
		(trying_string[i] >= 0) ? printf(" %02x", trying_string[i]) :
			printf(" %02x", 256 + trying_string[i]);
	printf("\n");
}
/**
* print_python_list - Prints the list information of a PyObject
*
* @p: A Python Object
*/
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *pp = (PyListObject *)p;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		item = pp->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
