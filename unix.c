#include<stdio.h>

void main()
{
	int c;
	while(1)
	{
		printf("Done");
		printf("1: Running Process\n 2: Join Process\n 3: Create process\n Enter Your Choice : \n");
		scanf("%d",&c);
		switch(c)
		{
		case 1:
		{
			system("ps");
		}break;
		case 2:
		{
		system("join college.txt city.txt > sai.txt");
		printf("Done");
		//system("join text1.txt text2.txt > text3.txt");
		}break;
		case 3:
		{
			int pid;
			pid = fork();
			if(pid == 0)
			{
				sleep(2);
				printf("Child Process\n");
				execl("/bin/ps","/bin/ps",NULL);
			}
			else
			{
				printf("Parent Process\n");
				wait();
			}
		}break;
		}
	}
}							
