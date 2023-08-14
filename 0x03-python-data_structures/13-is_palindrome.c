#include "lists.h"

/**
*is_pal - Checks if a list is palindrome
*
*@head: Head of the original list
*@rev: Head of the reversed list
*
*Return: 1 if is palindrome else 0
*/
int is_pal(listint_t *head, listint_t *rev)
{
	while (head->next && rev->next)
	{
		if (head->n != rev->n)
			return (0);
		head = head->next;
		rev = rev->next;
	}
	if (!head && !rev)
		return (1);
	return (0);
}
/**
* reverse_list - Reverses a linked list
*
*@head: Head of the list to be reversed
*
*Return: Reversed list
*/
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	for (; current; current = next)
	{
		next = current->next;
		current->next = prev;
		prev = current;
	}
	head = prev;
	return (head);
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
	listint_t *r;

	if (!*head || (*head)->next == NULL)
		return (1);
	r = reverse_list(*head);
	if (is_pal(*head, r))
		return (1);
	return (0);
}
