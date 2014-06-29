#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
#define RED FOREGROUND_RED
#define GREEN FOREGROUND_GREEN
#define BLUE FOREGROUND_BLUE
#define BUFSIZE 1000
/*
	LeGiT 
	The Lynch-eNVY Graphing Tool
	March 2013
*/
/*
This code is now a part of the GUISE Symblint Package
------------------------
sLING : serial LINe Grapher: The command line grapher on acid
------------------------
Lynch-eNVY Corp is now Lynch Computer Corp.
July 2014
*/


struct node{
	char val;
	struct node *next;
	};
typedef struct node *npt;

int ispoint(npt N){
	return N->next != NULL;
	}



void map_print(int h, npt map[]){
	printf("\n");
	int i;
	for(i=0; i<=(h*h)-1; ++i){
		if(i%h ==0){
			printf("\n");
			printf("%c ", map[i]->val);
			}
		else printf("%c ", map[i]->val);
		}

	}



void quad(int a, int b, int c, int y[],int h){
	int i;
	for(i=0; i<=h; ++i){
		y[i] = (a*i*i)+(b*i)+c;
		}
}

void line(int m, int c, int l[], int h){
	int i;
	for(i=0; i<=h; ++i){
		l[i] =(m*i) + c;
		}
}

/*
COPYRIGHT WINDOWS API
*/
/*
void colorer (char str[], int color)
{
     HANDLE h = GetStdHandle ( STD_OUTPUT_HANDLE ); //stdout handle
  WORD wOldColorAttrs; //->set back to old color once used
  CONSOLE_SCREEN_BUFFER_INFO csbiInfo;
   
  
   * First save the current color information
   
  GetConsoleScreenBufferInfo(h, &csbiInfo);
  wOldColorAttrs = csbiInfo.wAttributes; 
   
  
   * Set the new color information
   
  SetConsoleTextAttribute ( h, color | FOREGROUND_INTENSITY );
   
  printf ("%s", str);
 
  
   * Restore the original colors
   
  SetConsoleTextAttribute ( h, wOldColorAttrs);
  
  
}
*/
main(int argc, char *argv[]){
      start:;
     int gt=20;
     int p = (gt*gt)-1;    
    npt map[p];
    int qua[1000];
    int l[1000];
    int i, var[1000];
	for(i=0; i<=p; ++i){
		map[i] = malloc(sizeof(struct node));
		map[i]->val = ' ';
		map[i]->next = map[i+1];
		}
	//map[20]->next = NULL;  ----------ERROR :: TOGGLE BREAKPOINT HERE <- <- <- --------------------


	map_print(gt, map);
	map[p-(gt-1)]->val = ' ';
    int w = p-(gt-1);
	map_print(gt, map);
 	quad(1,-4,0,qua,gt);
	int sl, cept;
	scanf("%d", &sl);
	scanf("%d", &cept);
	line(sl,cept,l,gt);
	for(i=0; i<=gt; ++i){
   		int q = (w+i)-gt*(qua[i]);
		if(q>=0 && q<=p){
                //colorer(map[q]->val, RED);
		map[q]->val = '#';
    }
		}
	map_print(gt, map);
	getchar();
    goto start;
}
