/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   part1.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gpasquet <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/01 09:34:33 by gpasquet          #+#    #+#             */
/*   Updated: 2022/12/01 10:10:58 by gpasquet         ###   ########.fr       */
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
	int		result = 0;
	int		fd;

	fd = open("sample", O_RDONLY);
	line = get_next_line(fd);
	while (line)
	{
		if (line[0] != '\n')
			sum += ft_atoi(line);
		else 
		{
			if (sum > result)
				result = sum;
			sum = 0;
		}
		line = get_next_line(fd);
	}
	free(line);
	close(fd);
	ft_printf("%d\n", result);
	return (0);
}
