#include "lists.h"

/**
 * check_cycle - check if a linked list cyclic
 * @list: list head
 * Return: return 1 if cyclic or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *fixed =  list;

	if (!list)
		return (0);
	while (head->next != NULL && head->next->next != NULL)
	{
		head = head->next;
		if (head == fixed)
			return (1);
		if (head->next == fixed)
			return (1);
		head = head->next;
	}
	return (0);
}
