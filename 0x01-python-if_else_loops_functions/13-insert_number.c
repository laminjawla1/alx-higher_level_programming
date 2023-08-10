#include "lists.h"
#include <stdio.h>

/**
* insert_node - Insert nodes in sorted order
*
*@head: The head of the list
*@number: Value to the nodes field
*
*Return: A pointer to the head of the list if successful else NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!*head || number <= tmp->n)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		while (tmp->next && tmp->next->n < number)
			tmp = tmp->next;
		node->next = tmp->next;
		tmp->next = node;
	}
	return (*head);
}
