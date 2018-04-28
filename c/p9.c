#include <stdio.h>
#include <stdlib.h> // For exit() function
#include <stdint.h>
#include <string.h>

/*
(setq c-default-style "linux"
      c-basic-offset 4
      tab-width 4
      indent-tabs-mode nil      
      )

 */

#define COMPRESSION_NONE 1
#define COMPRESSION_COMMAND 10
#define COMPRESSION_READ_DATA 20

uint64_t process(int depth, char *string, long size){

  char command[25];
  uint32_t command_index = 0;
  uint32_t state = COMPRESSION_NONE;

  uint64_t total_count = 0;
  uint64_t repeat, count = 0;

  char * repeat_data = (char*)0;
  uint32_t repeat_index = 0;  
  uint32_t repeat_size = 0;
  char c;

  for (long i=0; i< size; i++){
      c = string[i];
      if (state == COMPRESSION_NONE){
          if (c == '('){
              state = COMPRESSION_COMMAND;
              memset(&command[0], 0, sizeof(command));
              command_index = 0;
          } else {
              total_count++;
          }
      }
      else if (state == COMPRESSION_COMMAND){
          if (c == ')'){
              state = COMPRESSION_READ_DATA;
              command[command_index] = '\0';
              // figure out command, where's the x ?
              for (int j=0; j < command_index; j++){
                  if (command[j] == 'x'){
                      command[j] = '\0';
                      repeat = atoi(&command[j+1]);
                      count = atoi(command);
                      break;
                  }
              }
              if (repeat_data){
                  free(repeat_data);
              }
              repeat_index = 0;
          } else {
              command[command_index] = c;
              command_index++;
          }
      } else if (state == COMPRESSION_READ_DATA){
          if(!repeat_data){
              repeat_data = malloc(1024 * sizeof(char));
              if (repeat_data == 0){
                  printf("bad malloc");
                  exit(2);
              }
              repeat_size = 1024;
          } else if (repeat_index >= repeat_size){
              //repeat_data = realloc(repeat_data, (repeat_size + 1024)*sizeof(char));
              char *new_data = malloc((repeat_size + 1024)*sizeof(char));
              if (new_data == 0){
                  printf("bad malloc of new_data");
                  exit(2);
              }
              
              memcpy(new_data, repeat_data, repeat_size*sizeof(char));
              free(repeat_data);
              repeat_data = new_data;
              repeat_size += 1024;
          }

          repeat_data[repeat_index] = c;
          repeat_index++;
          count--;
          if (count == 0){
              char *expanded = malloc(repeat_index * repeat * sizeof(char));
              for (int k=0; k<repeat; k++){
                  memcpy(&(expanded[k*repeat_index]), repeat_data, repeat_index);
              }
              total_count += process(depth+1,
                                     expanded,
                                     repeat*repeat_index);
              state = COMPRESSION_NONE;
              free(repeat_data);
              repeat_data = (char*)0;
              free(expanded);
              expanded = (char*)0;
          }
      }
  }
  return total_count;
}

int main(int argc, char** argv)
{
    if (argc == 1){
        return 0;
    }
    
    FILE *f = fopen(argv[1], "r");
  fseek(f, 0, SEEK_END);
  long fsize = ftell(f);
  fseek(f, 0, SEEK_SET);  //same as rewind(f);

  char *string = malloc(fsize + 1);
  fread(string, fsize, 1, f);
  fclose(f);

  string[fsize] = 0;
  if (string[fsize-1] == '\n'){
      string[fsize-1] = 0;
      fsize--;
  }

  printf("size is %llu\n", process(0, string, fsize));
  
  free(string);
  return 0;
}
