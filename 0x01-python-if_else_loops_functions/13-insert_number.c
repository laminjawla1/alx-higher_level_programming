#include "lists.h"
#include <stdio.h>

/**
* create_node - Creates a node
*
*@number: Value to the node field
*
*Return: New node if successful else NULL
*/
listint_t *create_node(int number)
{
	listint_t *node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	return (node);
}
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
	listint_t *node = create_node(number);

	if (!node)
		return (NULL);
	if (!*head)
		*head = node;
	else
	{
		while (tmp->next && tmp->next->n < number)
			tmp = tmp->next;
		node->next = tmp;
		tmp->next = node;
	}
	return (*head);
}
