#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#define BUFFER_SIZE 1000

int main(int argc, const char *argv[])
{
	int read_size = BUFFER_SIZE;

	if(argc < 2)
	{
		perror("Error");
		return(-1);
	}
	else{
		write(1,"==>",4);
		write(1,argv[1],strlen(argv[1]));
		write(1,"<==\n",5);
		for(int j=1;j<argc;j++)
		{
			int file = open(argv[j], O_RDONLY);
			char buff[BUFFER_SIZE];
			int counter = 0;
			while((read_size = read(file, buff, BUFFER_SIZE)) > 0)
			{
				int iterator = 0;
				while(iterator<read_size)
				{
					if(buff[iterator] == '\n')
            			counter++;
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
		}
	}
	return 0;
}
