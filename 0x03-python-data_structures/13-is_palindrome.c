#include "lists.h"

/**
* reverse_list - Reverses a linked list
*
*@h: Head of the list to be reversed
*
*Return: Reversed list
*/
listint_t *reverse_list(listint_t *h)
{
	return (h);
}
/**
* is_palindrome - Checks if a list palindrome
*
*@head: Head of the linkedlist
*
*Return: 1 if is_palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *reversed_list = NULL;

	if ((*head)->next == NULL)
		return (1);
	reversed_list = reverse_list(*head);
	if (reversed_list->n == (*head)->n)
		return (1);
	return (0);
}
