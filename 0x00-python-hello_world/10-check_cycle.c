#include "lists.h"

/**
* check_cycle - Checks if a singly linked list contains a cycle
*
*@list: The singly linked list
*Return: True or False
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp1, *tmp2;

	if (!list)
		return (0);
	tmp1 = tmp2 = list;
	while (tmp1 && tmp2 && tmp2->next)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
