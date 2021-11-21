#include "lists.h"

/**
 *check_cycle - checks if there a loop in a linked list
 *It uses the floyed-cycle algorithm
 *@list: head of the linked least
 *Return: 1 if there is a loop, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (!list)
		return (0);
	fast = list->next;
	slow = list;

	while (fast && fast->next)
	{
		/*if there is a loop they would crush*/
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
