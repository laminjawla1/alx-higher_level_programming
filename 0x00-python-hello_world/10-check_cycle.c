#include "lists.h"

/**
* gateway - Checks if we are still eligible to enter
*
*@t1: Var one
*@t2: Var two
*@t3: Var three
*
*Return: True or False
*/
int gateway(listint_t *t1, listint_t *t2, listint_t *t3)
{
	return (t1 && t2 && t3->next);
}
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
	while (gateway(tmp1, tmp2, tmp2->next))
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
