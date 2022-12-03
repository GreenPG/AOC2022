/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   part2.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gpasquet <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/01 09:34:33 by gpasquet          #+#    #+#             */
/*   Updated: 2022/12/01 10:26:13 by gpasquet         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/include/libft.h"
#include "../get_next_line/get_next_line.h"
#include "fcntl.h"

int	main(void)
{
	char	*line;
	int		sum = 0;
	int		i;
	int		result[3] = {0, 0, 0};
	int		fd;

	fd = open("puzzle_input", O_RDONLY);
	line = get_next_line(fd);
	while (line)
	{
		if (line[0] != '\n')
			sum += ft_atoi(line);
		else 
		{
			if (sum > result[0])
			{
				result[2] = result[1];
				result[1] = result[0];
				result[0] = sum;
			}
			else if (sum > result[1])
			{
				result[2] = result[1];
				result[1] = sum;
			}
			else if (sum > result[2])
				result[2] = sum;
			sum = 0;
		}
		line = get_next_line(fd);
	}
	if (sum > result[0])
			{
				result[2] = result[1];
				result[1] = result[0];
				result[0] = sum;
			}
			else if (sum > result[1])
			{
				result[2] = result[1];
				result[1] = sum;
			}
			else if (sum > result[2])
				result[2] = sum;
	free(line);
	close(fd);
	ft_printf("%d, %d, %d\n", result[0], result[1], result[2]);
	ft_printf("%d\n", result[0] + result[1] + result[2]);
	return (0);
}
