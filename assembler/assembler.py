def first_pass(path, symbol_table):
    file = open(path, "r")
    ignore = set(["/", "\n"])
    linecounter = 0
    instruction_list = []
    for line in file:
        if line[0] in ignore:
            continue
        if line[0] == "(":
            new_symbol = line.strip("\n")
            new_symbol = new_symbol.replace(" ", "")
            new_symbol = new_symbol.split("/")[0]
            new_symbol = new_symbol.strip("(")
            new_symbol = new_symbol.strip(")")
            symbol_table[new_symbol] = str(linecounter)
        else:
            new_line = line.strip("\n")
            new_line = new_line.replace(" ", "")
            new_line = new_line.split("/")[0]
            instruction_list.append(new_line)
            linecounter+=1
    file.close()
    return instruction_list, symbol_table

def second_pass(instruction_list, symbol_table):

    def a_instruction(instruction, variable_counter):
        if not instruction.isnumeric():
            if instruction in symbol_table:
                instruction = int(symbol_table[instruction])
            else:
                symbol_table[instruction] = str(variable_counter)
                instruction = variable_counter
                variable_counter += 1
        a_number = format(int(instruction), '016b')
        binary_instructions.append(a_number)
        return variable_counter

    def c_instruction(instruction):
        a0_instruction_map = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100",
                           "A": "110000", "!D": "001101", "!A": "110001", "-D": "001111",
                           "-A": "110001", "D+1": "011111", "A+1": "110111", "D-1": "001110",
                           "A-1": "110010", "D+A": "000010", "D-A": "010011", "A-D": "000111",
                           "D&A": "000000", "D|A": "010101"}
        a1_instruction_map = {"M": "110000", "!M": "110001", "-M": "110011", "M+1": "110111",
                              "M-1": "110010", "D+M": "000010", "D-M": "010011", "M-D": "000111",
                              "D&M": "000000", "D|M": "010101"}
        destination_map = {"null": "000", "M": "001", "D": "010", "MD": "011", "A": "100",
                           "AM":"101", "AD": "110", "AMD": "111"}
        jump_map = {"JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", 
                    "JLE": "110", "JMP": "111"}

        start = "111"
        dest = "000"
        jump = "000"

        if "=" in instruction:
            command_list = instruction.split("=")
            dest = destination_map[command_list[0]]
            instruction = command_list[1]

        if ";" in instruction:
            command_list = instruction.split(";")
            instruction = command_list[0]
            jump = jump_map[command_list[1]]

        if instruction in a1_instruction_map:
            comp = "1" + a1_instruction_map[instruction]
        else:
            comp = "0" + a0_instruction_map[instruction]

        final_instruction = start + comp + dest + jump
        binary_instructions.append(final_instruction)
    
    binary_instructions = []
    variable_counter = 16
    for instruction in instruction_list:
        if instruction[0] == "@":
            variable_counter = a_instruction(instruction[1:], variable_counter)
        else:
            c_instruction(instruction)
    return binary_instructions

symbol_table = {"SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1", "ARG": "2",
                "THIS": "3", "THAT": "4", "WRITE": "18", "END": "22"}
for i in range(16):
    symbol_table["R"+str(i)] = str(i)

if __name__ == "__main__":
    filename = "Pong"
    instruction_list, symbol_table = first_pass(filename + ".asm", symbol_table)
    binary_instructions = second_pass(instruction_list, symbol_table)
    file = open(filename + ".hack", "w")
    for instruction in binary_instructions:
        file.write(instruction + "\n")
    file.close()
