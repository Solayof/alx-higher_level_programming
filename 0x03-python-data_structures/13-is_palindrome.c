#include "lists.h"

/**
 */

int is_palindrome(listint_t **head)
{
		listint_t *tmp = *head;
	unsigned int size = 0, i = 0;
	int buff[10240];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (tmp)
	{
		tmp = tmp->next;
		size += 1;
	}
	if (size == 1)
		return (1);

	tmp = *head;
	while (tmp)
	{
		buff[i++] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (buff[i] != buff[size - i - 1])
			return (0);
	}
	return (1);
}
