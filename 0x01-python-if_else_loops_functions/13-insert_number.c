#include "lists.h"

/**
 * insert_node - insert a node into a sorted list
 * @head: pointer to the head pointer.
 * @number: valueto store
 * Return: pointer to the inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *curr = NULL, *tmp = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	tmp = *head;
	while (tmp != NULL)
	{
		if (tmp->n > number)
			break;
		curr = tmp;
		tmp = tmp->next;
	}
	if (curr == NULL)
	{
		curr = tmp;
		tmp = new;
		new->next = curr;
	}
	else
	{
		curr->next = new;
		new->next = tmp;
	}
	return (new);
}
