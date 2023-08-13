#include "lists.h"

/**
*is_pal - Checks if a list is palindrome
*
*@h: Head of the original list
*@r: Head of the reversed list
*
*Return: 1 if is palindrome else 0
*/
int is_pal(listint_t *h, listint_t *r)
{
	listint_t *head = h, *rev = r;

	while (head->next && rev->next)
	{
		if (head->n != rev->n)
			return (0);
		head = head->next;
		rev = rev->next;
	}
	return (1);
}
/**
* reverse_list - Reverses a linked list
*
*@h: Head of the list to be reversed
*
*Return: Reversed list
*/
listint_t *reverse_list(listint_t *h)
{
	listint_t *prev = NULL, *next, *head;

	for (head = h; head; head = next)
	{
		next = head->next;
		head->next = prev;
		prev = head;
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
	if ((*head)->next == NULL)
		return (1);
	if (is_pal(*head, reverse_list(*head)))
		return (1);
	return (0);
}
