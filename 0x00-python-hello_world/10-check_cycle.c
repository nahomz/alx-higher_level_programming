/*
 * Project - 0x00.Python - Hello, world
 * File - 10-check_cycle
 * Author - Waython Yesse
 * Occupation - Software Engineering Student at ALX
 * Year - 2021 November 15
 */

#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if there is no cycle, 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
