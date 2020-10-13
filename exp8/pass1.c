#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int loc;
struct optab
{
   char mne[10];
   int  op;
};
struct symtab
{
   char sname[10];
   int location;
   int err;
};
  
struct source 
{
    int add;
  char label[10];
  char opcode[10];
  char operand[10];
};
void main()
{
   struct source s[100],inte[100];
   struct optab o[100];
   struct symtab sm[100];
   
   
   int n,i,size,sa,flg,k=0,j,len;
  
printf(" Enter the size of optab: ");
   scanf("%i",&size);
printf("Enter the optab data:\n"); 
   for(i=0;i<size;i++)
{
   scanf("%s",o[i].mne);
   scanf("%i",&o[i].op);
}  
printf(".....................OPTAB.....................\n");
for(i=0;i<size;i++)
{
   printf("%s\t%i\n",o[i].mne,o[i].op);
}
printf("\n");
printf("Enter the size of source program: ");

   scanf("%i",&n);

printf("Enter the data of source program:\n");
   for(i=0;i<n;i++)
  {
       s[i].add=0;
       inte[i].add=0;
       scanf("%s",s[i].label);
       strcpy(inte[i].label,s[i].label);
       scanf("%s",s[i].opcode);
       strcpy(inte[i].opcode,s[i].opcode);
       scanf("%s",s[i].operand);
       strcpy(inte[i].operand,s[i].operand);
   }

printf("..........................THE SOURCE PROGRAM.............................\n");
   for(i=0;i<n;i++)
{
     printf("%i\t%s\t%s\t%s\n",s[i].add,s[i].label,s[i].opcode,s[i].operand);
 }
printf("\n");
  if(strcmp(s[0].opcode,"START")==0) 
  {
       sa=atoi(s[0].operand);
       
   }
  else
  {
      
       sa=0;
   }
loc=sa;
   i=1;
   inte[0].add=loc;
   while(strcmp(s[i].opcode,"END")!=0)
 {
           len=loc;
           inte[i].add=loc;
           flg=0;
           for(j=0;j<k;j++)
          {   
                if(strcmp(s[i].label,"-")==0)
                {   
                        flg=1;break;
                }
               else
                { 
                  if(strcmp(s[i].label,sm[j].sname)==0)
                    {
                          sm[k].err=1;
                           flg=1;
                          break;
                   }
                 }
               
          }    
         if(flg==0)
        {
              strcpy(sm[k].sname,s[i].label);
              sm[k].location=loc;
              sm[k].err=0;
              k++;
              
         }

      int a=0;
     
 
 
       while(a<size)
       {     
             if(strcmp(s[i].opcode,o[a].mne)==0)
                   { loc=loc+3;break;}
              
                   a++;
        }
             if(strcmp(s[i].opcode,"WORD")==0)
                   {loc=loc+3;}
            else if(strcmp(s[i].opcode,"RESW")==0)
                  {loc = loc + 3*(atoi(s[i].operand));}
            else if(strcmp(s[i].opcode,"RESB")==0)
                  {loc=loc+ atoi(s[i].operand);}
            else if(strcmp(s[i].opcode,"BYTE")==0)
                   {loc =loc+(strlen(s[i].operand)-3);}
         
            
      i++;
}
  printf(".......................................SYMTAB.............................................\n");                      
   for(i=0;i<k;i++)
        printf("%s\t%i\t%i\n",sm[i].sname,sm[i].location,sm[i].err); 
 printf(".....................................INTEREDIATE FILE...................................................\n");
   for(i=0;i<n;i++)
       printf("%i\t%s\t%s\t%s\n",inte[i].add,inte[i].label,inte[i].opcode,inte[i].operand);    
      
printf("\n");
printf("The length of the file: %i\n",len-sa);                   
   
} 
