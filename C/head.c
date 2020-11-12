#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#define BUFFER_SIZE 1000

int main(int argc, const char *argv[])
{
	int file = open(argv[1], O_RDONLY);
	if(argc < 2)
	{
		perror("Error");
		return(-1);
	}
	if(file == -1)
	{
		perror("open() failed");
		return (-1);
	}
	char buff[BUFFER_SIZE];
	int counter = 0;
	int read_size;
	while((read_size = read(file, buff, BUFFER_SIZE)) > 0)
	{
		int iterator = 0;
		while(iterator<read_size)
		{
			if(buff[iterator] == '\n')
			{
            	counter++;
            }
            if(counter == 10)
       		{
            	iterator = iterator + 1;
                break;
            }
            iterator++;
            
		}
		write(1, buff, iterator);

	}
	close(file);
	return 0;
}
