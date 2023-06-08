%option noyywrap
%{
    #include<stdio.h>
%}
letter [A-Za-z]
digit [0-9]
identifier {letter}({letter}|{digit})*
number {digit}{digit}*
operator [+|-|*|/|=]
keywords int|float|void|main|printf|scanf
punctuation [;|,|!|(|)|{|}]
header #.*


%%
{header} {printf("\nHeader: %s",yytext);}
{keywords} {printf("\nKeyword: %s",yytext);}
{identifier} {printf("\nIdentifier: %s",yytext);}
{number} {printf("\nNumber: %s",yytext);}
{operator} {printf("\nOperator: %s",yytext);}
{punctuation} {printf("\nPunctuation: %s",yytext);}

%%

int main(){
    yyin = fopen("code.c", "r");
    yylex();
    return 0;
}