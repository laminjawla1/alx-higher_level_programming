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
	return (1);
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
	listint_t *prev = NULL, *next;

	for (; head; head = next)
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
	listint_t *r;

	if (!*head || (*head)->next == NULL)
		return (1);
	r = reverse_list(*head);
	if (is_pal(*head, r))
	{
		*head = reverse_list(*head);
		return (1);
	}
	*head = reverse_list(*head);
	return (0);
}
