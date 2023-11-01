#include "lists.h"
#include <stdio.h>
/**
 * insert_node - insert a node into a sorted list
 * @head: pointer to the head pointer.
 * @number: valueto store
 * Return: pointer to the inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *curr = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (*head != NULL)
	{
		if ((*head)->n > number)
			break;
		curr = *head;
		*head = (*head)->next;
	}
	if (curr == NULL)
	{
		curr = *head;
		*head = new;
		new->next = curr;
	}
	else
	{
		curr->next = new;
		new->next = *head;
	}
	return (new);
}
