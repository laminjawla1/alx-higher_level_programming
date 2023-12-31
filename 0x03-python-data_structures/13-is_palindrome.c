#include "lists.h"

/**
* len - Gets the length of the list
*
*@head: Head of the list
*
*Return: len(list)
*/
int len(listint_t *head)
{
	int length = 0;

	while (head)
	{
		length++;
		head = head->next;
	}
	return (length);
}
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
	while (rev)
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
	int i, length;
	listint_t *r, *mid = *head;

	if (!*head || (*head)->next == NULL)
		return (1);
	/*Middle of the list*/
	length = len(*head);
	for (i = 0; i < length / 2 - 1; i++)
		mid = mid->next;
	if ((length % 2 == 0) && (mid->n != mid->next->n))
		return (0);
	r = reverse_list(mid->next->next);
	if (is_pal(*head, r))
		return (1);
	return (0);
}
