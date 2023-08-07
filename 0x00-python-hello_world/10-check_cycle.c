#include "lists.h"

/**
* check_cycle - Checks if a singly linked list contains a cycle
*
*@list: The singly linked list
*Return: True or False
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp, *tmp1;
	tmp = tmp1 = list;

	while (tmp)
	{
		if (tmp->next == list || tmp1 == tmp)
			return (1);
		tmp1 = tmp;
		tmp = tmp->next;
	}
	return (0);
}
