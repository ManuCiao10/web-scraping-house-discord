#include "unistd.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "sys/types.h"
#include "sys/stat.h"
#include "sys/wait.h"

int call_python(char *argv[])
{
    pid_t pid;
    int status;
    int i;
    char *argv2[2];
    argv2[0] = "python3";
    argv2[1] = argv[1];
    pid = fork();
    if (pid == 0)
    {
        execvp("python3", argv2);
        printf("fuck thisé\n");
        exit(0);
    }
    if (pid < 0)
    {
        perror("fork");
        exit(1);
    }
    else
    {
        waitpid(pid, &status, -1);
        return 0;
    }

    return (0);
}

void do_python(void)
{

    char *argv[2];
    argv[0] = "python3";
    argv[1] = "kijiji.py";
    call_python(argv);

    argv[1] = "utils.py";
    call_python(argv);
}

int main(void)
{
    do_python();
}