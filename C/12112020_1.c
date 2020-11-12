#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

#define BUFFER_SIZE 128
typedef struct
{
    char data;
    unsigned char nextElementAdress;
} block;

int main(int argc, const char *argv[])
{
    int file = open(argv[1], O_RDONLY);
    struct block;
    block buff[BUFFER_SIZE];
    int read_size=0;
    while((read_size = read(file, buff, BUFFER_SIZE)) > 0)
	{
		write(1, buff, read_size);
	}
	close(file);
}