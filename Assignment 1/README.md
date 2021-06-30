# ASSIGNMENT-1: Bash Scripting

## q1 .sh
* Created the directory using the command `mkdir Assignment1` and cd into it using the command `cd Assignment1`.
* Created the required empty files using the command `touch lab1.txt lab2.txt lab3.txt lab4.txt lab5.txt`.
* Renamed the files to .c format using the command `ls *.txt | sed 's/.txt/''/g' | xargs -I {} mv {}.txt {}.c`.
Note: Here, I have renamed the files by taking the file names as the argument in xargs and then renamed the .txt files to .c files.
* Used the command `ls -lSr` to display the contents of the directory `Assignment1` in long list format sorted in increasing order of the file size.
Note: The fifth parameter in the output is the file size. After executing the above command, we can see that the data has been sorted in ascending order according to the fifth column.
* Displayed the paths of all files and foldes with their absolute path upto the depth of two using the command `find /home/$HOSTNAME/ -mindepth 0 -maxdepth 2`.
* The following code snippet is used to display the absolute path of the .txt files, **provided that a text file exists in the Assignment1 directory**. If no text file exists, no error is printed.
  * `ls *.txt &>/dev/null`
The `ls.*txt` command lists all the .txt files if they exist in the directory. If they do not exist, the error message is given. The output of this command is redirected to `/dev/null` so that it remains hidden and is not displayed, since the error message needs to be hidden.
  * `if [ $? -eq 0 ];  then ls *.txt | xargs realpath; fi`
This command checks the exit status of the previously executed `ls.txt` command using `$?`. If it is 0, it means that atleast one .txt file exists and the absolute path of the .txt files is printed. If no .txt file is present, nothing will be printed.

## q2 .sh
* The input is taken from the user and stored in the variable *input*.
* The length of the input is taken by using the command `length=${#input}`. I have used this length to optimise searching for the input in the list of commands.
* Sorted the input by using `sorted_input=$(echo $input | grep -o . | sort | tr -d "\n")`
* Then, I got a list of commands that have the same length as the input using `i=$(compgen -c | grep -x '.\{'$length'\}')` . By filtering based on length, the search space is reduced considerably.
* Then, I sorted each command in the list and then compared it with the input.
* If the sorted input matches with any sorted command, then I printed "Yes" and the original command after it. If there is no match, I printed "No" as the output.

## q3 .sh
* The commands that are written into .bash_history file on exiting the terminal. I have accessed those commands **of the previous session** using `cat ~/.bash_history`.
* The last 10 commands will be obtained by the command ` tail -n 10`.
* The command will be specified only in the first column . So, I obtained the first column of all 10 commands using `awk '{ print $1 }'`.
* I counted the unique commands using `| sort | uniq -c` .
* The command list is required in the decreasing order of usage. So, we sort the count (first filed) in reverse order using `sort -r $1`.
* Since the format required is `command_name count` used  `awk '{ print $2 " " $1}'` for getting the answer in the rquired format.


## q4 .sh
* The input is read in the form of a string.
* All the brackets are removed and replaced with spaces using `sed 's/[()]/ /g'`.
* Now, running the above command will lead to unneccessary double spaces in some cases. So, I am squeezing the spaces using `tr -s " " ` command.
* Now, to remove the spaces at the begginning and at the end of the string, I used the command `sed -e 's/^[[:space:]]//'| sed -e 's/[[:space:]]$//'`. 
* Then, finally to add the brackets at the beginning and the end of the string, I used the command `sed 's/\(^.*$\)/\(\1\)/g'`which just appends '(' at the beginning and ')' at the end of the string.

## q5 .sh
* The input is read and first converted into a lowercase string using `s=$(echo "${input,,}")`.
* The string is reverse using `$(rev <<< "$s")` and compared with the lowercased input. If they match, print "Yes", else print "No".

## q6 .sh
* Assuming that the inputs are in the **integer** format only.
* Took the number of the command line arguments and stored it in a variable using the command `number=$#`.
* Stored all the command line arguments in the form of an input array using the command `inputs=( "$@" )`.
* Initialised the variable 'exp' as the first variable using `exp=${inputs[0]}`.
* Ran a for loop for remaining elements to update the result of exponentiation with every number.
* Printed the result using `echo $exp`.

## q7 .sh
* The information about the running processes is generated using the command `ps au`. The process ID (PID) is the second field. Since only the process IDs are to be stored in the pid.txt file, we retrive the second column using awk command `awk '{ print $2 }'`. The heading "PID" is removed using `tail -n +2` and the PIDs are finally redirected to file using `> pid.txt`.
* The N value is taken from the user using the command `read input`.
* To get the count of PIDs present, I counted the lines in the file pid.txt using the command `maxPIDs=$(cat pid.txt | wc -l)`.
* The input number has to be restricted to the maximum count of PIDs. This is acheived by the command `.
if [ $input -gt $maxPIDs ] 
then
input=$maxPIDs
fi`
* The N smallest PIDs are printed to stdout using the command `cat pid.txt | head -n $input`. Since the PIDs are already sorted, there is no need to sort them explicitly again.

## q8 .sh
* The name of the crontab file is taken as the command line argument. The crontab file is run using the command `crontab "$1" &>/dev/null`.
* To check if the crontab command has executed properly, we compare it with $?. If it returns 0, the file has been executed properly and so it is properly formatted and the output is printed as "Yes". Else, "No" is printed.
`if [ $? -eq 0 ]; then
    echo "Yes"
else
    echo "No"
fi
`
## q9. sh
* The input is read from the user using `read input` and all the spaces in the input are removed using the command `input=$(echo $input | tr -d ' ')`.
* The length of the input is obtained using `length=${#input}`.
* First, I checked that the string contains only digits using `"$(echo "$input" | sed 's/[0-9]//g')"` . If the string contains any other characters other than digits, the output is returned as "Invalid" and the execution stops. 
* If the length of the input is 1, then also the output is printed as "Invalid" and the execution stops.
* Now, the `Luhn algorithm` is followed and the sum of the digits is obtained using the `for loop` for traversing through the digits and `if-else statements` to check if the position of the digits is even or odd (for doubling the digits at the even position). If sum is divisible by 10, we print "Yes", else we print "No".

## q10. sh
* The operator and number of operands are input using the commands `read op` and `read n`.
* The result variable is initialised to the first variable. So, we read the first operand as `read result`.
* For rest of the operands, we use a `for loop` for fetching and simultaneously keep updating the result according to the operator using the basic calculator (bc) command: `
result=$(echo "$result $op $input" | bc -l) 
`.
* Finally, we print the result rounded off upto 4 decimal places using the command `echo $result | xargs printf "%.4f"`.














