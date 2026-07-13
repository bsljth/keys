import inspect

class KeysMachine():
    def __init__(self):
        self.stack = []
        self.ram = [0] * 64
        self.ip = 0
        self.code = []
        self.max_ticks = 256
        self.tick = 0
        self.registers = {
            "IX": 0,
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "DX": 0,
        }
        self.error = ""
        self.error_line = 0
        self.halted = False

    def assert_test(test, message, self):
        if not test:
            display_op = self.cur_op.join(" ") if self.cur_op else None
            self.error_line = self.ip
            print(f"Halt: {message} at line #{self.ip}: {display_op}")
            self.error = message
            self.halted = True

        return test

    def register_names(self):
        return self.registers.keys()

    def operations():
        # TODO
        return [method[0] for method in inspect.getmembers(
            KeysMachine,
            predicate=inspect.ismethod,
        )].

    def get_stack_top(self):
        return self.stack[self.stack.len() - 1]

