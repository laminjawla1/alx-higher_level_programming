#include "lists.h"

/**
* check_cycle - Checks if a singly linked list contains a cycle
*
*@list: The singly linked list
*Return: True or False
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp)
	{
		if (tmp->next == list)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
